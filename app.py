from flask import Flask, render_template, request
import pandas as pd
from data_preprocess import preprocess
import pickle
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/predict/', methods=['POST'])
def predict_reaction_rate(preprocessed_data):
    EC_C = float(request.form['EC_C'])
    BC_C = float(request.form['BC_C'])
    PMS_C = float(request.form['PMS_C'])
    pH = float(request.form['pH'])
    Bio = float(request.form['Bio'])
    T = float(request.form['T'])
    O_C = float(request.form['O_C'])
    Raman = float(request.form['Raman'])
    SSA = float(request.form['SSA'])
    VIP = float(request.form['VIP'])
    Gap = float(request.form['Gap'])
    HN = float(request.form['HN'])
    input_data = pd.DataFrame({
        "EC-C": [EC_C],
        "BC-C": [BC_C],
        "PMS-C": [PMS_C],
        "pH": [pH],
        "Bio": [Bio],
        "T": [T],
        "O/C": [O_C],
        "Id/Ig": [Raman],
        "SSA": [SSA],
        "VIP": [VIP],
        "Gap": [Gap],
        "HN": [HN]
    })
    preprocessed_data = preprocess(input_data)

    prediction = predict_reaction_rate(preprocessed_data)

    return render_template('Web.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
