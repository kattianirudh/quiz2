from ast import keyword
from colorama import Cursor
from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
import pyodbc

app = Flask(__name__)
class Main():
    def initial():
        print("Done")


if __name__ == "__main__":

  app.logger.debug("Loading ")

  app.run(
    host='0.0.0.0', 
    port=9001)
