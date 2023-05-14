import os
from flask import Flask, request, jsonify, make_response, Response, render_template
import cv2
import pickle
import socket
import numpy as np
from paperswithcode import PapersWithCode

CONST_BASE_PATH = os.path.dirname(__file__)
app = Flask(__name__)
agent = PapersWithCode()

@app.route("/pdf/<pdf_file>", methods=['GET'])
def show_pdf(pdf_file):
    return render_template("pdf.html", filename=pdf_file, header=f"http://127.0.0.1:8084")

@app.route("/")
def main():
    data = agent.get()
    return render_template("index.html", paperinfo=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8084))
    app.run(host='0.0.0.0', port=port)
