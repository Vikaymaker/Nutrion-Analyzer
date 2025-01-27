import os
import numpy as np
from flask import Flask, render_template, request
import requests
import image
from keras.src.saving import load_model

app = Flask(__name__, template_folder="templates")

# Loading the model
model = load_model('nutrition.h5')
print("Loaded model from disk")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/image1', methods=['GET', 'POST'])
def image1():
    return render_template("image.html")

@app.route('/predict', methods=['POST'])
def launch():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        filepath = os.path.join(basepath, "uploads", f.filename)
        f.save(filepath)

        img = image.load_img(filepath, target_size=(64, 64))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        pred = np.argmax(model.predict(x), axis=1)
        print("prediction", pred)
        index = ['APPLES', 'BANANA', 'ORANGE', 'PINEAPPLE', 'WATERMELON']
        result = index[pred[0]]

        nutrition_info = nutrition(result)
        print(nutrition_info)

        return render_template("0.html", showcase=nutrition_info, showcase1=result)

def nutrition(index):
    url = "https://calorieninjas.p.rapidapi.com/v1/nutrition"
    querystring = {"query": index}
    headers = {
        'x-rapidapi-key': "5d797ab107mshe668f26bd044e64p1ffd34jsnf47bfa9a8ee4",
        'x-rapidapi-host': "calorieninjas.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()['items']

if __name__ == "__main__":
    app.run(debug=False)
