# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 19:39:39 2022

@author: acczj
"""

from flask import Flask,render_template,request
import joblib

app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        rate = float(request.form.get("rate"))
        model = joblib.load("linear_regression")
        results = model.predict([[rate]])
        return(render_template("index.html", result=results))
    else:
        
        return(render_template("index.html", result="Loading"))
    
if __name__=="__main__":
    app.run()
