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
    
    Purchase = (request.form['Purchase'])
    Freqency = (request.form['Freqency'])
    last_purchase = (request.form['last_purchase'])


    data = [[Purchase, Freqency, last_purchase]]
    
    prediction = model.predict(data)

    if float(prediction) == 0:
        return render_template('index.html', prediction_text='High value customer')
    elif float(prediction) == 1:
        return render_template('index.html', prediction_text='Medium value customer')
    elif float(prediction) == 2:
        return render_template('index.html', prediction_text='Low value customer ')
        
            
if __name__ == "__main__":
    app.run(debug=False) # use debug = False for jupyter notebook