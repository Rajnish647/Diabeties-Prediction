
from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("model_pickle", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")



@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        preg = request.form["Preg"]
        Glucose = request.form["Glucose"]
        BloodPressure = request.form["BloodPressure"]
        SkinThickness = request.form["SkinThickness"]
        Insulin = request.form["Insulin"]
        BMI = request.form["BMI"]
        Dia = request.form["Dia"]
        Age = request.form["Age"]

        #print(Age, Dia, BMI, Insulin, SkinThickness, BloodPressure, Glucose, preg)
        prediction = model.predict([[preg, Glucose, BloodPressure, SkinThickness, Insulin, BMI, Dia, Age]])

        output = prediction[0]

        return render_template('home.html',prediction_text=" Chance of you having a Diabeties is {}".format(output))

    return render_template("home.html")
        




if __name__ == "__main__":
    app.run(debug=True)