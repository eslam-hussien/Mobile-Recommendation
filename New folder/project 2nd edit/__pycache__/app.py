import os

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

from models import *


@app.route('/about_us_.html', methods=['GET'])
def about_us():
    return render_template("about_us_.html")


@app.route('/Blog.html', methods=['GET'])
def blog():
    return render_template("Blog.html")


@app.route('/', methods=['GET','POST'])
def landing_page():
   return render_template("Home.html")


@app.route('/Home', methods=['GET'])
def home():
    return render_template("Home.html")


@app.route('/login.html', methods=['GET'])
def login():
    return render_template("login.html")


@app.route('/mobile_buy_now.html', methods=['GET'])
def modbileBuynow():
    return render_template("mobile_buy_now.html")


@app.route('/mobile_details.html', methods=['GET'])
def mobiledetails():
    return render_template("mobile_details.html")


@app.route('/mobile_gallery.html', methods=['GET'])
def mobilegallery():
    ...
    return render_template("mobile_gallery.html")


@app.route('/mobile_reviews.html', methods=['GET'])
def mobilereviews():
    ...
    return render_template("mobile_reviews.html")


@app.route('/personal.html', methods=['GET'])
def personal():
    return render_template("personal.html")


@app.route('/remember_password.html', methods=['GET'])
def remmemberpassword():
    return render_template("remember_password.html")


@app.route('/result.html', methods=['GET'])
def result():
    return render_template("result.html")


@app.route('/sign_up1.html', methods=['GET'])
def singup():
    return render_template("sign_up1.html")


@app.route('/technical_1.html', methods=['GET','POST'])
def tech1():
    return render_template("technical_1.html")


@app.route('/technical_2.html', methods=['GET','POST'])
def tech2():
    return render_template("technical_2.html")


@app.route('/technical_3.html', methods=['GET','POST'])
def tech3():
    return render_template("technical_3.html")


@app.route('/technical_4.html', methods=['GET','POST'])
def tech4():
    return render_template("technical_4.html")


@app.route('/technical_5.html',methods=['GET','POST'])
def tech5():
    return render_template("technical_5.html")


@app.route('/technical_6.html', methods=['GET','POST'])
def tech6():
    return render_template("technical_6.html")


@app.route('/technical_7___1.html', methods=['GET','POST'])
def tech7():
    return render_template("technical_7___1.html")

#henaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
#l2aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
@app.route('/top10Battery.html', methods=['GET'])
def top10battery():
    return render_template("top10 Battery.html")

@app.route('/top10Browsing.html', methods=['GET'])
def top10browsing():
    return render_template("top10 Browsing.html")


@app.route('/top10Camera.html', methods=['GET'])
def top10camera():
    return render_template("top10 Camera.html")


@app.route('/top10CPU.html', methods=['GET'])
def top10cpu():
    return render_template("top10 CPU.html")



@app.route('/top10Games.html', methods=['GET'])
def top10games():
    return render_template("top10 Games.html")


@app.route('/top10Media.html', methods=['GET'])
def top10media():
    return render_template("top10 Media.html")


@app.route('/top10Screen.html', methods=['GET'])
def top10screen():
    return render_template("top10 Screen.html")

@app.route('/top10SocialMedia.html', methods=['GET'])
def top10socialmedia():
    return render_template("top10 SocialMedia.html")



if __name__ == '__main__':
    app.run()
