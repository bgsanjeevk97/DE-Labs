from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate-bmi', methods=['POST'])
def calculate_bmi():
    try:
        data = request.get_json()
        weight = float(data.get('weight'))  # in kg
        height = float(data.get('height'))  # in meters
        
        if weight <= 0 or height <= 0:
            return jsonify({'error': 'Weight and height must be positive numbers'}), 400
        
        # BMI = weight (kg) / height (m)^2
        bmi = weight / (height ** 2)
        
        # Determine BMI category
        if bmi < 18.5:
            category = 'Underweight'
        elif 18.5 <= bmi < 25:
            category = 'Normal weight'
        elif 25 <= bmi < 30:
            category = 'Overweight'
        else:
            category = 'Obese'
        
        return jsonify({
            'bmi': round(bmi, 2),
            'category': category
        })
    
    except ValueError:
        return jsonify({'error': 'Invalid input. Please enter valid numbers'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
