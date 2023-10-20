"""
Copyright (C) 2023 SE Slash - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: slashse2023@gmail.com

"""
from flask import Flask, request, render_template, session, jsonify
from src.modules.scraper import driver
# import json
# from src.firebase_config import auth

app = Flask(__name__, template_folder=".")


@app.route("/")
def landingpage():
    return render_template("./static/landing.html")


# @app.route("/",methods=["POST","GET"])
# def landingpage():
#     if request.method == "POST" :
#         email = request.form.get("email")
#         password = request.form.get("password")
#
#         try:
#             user = auth.sign_in_with_email_and_password(email,password)
#             session['user'] = email
#         except:
#             return "Failed to Login"
#
#     return render_template("./static/landing.html")
#
#
# @app.route("/signup",methods=["POST","GET"])
# def signup():
#     if request.method == "POST":
#         email = request.form.get("email")
#         password = request.form.get("password")
#         try:
#             auth.create_user_with_email_and_password(email, password)
#             return render_template("/")
#         except:
#             return "Account creation failed"
#
#
#
#     return render_template("./static/signup.html")


@app.route("/search", methods=["POST", "GET"])
def product_search(new_product="", sort=None, currency=None, num=None):
    product = request.args.get("product_name")
    if product == None:
        product = new_product
    isRestApi = request.headers.get('Content-Type','') == 'application/json'
    data = driver(product, currency, num, 0, False, None, True, sort, isRestApi)
    if isRestApi:
        return jsonify(data)

    return render_template("./static/result.html", data=data, prod=product)


@app.route("/filter", methods=["POST", "GET"])
def product_search_filtered():
    product = request.args.get("product_name")
    sort = request.form["sort"]
    currency = request.form["currency"]
    num = request.form["num"]

    if sort == "default":
        sort = None
    if currency == "usd":
        currency = None
    if num == "default":
        num = None
    return product_search(product, sort, currency, num)
