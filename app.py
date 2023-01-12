from flask import Flask, render_template, request
import requests
from summarizer import summarization



app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def home():
    return render_template("index.html")

@app.route("/text_summary",methods = ["GET","POST"])
def text_summary():
    if request.method == "POST":
        rawtext = request.form["rawtext"]
        summary,original_text, len_summary, len_originaltext = summarization(rawtext)

    return render_template("textsummary.html",summary=summary,original_text=original_text, len_summary=len_summary, len_originaltext=len_originaltext)


if __name__=="__main__":
    app.run(debug=True)
