import pandas as pd

# Load dataset
df = pd.read_csv("data/schemes.csv")

# Normalize columns
df.columns = df.columns.str.lower().str.strip()

# ✅ Correct column mapping (based on your CSV)
disease_col = "disease/pest"
scheme_col = "government scheme/support"
benefit_col = "key benefit of control"
type_col = "type"


def get_schemes(text, risk, weather):
    try:
        # 🔍 Match disease from user text
        text = text.lower()

        matched = df[df[disease_col].str.lower().apply(lambda x: x in text)]

        # If no direct match → fallback to all
        if matched.empty:
            matched = df

        # 🔥 Risk-based filtering
        if risk.get("risk_percent", 0) > 60:
            matched = matched[matched[type_col].str.contains("fungal|pest", case=False, na=False)]

        top = matched.head(3)

        schemes = []
        for _, row in top.iterrows():
            schemes.append({
                "name": str(row.get(scheme_col)),
                "benefit": str(row.get(benefit_col)),
                "eligibility": "Applicable for farmers facing this issue"
            })

        # ✅ Fallback (VERY IMPORTANT)
        if not schemes:
            schemes = [
                {
                    "name": "PMFBY",
                    "benefit": "Crop insurance against losses",
                    "eligibility": "All farmers"
                },
                {
                    "name": "PM-KISAN",
                    "benefit": "₹6000/year income support",
                    "eligibility": "Small & marginal farmers"
                }
            ]

        return schemes

    except Exception as e:
        print("Scheme error:", e)
        return []