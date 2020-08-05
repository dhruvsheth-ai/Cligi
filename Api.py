from flask import Flask, request, abort
from tinydb import TinyDB, Query
from tinydb.operations import delete, increment, decrement, add, subtract, set
import json
import threading
# from app.mainscript import main
  
app = Flask(__name__) 
db = TinyDB('db.json')
density_table = db.table('density_table')
mask_table = db.table('mask_table')
violation_table = db.table('violation_table')
  
@app.route("/") 
def home_view(): 
    return "<h1>Welcome to Cligi</h1><h5>API server for Edge Devices</h5>"
