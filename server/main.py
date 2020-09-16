__author__ = "Jordan Zdimirovic"
__lnk__ = "https://github.com/jordstar20001/FunctionCtrlPanel"

# CONSTS
LOGINS_PATH = "data/LOGINS"
TOKEN_LEN = 30
# IMPORTS
import json
import utils
from flask import Flask, request, jsonify
import requests
import random
import socket_helper as sh
# GLOBAL VARS
valid_tokens = []
LOGINS = []

with open(LOGINS_PATH, 'r') as f:
    LOGINS = json.loads(f.read())

# Init flask server

app = Flask("main")

@app.route("/login", methods=["POST"])
def login():
    u, p = request.json["username"], request.json["password"]
    for l in LOGINS:
        if u == l.username and p == l.password:
            # Generate login token
            m_token = utils.random_hex_str(TOKEN_LEN)
            # Add to valid tokens
            valid_tokens.append(m_token)
            # Reply to request
            return m_token, 200

    return 403

class ClientRequestHandler(sh.brh):
    global app
    def handle(handler):
        print(app)
        data = json.loads(handler.request.recv(1024).strip().decode())
        print(handler.request.getpeername())

csm = sh.ClientSocketManager(("0.0.0.0", 8081), ClientRequestHandler)
csm.start()

app.run("0.0.0.0", 8080)