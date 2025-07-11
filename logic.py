import pandas as pd
# Suggest health items based on place and season
def get_health_suggestions(place, season):
    data = pd.read_csv("rules.csv")
    row = data[(data["Location"] == place) & (data["Season"] == season)]
    if not row.empty:
        return row.iloc[0]["Suggestions"].split("|")
    return ["No suggestions found for this condition."]
# Get patient info from file
def get_medical_history(name):
    data = pd.read_csv("medical_history.csv")
    found = data[data["Name"].str.lower() == name.lower()]
    if not found.empty:
        return found.iloc[0].to_dict()
    return {"Error": "Patient record not found."}
# Suggest doctor based on location and issue
def get_doctor_recommendations(city, symptom):
    data = pd.read_csv("doctors.csv")
    results = data[(data["Location"] == city) & (data["Specialty"].str.contains(symptom, case=False))]
    if results.empty:
        return ["No doctor available for this issue."]
    return [row["Name"] + " - " + row["Specialty"] for _, row in results.iterrows()]
# Check entered heart rate and oxygen level
def check_vitals(heart_rate, spo2):
    heart_rate = int(heart_rate)
    spo2 = int(spo2)
    alerts = []
    if heart_rate < 60 or heart_rate > 100:
        alerts.append("Heart rate not normal")
    if spo2 < 94:
        alerts.append("Low oxygen level")
    if not alerts:
        return ["Vitals look fine"]
    return alerts
