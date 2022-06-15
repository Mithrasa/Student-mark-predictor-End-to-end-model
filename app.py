#import the needed libraries
import numpy as np
from flask import Flask,render_template,url_for,request,jsonify
import pickle
import re
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)
model1 = pickle.load(open('model1.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])

def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model1.predict(final_features)
    return render_template('index.html', prediction_text='Marks{}'.format(prediction))
'''
@app.route('/predict_ap',methods=['POST'])
def predict_api():
    data=request.get_json(force=True)
    prediction=model.predict([np.array(list(data.values()))])
    output=prediction[0]
    return jsonify(output)
'''
if __name__ == "__main__":
    app.run(debug=True)



