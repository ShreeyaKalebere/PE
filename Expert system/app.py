from flask import Flask, render_template, request

app = Flask(__name__)

# --- Expert system rules ---
def diagnose(symptoms):
    symptoms = [s.lower() for s in symptoms]

    # --- Respiratory Diseases ---
    if 'fever' in symptoms and 'cough' in symptoms and 'sore throat' in symptoms:
        return "You may have a Common Cold or Mild Flu. Rest well and drink warm fluids."
    elif 'fever' in symptoms and 'shortness of breath' in symptoms and 'chest pain' in symptoms:
        return "These could be signs of a Respiratory Infection or Pneumonia. Please consult a doctor immediately."
    elif 'runny nose' in symptoms and 'sneezing' in symptoms and 'itching' in symptoms:
        return "You may be experiencing an Allergy or Seasonal Rhinitis. Avoid dust and pollen exposure."
    elif 'cough' in symptoms and 'fatigue' in symptoms and 'fever' in symptoms:
        return "You might be suffering from Bronchitis or Viral Infection. Drink warm fluids and rest."

    # --- Digestive Diseases ---
    elif 'stomach pain' in symptoms and ('nausea' in symptoms or 'vomiting' in symptoms):
        return "You may have Food Poisoning or Indigestion. Stay hydrated and avoid oily foods."
    elif 'diarrhea' in symptoms and 'stomach pain' in symptoms and 'fever' in symptoms:
        return "You might have Gastroenteritis (Stomach Flu). Drink fluids and consult a doctor."
    elif 'bloating' in symptoms and 'heartburn' in symptoms and 'constipation' in symptoms:
        return "These symptoms suggest Acid Reflux or Gastritis. Avoid spicy and acidic foods."
    elif 'nausea' in symptoms and 'headache' in symptoms:
        return "You may be experiencing Migraine-related nausea. Take rest in a quiet room."

    # --- Skin / Allergy Related ---
    elif 'rash' in symptoms and 'itching' in symptoms and 'redness' in symptoms:
        return "You may have a Skin Allergy or Dermatitis. Use mild lotion and avoid harsh soaps."
    elif 'swelling' in symptoms and 'pain' in symptoms and 'redness' in symptoms:
        return "This may indicate an Infection or Inflammation. Apply a cold compress and see a doctor."
    elif 'itching' in symptoms and 'dry skin' in symptoms:
        return "You may have Eczema or Dry Skin Condition. Keep your skin moisturized."

    # --- Neurological / Mental ---
    elif 'headache' in symptoms and 'fatigue' in symptoms:
        return "You may be Dehydrated or Stressed. Drink water and take adequate rest."
    elif 'dizziness' in symptoms and 'confusion' in symptoms:
        return "Possible sign of Low Blood Pressure or Anemia. Check your iron intake."
    elif 'anxiety' in symptoms and 'sleepiness' in symptoms:
        return "You might be suffering from Stress or Mild Depression. Try relaxation or meditation."
    elif 'difficulty concentrating' in symptoms and 'fatigue' in symptoms:
        return "You may have Sleep Deprivation or Vitamin Deficiency."

    # --- Body Pain / Fever Related ---
    elif 'body ache' in symptoms and 'fever' in symptoms:
        return "You may have a Viral Infection or Influenza. Rest and stay hydrated."
    elif 'muscle pain' in symptoms and 'joint pain' in symptoms:
        return "You might have Rheumatic Pain or Muscle Strain. Gentle stretching and warm compress may help."
    elif 'back pain' in symptoms and 'fatigue' in symptoms:
        return "Possible cause: Poor posture, muscle strain, or stress. Do light exercises and take breaks."
    elif 'chills' in symptoms and 'fever' in symptoms and 'sweating' in symptoms:
        return "This combination can indicate Malaria or Viral Infection. Consult a healthcare provider."

    # --- Eye / Head Issues ---
    elif 'headache' in symptoms and 'eye pain' in symptoms:
        return "You may have Eye Strain or Migraine. Avoid screen time and rest your eyes."
    elif 'blurred vision' in symptoms and 'dizziness' in symptoms:
        return "You might have Vision-related issues or Low Blood Sugar. Check with an eye specialist."

    # --- Default ---
    else:
        return "Symptoms unclear or overlapping. Please consult a doctor for accurate diagnosis."


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def get_diagnosis():
    symptoms = request.form.getlist('symptoms')
    result = diagnose(symptoms)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
