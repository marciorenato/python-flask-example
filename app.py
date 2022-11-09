from flask import Flask, Response
import os
cont=0

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Ola, mundo!"

@app.route("/health")
def health():
     return Response("ok", status=200)

@app.route("/counter")
def counter():
    global cont
    cont = cont+1
    return str(cont)

    
@app.route("/version")
def version_route():
    return "2.0.0"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ["APP_PORT"], debug=True) 
