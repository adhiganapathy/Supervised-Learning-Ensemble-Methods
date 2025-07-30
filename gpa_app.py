from flask import Flask, request,render_template
import pickle
import json
app=Flask(__name__)



@app.route("/init_GPA",methods=["POST"])
def predict():
    request_data=request.json["sat_scores"]
    picklefilepath=r"C:\Users\Adhi Ganapathy\Documents\Python_ws\Linear Regression 13072025\Model\Linear_reg.pkl"
    with open(picklefilepath,'rb') as File:
        load_model = pickle.load(File)
    gpa_result =load_model.predict([[request_data]])[0][0]
    return json.dumps({"gpa_grade":gpa_result})

@app.route("/home",methods=["GET"])
def home():
    return render_template("index.html") 

@app.route("/predict_GPA",methods=["POST"])
def main():
    StudentName=request.form.get("StudentName")
    sat_scores=float(request.form.get("sat_scores"))
    picklefilepath=r"C:\Users\Adhi Ganapathy\Documents\Python_ws\Linear Regression 13072025\Model\Linear_reg.pkl"
    with open(picklefilepath,'rb') as File:
        load_model = pickle.load(File)
    gpa_result =load_model.predict([[sat_scores]])[0][0]
    return render_template("predict.html",gpa_result=gpa_result,StudentName=StudentName) 
if __name__=="__main__":                          
    app.run(port="8090")    