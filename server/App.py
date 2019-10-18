from flask import Flask,request
from flask_cors import CORS
import _sql
import json


app = Flask(__name__)

CORS(app, origins="*", methods=['GET', 'POST'],allow_headers=[
        "Content-Type", "Authorization", "Access-Control-Allow-Credentials","Access-Control-Allow-Origin","Access-Control-Allow-Headers"],
        supports_credentials=True)


@app.route('/login',methods = ['POST'])
def login():
    data = json.loads(request.data)
    return _sql.DbHelper.login(data['username'], data['password'])


@app.route('/signup',methods = ['POST'])
def signup():
    data = json.loads(request.data)
    _sql.DbHelper.sign_up(data['username'],data['password'],data['height'],data['weight'],data['bp'],data['sugar'],data['smoke'],data['alcohol'],data['foodpref'])
    return {"res" : "sucess"}


@app.route('/suggestions',methods = ['POST'])
def suggest():
    data = json.loads(request.data)
    return _sql.DbHelper.suggestions(data['username'])


@app.route('/appointment', methods = ['POST'])
def appointment():
    data = json.loads(request.data)
    _sql.DbHelper.appointment(data['username'])
    return {"res":"success"}

@app.route('/schedule', methods = ['GET'])
def appointment_schedule():
    return _sql.DbHelper.schedule()

if __name__ == '__main__':
    app.run()














