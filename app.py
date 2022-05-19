from flask import *
import pickle

app = Flask(__name__, static_url_path='/static')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def Home():
    return render_template('index.html')
	
@app.route("/add", methods = ['POST'])

def predict():
    if request.method == 'POST':
        BALANCE_TENURE = int(request.form['BALANCE_TENURE'])
        CURRENT_INTEREST_RATE_MAX = float(request.form['CURRENT_INTEREST_RATE_MAX'])
        DPD = int(request.form['DPD'])
        EMI_DueAmount = float(request.form['EMI_DueAmount'])
        EMI_OS_AMOUNT = int(request.form['EMI_OS_AMOUNT'])
        FOIR = float(request.form['FOIR'])
        NET_LTV = float(request.form['NET_LTV'])
        NET_RECEIVABLE = float(request.form['NET_RECEIVABLE'])
        OUTSTANDING_PRINCIPAL = float(request.form['OUTSTANDING_PRINCIPAL'])
        DUEDAY_5= int(request.form['DUEDAY_5'])
        DUEDAY_15= int(request.form['DUEDAY_15'])
        PRODUCT_LAP= int(request.form['PRODUCT_LAP'])
        PRODUCT_STHL= int(request.form['PRODUCT_STHL'])
        PRODUCT_STLAP= int(request.form['PRODUCT_STLAP'])
        
        prediction = model.predict([[BALANCE_TENURE, CURRENT_INTEREST_RATE_MAX, DPD, EMI_DueAmount, EMI_OS_AMOUNT, FOIR, NET_LTV,NET_RECEIVABLE,OUTSTANDING_PRINCIPAL,DUEDAY_5,DUEDAY_15,PRODUCT_LAP,PRODUCT_STHL,PRODUCT_STLAP]])
        pred = prediction[0]
        out = "Error"
        if pred ==1:out = "Survived"
        else: out = "Didn't Survived"
        
        worksheet.append_row([name, out])
        return render_template('index.html', results = out)
    else:
        return render_template('index.html')
        
if __name__ == "__main__":
	app.run(debug = True)