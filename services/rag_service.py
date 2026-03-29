import pandas as pd

df = pd.read_csv("data/crop_knowledge.csv")

# Normalize column names
df.columns = df.columns.str.lower().str.strip()

# 🔍 Smart column mapping
COLUMN_MAP = {
    "disease": ["disease", "problem", "issue", "infection"],
    "treatment": ["treatment", "solution", "remedy", "chemical"],
    "organic": ["organic", "bio", "natural"],
    "notes": ["notes", "info", "details", "symptoms"]
}

def find_column(possible_names):
    for name in possible_names:
        if name in df.columns:
            return name
    return None

# Auto-detect columns
disease_col = find_column(COLUMN_MAP["disease"])
treatment_col = find_column(COLUMN_MAP["treatment"])
organic_col = find_column(COLUMN_MAP["organic"])
notes_col = find_column(COLUMN_MAP["notes"])


def retrieve_knowledge(query):

    try:
        if not disease_col:
            return "⚠️ No disease column found in dataset."

        matches = df[df[disease_col].astype(str).str.contains(query, case=False, na=False)]

        if matches.empty:
            return "No exact match found. Possible fungal or bacterial issue."

        results = []

        for _, row in matches.head(3).iterrows():

            entry = f"Disease: {row.get(disease_col, 'N/A')}"

            if treatment_col:
                entry += f" | Treatment: {row.get(treatment_col, 'N/A')}"

            if organic_col:
                entry += f" | Organic: {row.get(organic_col, 'N/A')}"

            if notes_col:
                entry += f" | Notes: {row.get(notes_col, 'N/A')}"

            results.append(entry)

        return "\n".join(results)

    except Exception as e:
        return f"Knowledge retrieval error: {str(e)}"