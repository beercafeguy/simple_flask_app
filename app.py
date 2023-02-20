from flask import Flask,render_template,redirect,request,jsonify
import math
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route("/math",methods=['POST'])
def math_operation():
    if request.method == "POST":
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = 0
        if operation == "add":
            result_tmp = num1+num2
            result = "Sum of {} and {} is {}".format(num1,num2,result_tmp)
        if operation == "subtract":
            result_tmp = num1 - num2
            result = "Subtraction of {} and {} is {}".format(num1,num2,result_tmp)
        if operation == "multiply":
            result_tmp = num1*num2
            result = "Multiplication of {} and {} is {}".format(num1,num2,result_tmp)
        if operation == "divide":
            result_tmp = num1/num2
            result = "Division of {} and {} is {}".format(num1,num2,result_tmp)
        if operation == "log":
            result_tmp = math.log(num1,num2)
            result = "LOG of {} and {} is {}".format(num1,num2,result_tmp)
        return render_template("results.html",result=result)    

@app.route("/math_postman",methods=['POST'])
def math_operation_postman():
    if request.method == "POST":
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        result = 0
        if operation == "add":
            result_tmp = num1+num2
            result = "Sum of {} and {} is {}".format(num1,num2,result_tmp)
        if operation == "subtract":
            result_tmp = num1 - num2
            result = "Subtraction of {} and {} is {}".format(num1,num2,result_tmp)
        if operation == "multiply":
            result_tmp = num1*num2
            result = "Multiplication of {} and {} is {}".format(num1,num2,result_tmp)
        if operation == "divide":
            result_tmp = num1/num2
            result = "Division of {} and {} is {}".format(num1,num2,result_tmp)
        if operation == "log":
            result_tmp = math.log(num1,num2)
            result = "LOG of {} and {} is {}".format(num1,num2,result_tmp)
        return jsonify({'result':result})   

if __name__ == "__main__":
    app.run(host="0.0.0.0")
