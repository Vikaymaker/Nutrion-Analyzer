from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuration for serving static files
app.config['STATIC_FOLDER'] = 'static'
app.config['DEBUG'] = 'True'

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vijay",
    database="analysis"
)
mycursor = mydb.cursor()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Insert new user into the database with phone number
        # Assume you have your database connection and cursor set up already
        sql = "INSERT INTO users (username, email, password) VALUES ( %s, %s, %s)"
        val = (username, email, password)
        mycursor.execute(sql, val)
        mydb.commit()

        # Redirect to login page after successful registration
        return redirect(url_for('signin'))

    return render_template('signup.html')


# Route for the login form
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Placeholder for database query, replace this with your actual database code
        # For demonstration purposes, let's assume user exists
        user_exists = True

        if user_exists:
            # User authentication successful, redirect to home page or dashboard
            return render_template('home.html', email=email)
        else:
            error = "Login failed. Please try again."
            return render_template('signin.html', error=error)

    # If the request method is GET, render the login page
    return render_template('signin.html')

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/fitness')
def fitness():
    return render_template('fitness.html')

@app.route('/diet')
def diet():
    return render_template('diet.html')

@app.route('/personal')
def personal():
    return render_template('personal.html')

@app.route('/classify', methods=['POST'])
def classify_image():
    if 'file' not in request.files:
        return 'No file uploaded!'

    file = request.files['file']
    if file.filename == '':
        return 'No file selected!'

    # Check if the file is an image (you can add more image formats if needed)
    if file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        classify_result = classify_fruit_or_vegetable(file)
        return render_template('result.html', result=classify_result)
    else:
        return 'Invalid file format! Please upload a valid image.'

def classify_fruit_or_vegetable(image_file):
    filename = image_file.filename.lower()

    if 'apple' in filename:
        return {
            'name': 'Apple',
            'description': 'A fruit with a sweet taste and various health benefits.',
            'sugar': '10g',
            'fat_saturated': '0.3g',
            'calories': '52 kcal',
            'cholesterol': '0mg',
            'protein': '0.3g',
            'carbohydrate': '14g'
        }
    elif 'banana' in filename:
        return {
            'name': 'Banana',
            'description': 'A tropical fruit rich in potassium and fiber.',
            'sugar': '12g',
            'fat_saturated': '0.4g',
            'calories': '89 kcal',
            'cholesterol': '0mg',
            'protein': '1.1g',
            'carbohydrate': '23g'
        }
    elif 'orange' in filename:
        return {
            'name': 'Orange',
            'description': 'A citrus fruit high in vitamin C and antioxidants.',
            'sugar': '9g',
            'fat_saturated': '0.2g',
            'calories': '47 kcal',
            'cholesterol': '0mg',
            'protein': '0.9g',
            'carbohydrate': '12g'
        }
    elif 'pineapple' in filename:
        return {
            'name': 'Pineapple',
            'description': 'A tropical fruit known for its sweet and tangy flavor.',
            'sugar': '16g',
            'fat_saturated': '0.1g',
            'calories': '50 kcal',
            'cholesterol': '0mg',
            'protein': '0.5g',
            'carbohydrate': '13g'
        }
    elif 'watermelon' in filename:
        return {
            'name': 'Watermelon',
            'description': 'A juicy fruit with high water content and vitamins.',
            'sugar': '6g',
            'fat_saturated': '0.1g',
            'calories': '30 kcal',
            'cholesterol': '0mg',
            'protein': '0.6g',
            'carbohydrate': '8g'
        }
    elif 'tomato' in filename:
        return {
            'name': 'Tomato',
            'description': 'A versatile fruit commonly used in salads and cooking.',
            'sugar': '2.6g',
            'fat_saturated': '0.03g',
            'calories': '18 kcal',
            'cholesterol': '0mg',
            'protein': '0.9g',
            'carbohydrate': '3.9g'
        }
    elif 'carrot' in filename:
        return {
            'name': 'Carrot',
            'description': 'A root vegetable rich in beta-carotene and fiber.',
            'sugar': '4.7g',
            'fat_saturated': '0.2g',
            'calories': '41 kcal',
            'cholesterol': '0mg',
            'protein': '0.9g',
            'carbohydrate': '9.6g'
        }
    elif 'broccoli' in filename:
        return {
            'name': 'Broccoli',
            'description': 'A nutrient-rich vegetable known for its antioxidant properties.',
            'sugar': '1.6g',
            'fat_saturated': '0.1g',
            'calories': '55 kcal',
            'cholesterol': '0mg',
            'protein': '4.2g',
            'carbohydrate': '11g'
        }
    elif 'spinach' in filename:
        return {
            'name': 'Spinach',
            'description': 'A leafy green vegetable packed with vitamins and minerals.',
            'sugar': '0.4g',
            'fat_saturated': '0.1g',
            'calories': '23 kcal',
            'cholesterol': '0mg',
            'protein': '2.9g',
            'carbohydrate': '3.6g'
        }
    elif 'cucumber' in filename:
        return {
            'name': 'Cucumber',
            'description': 'A refreshing vegetable with high water content.',
            'sugar': '1.8g',
            'fat_saturated': '0.1g',
            'calories': '15 kcal',
            'cholesterol': '0mg',
            'protein': '0.7g',
            'carbohydrate': '3.6g'
        }
    else:
        return {'name': 'Unknown', 'description': 'Unable to classify.'}

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
