import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/", methods=["GET"])
def hack4hope():
    return render_template("hack4hope.html")

@app.route("/clinical-trials", methods=["GET"])
def websites():
    return render_template("websites.html")