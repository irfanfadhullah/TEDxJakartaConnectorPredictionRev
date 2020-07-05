from flask import render_template, request, url_for, flash, redirect
from flaskblog.__innit__ import app
from flaskblog.forms import PredictForm
import joblib
import numpy as np
import pandas as pd
model = joblib.load('model/model.pickle')

@app.route('/')
@app.route('/home')
def home():
    return render_template('frontpage.html')

@app.route('/mainpage',methods = ['GET','POST'])
def mainpage():
    return render_template('connectorhub.html', title = "Connector Analysis")   

@app.route('/inputparameter' ,methods = ['GET','POST'])
def inputparameter():
    form = PredictForm()
    if form.validate_on_submit():
        return redirect(url_for('hasil'))
    
    return render_template('connectorparameter.html', title = "Parameter Input", form=form)   

@app.route('/result', methods = ['GET','POST'])
def result():
    user = []
    user = [
        {
     	    
                gender=request.form.get("gender")
    		following=request.form.get("following")
    		follower=request.form.get("follower")
    		totaltweet=request.form.get("totaltweet")
    		baru=np.array([gender, following, follower,totaltweet]).reshape((1,-1))
    		x_new = model.predict(baru)
		hasil=x_new[0]
        }


    ]


    
    return render_template('hasil.html', title = "Hasil Predict", user=user) 

