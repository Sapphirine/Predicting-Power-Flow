#import libraries
import numpy as np
from flask import Flask, request, render_template
import joblib
import pandas as pd
import plotly
import plotly.express as px
import json

#Initialize the flask App
app = Flask(__name__)
model = joblib.load(open('clf.pkl', 'rb'))

#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = np.round(prediction[0], 2)

    return render_template('index.html', prediction_text='Power Flow Prediction is: {}'.format(output))

@app.route('/chart1')
def chart1():
    df = pd.read_csv(r"C:\Users\rohan\Desktop\ELENE6895_Project\Forecast Data\10 Years Ahead\all_forecast.csv")

    fig = px.line(df, x="Date", y="Energy Demand (MWh)", color="Zone")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Energy Demand Forecast in New England"
    description = """
    10-year ahead energy demand (MWh) forecast for each zone in New England.
    """
    return render_template('charts.html', graphJSON=graphJSON, header=header,description=description)

if __name__ == "__main__":
    app.run(debug=True)