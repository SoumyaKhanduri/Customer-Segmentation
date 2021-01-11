from flask import Flask, render_template, request
import joblib,pickle
import numpy as np


from flask import Flask,render_template

app=Flask(__name__,template_folder='template')

app = Flask(__name__)
# Load the Random Forest model
model = joblib.load('model.pkl')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    Total_purchase = (request.form['Total_purchase'])
    times_bought = (request.form['times_bought'])
    last_purchase = (request.form['last_purchase'])


    data = [[Total_purchase, times_bought, last_purchase]]
    
    prediction = model.predict(data)

    if float(prediction) == 0:
        return render_template('index.html', prediction_text='This is not a Fraud Transaction')
    elif float(prediction) == 1:
        return render_template('index.html', prediction_text='This is not a Fraud Transaction')
    elif float(prediction) == 2:
        return render_template('index.html', prediction_text='This is not a Fraud Transaction')
        
            
if __name__ == "__main__":
    app.run(debug=False) # use debug = False for jupyter notebook