from flask import Flask, request, jsonify
import json
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, \
                               unset_jwt_cookies, jwt_required, JWTManager


from script import main
from flask_wtf import FlaskForm 
from wtforms import SubmitField, StringField, TextAreaField, IntegerField, BooleanField, RadioField
from wtforms.validators import DataRequired, InputRequired


api = Flask(__name__)
api.config["JWT_SECRET_KEY"] = "changeme"
jwt = JWTManager(api)

@api.route('/profile')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }

    return response_body

class UserInput(FlaskForm):
    key = StringField('Enter Keyword', validators=[InputRequired()])
    submit = SubmitField('Submit')

@api.route('/searchtrend/<key>', methods=['GET','POST'])
def search_trend(key):
    # form = UserInput()

    # if form.validate_on_submit():
    #     data = form.key.data
    #     tweets = main(data)
    #     for t in tweets 
    
    tweets = main(key)
    pos = 0
    neg = 0
    neu = 0
    total = len(tweets)
    pos_av = 0
    neg_av = 0
    neu_av = 0

    for t in tweets:
        
        if t == "positive":
            pos +=1
        elif t == "negative":
            neg +=1
        elif t == "neutral":
            neu +=1
    
    pos_av = pos/total
    neu_av = neu/total
    
    data = {
        "positive" : pos,
        "negative" : neg,
        "neutral" : neu,
        "positive tweets average": pos_av,
        "negative tweets average": neg_av,
        "neutral tweets average": neu_av,
    }

    return data
    


