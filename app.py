from flask import Flask, render_template, request
import requests
import pickle
import numpy as np
app = Flask(__name__)
model = pickle.load(open('forest.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
    
        radius_mean = eval(request.form['radius_mean'])
        texture_mean = eval(request.form['texture_mean'])
        perimeter_mean = eval(request.form['perimeter_mean'])
        area_mean = eval(request.form['area_mean'])
        smoothness_mean = eval(request.form['smoothness_mean'])
        compactness_mean = eval(request.form['compactness_mean'])

        #
        concavity_mean = eval(request.form['concavity_mean'])
        concave_points_mean = eval(request.form['concave points_mean'])
        symmetry_mean = eval(request.form['symmetry_mean'])
        fractal_dimension_mean = eval(request.form['fractal_dimension_mean'])
        radius_se = eval(request.form['radius_se'])
        texture_se = eval(request.form['texture_se'])
        ##
        perimeter_se = eval(request.form['perimeter_se'])
        area_se = eval(request.form['area_se'])
        smoothness_se = eval(request.form['smoothness_se'])
        compactness_se = eval(request.form['compactness_se'])
        concavity_se = eval(request.form['concavity_se'])
        concave_points_se = eval(request.form['concave points_se'])

        symmetry_se = eval(request.form['symmetry_se'])
       

        fractal_dimension_se = eval(request.form['fractal_dimension_se'])
        radius_worst = eval(request.form['radius_worst'])
        texture_worst = eval(request.form['texture_worst'])
        perimeter_worst = eval(request.form['perimeter_worst'])

        ###
        area_worst = eval(request.form['area_worst'])

        smoothness_worst = eval(request.form['smoothness_worst'])
        concave_points_worst = eval(request.form['concave points_worst'])


        compactness_worst = eval(request.form['compactness_worst'])
        concavity_worst = eval(request.form['concavity_worst'])
        symmetry_worst = eval(request.form['symmetry_worst'])
        fractal_dimension_worst = eval(request.form['fractal_dimension_worst'])



        prediction=model.predict([[radius_mean,texture_mean,perimeter_mean,area_mean,
        smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,
        radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,
        fractal_dimension_se,radius_worst,texture_worst, perimeter_worst,area_worst,smoothness_worst,
        compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]])
        output=prediction
        if output==1:
            return render_template('index.htm',prediction_texts="Malignant Immediately Go to hospital and Do all Tests")
        else:
            return render_template('index.html',prediction_text="Benign, No worry")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run()