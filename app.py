from flask import Flask, render_template, request

app = Flask(__name__)

# Function to calculate body fat percentage
def calculate_body_fat(weight, waist, wrist, hip, forearm, gender):
    try:
        if gender == 'male':
            # Body fat percentage formula for males
            body_fat_percentage = (495 / (1.0324 - 0.19077 * (waist / weight) + 0.15456 * (hip / weight))) - 450
        else:
            # Body fat percentage formula for females
            body_fat_percentage = (495 / (1.29579 - 0.35004 * (waist / weight) + 0.22100 * (hip / weight))) - 450

        return round(body_fat_percentage, 2)
    except ZeroDivisionError:
        return "Invalid inputs"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    weight = float(request.form['weight'])
    waist = float(request.form['waist'])
    wrist = float(request.form['wrist'])
    hip = float(request.form['hip'])
    forearm = float(request.form['forearm'])
    gender = request.form['gender']

    body_fat_percentage = calculate_body_fat(weight, waist, wrist, hip, forearm, gender)
    
    return render_template('result.html', body_fat_percentage=body_fat_percentage)

if __name__ == '__main__':
    app.run(debug=True)
