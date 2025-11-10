from flask import Flask, request, jsonify, render_template, json
#from main import ler_dados

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        data=request.get_data()       
        return jsonify(data)
    
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        data=request.json()
        usuario_e_senha = json.loads(data)
        return jsonify(data)
    
@app.route("/soma/<numero1>/<numero2>", methods=['GET', 'POST'])
def soma(numero1, numero2):
    if request.method == 'GET':
        return f"<h1> {int(numero1)+int(numero2)}</h1>"
    elif request.method == 'POST':
        return



if __name__=="__main__":
    app.run()