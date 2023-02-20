from flask import Flask,render_template,redirect,request,jsonify
import math
import mongo_utils

app = Flask(__name__)
col_name = "dim_users"

@app.route("/",methods=['GET','POST'])
def home_page():
    return "<p> simple user details app</p>"

@app.route("/users",methods=['POST'])
def math_operation():
    if request.method == "POST":
        user_name = request.json['user_name']
        print(mongo_utils.find_users(col_name))
        if mongo_utils.find_user(user_name,col_name) != None:
            return jsonify(mongo_utils.find_user(user_name, col_name))
        else:
            return jsonify({'error':'User Not Found'})

if __name__ == "__main__":
    app.run(host="0.0.0.0")
