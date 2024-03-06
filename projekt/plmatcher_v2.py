import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.impute import SimpleImputer

# Läs in datasetet
df = pd.read_csv("matcheskaggle.csv")

# Omvandla matchutgång till numeriskt värde
df["result_numeric"] = df["result"].map({"W": 2, "D": 1, "L": 0})

# Konvertera time till numeriskt värde
df["time_decimal"] = (
    pd.to_datetime(df["time"], format="%H:%M").dt.hour
    + pd.to_datetime(df["time"], format="%H:%M").dt.minute / 60
)

# Välj relevanta features/parametrar från datasetet
features = [
    # "xg",
    # "xga",
    # "poss",
    "venue",
    # "sh",
    # "sot",
    # "dist",
    "referee",
    "team",
    "time_decimal",
    "opponent",
]
X = df[features]
y = df["result_numeric"]

# Numeriska variabler
# numerical_features = ["xg", "xga", "poss", "sh", "sot", "dist", "time_decimal"]
numerical_features = ["time_decimal"]
numerical_transformer = SimpleImputer(strategy="mean")

# Kategoriska variabler
categorical_features = ["venue", "referee", "team", "opponent"]
categorical_transformer = OneHotEncoder(handle_unknown="ignore")

# Preprocessor-pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", categorical_transformer, categorical_features),
        ("num", numerical_transformer, numerical_features),
    ]
)

# Uppdatera pipelines för RandomForest och LogisticRegression
rf_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(random_state=42)),
    ]
)

lr_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=10000, random_state=42)),
    ]
)


# Korsvalidering
rf_scores = cross_val_score(rf_pipeline, X, y, cv=5)
lr_scores = cross_val_score(lr_pipeline, X, y, cv=5)

print(f"RandomForest: {rf_scores.mean():.2f} +/- {rf_scores.std():.2f}")
print(f"LogisticRegression: {lr_scores.mean():.2f} +/- {lr_scores.std():.2f}")

# Träna RandomForest och LogisticRegression med 80% av matcherna och testa på 20%
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

rf_pipeline.fit(X_train, y_train)
lr_pipeline.fit(X_train, y_train)

rf_predictions = rf_pipeline.predict(X_test)
lr_predictions = lr_pipeline.predict(X_test)

# Visa resultat i detalj
print("\nRandomForest:")
print(classification_report(y_test, rf_predictions))
print(confusion_matrix(y_test, rf_predictions))

print("\LogisticRegression:")
print(classification_report(y_test, lr_predictions))
print(confusion_matrix(y_test, lr_predictions))

# Tillägg: vill ta reda på hur viktig varje parameter är för att beräkna resultatet, med feature_importances_
# Hämta importance-värden
importances = rf_pipeline.named_steps["classifier"].feature_importances_

cat_feature_names = (
    rf_pipeline.named_steps["preprocessor"]
    .named_transformers_["cat"]
    .get_feature_names_out(categorical_features)
)
# Sammanställ alla parametrar
feature_names = list(cat_feature_names) + numerical_features

# Skapa en DataFrame med parametrar och deras viktning
importances_df = pd.DataFrame(
    {"Parameter": feature_names, "Viktning": importances}
).sort_values(by="Viktning", ascending=False)

# Spara DataFrame till en fil
importances_df.to_csv("importances.txt", index=False, sep="\t")
