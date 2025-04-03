import streamlit as st

st.title("🎈 Cardio Health Risk Assessment")
def calculate_cardio_risk(age, bmi, smoker, cholesterol, blood_pressure):
    risk_score = 0
    
    # Age factor
    if age >= 45:
        risk_score += 2
    if age >= 55:
        risk_score += 3
    if age >= 65:
        risk_score += 4
    
    # BMI factor
    if bmi >= 25:
        risk_score += 2
    if bmi >= 30:
        risk_score += 3
    if bmi >= 35:
        risk_score += 4
    
    # Smoking factor
    if smoker:
        risk_score += 3
    
    # Cholesterol factor (mg/dL)
    if cholesterol >= 200:
        risk_score += 2
    if cholesterol >= 240:
        risk_score += 3
    if cholesterol >= 280:
        risk_score += 4
    
    # Blood pressure factor (systolic BP)
    if blood_pressure >= 130:
        risk_score += 2
    if blood_pressure >= 140:
        risk_score += 3
    if blood_pressure >= 160:
        risk_score += 4
    
    # Risk level assessment
    if risk_score <= 4:
        return "Low risk"
    elif risk_score <= 8:
        return "Moderate risk"
    elif risk_score <= 12:
        return "High risk"
    else:
        return "Very high risk"

# Example usage
if __name__ == "__main__":
    age = int(input("Enter age: "))
    bmi = float(input("Enter BMI: "))
    smoker = input("Are you a smoker? (yes/no): ").strip().lower() == "yes"
    cholesterol = float(input("Enter cholesterol level (mg/dL): "))
    blood_pressure = float(input("Enter systolic blood pressure: "))
    
    risk = calculate_cardio_risk(age, bmi, smoker, cholesterol, blood_pressure)
    print(f"Cardiovascular Health Risk: {risk}")
