from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder



app = Flask(__name__, template_folder='templates')

#-------- MODEL -----------#

pipe = pickle.load(open("pipe.pkl", 'rb'))

#-------- ROUTES-----------#

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def predict_price():
    args = request.form
    print(args)
    data = pd.DataFrame({
        'LotArea': [args.get('LotArea')],
        'LotFrontage': [args.get('LotFrontage')],
        'OverallQual': [args.get('OverallQual')],
        'OverallCond': [args.get('OverallCond')],
        'YearBuilt': [args.get('YearBuilt')],
        'GrLivArea': [args.get('GrLivArea')],
        'BsmtFinSF1': [args.get('BsmtFinSF1')],
        'GarageArea': [args.get('GarageArea')],
        'TotalBsmtSF': [args.get('TotalBsmtSF')],
        'YearRemodAdd': [args.get('YearRemodAdd')],
    })

    prediction = f'${int(np.exp(pipe.predict(data)[0])*1.4)} CAD'
    return render_template('result.html', prediction=prediction)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
