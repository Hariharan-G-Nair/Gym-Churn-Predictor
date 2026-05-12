from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load trained model
with open('gym_churn_model.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect form data
        input_data = {
            'Avg_Workout_Duration_Min': float(request.form['Avg_Workout_Duration_Min']),
            'Membership_Duration_Days': float(request.form['Membership_Duration_Days']),
            'Gender': request.form['Gender'],
            'Membership_Type': request.form['Membership_Type'],
            'Favorite_Exercise': request.form['Favorite_Exercise'],
            'Joining_Season': request.form['Joining_Season'],
            'Age_Group': request.form['Age_Group']
        }

        # Convert to DataFrame
        data = pd.DataFrame([input_data])

        # Predict churn
        prediction = model.predict(data)[0]
        probability = model.predict_proba(data)[0][1]

        result = 'Customer Will Churn' if prediction == 1 else 'Customer Will Stay'

        return render_template(
            'index.html',
            prediction_text=result,
            probability=round(probability * 100, 2)
        )

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')


if __name__ == '__main__':
    app.run(debug=True)