from flask import Flask, request, render_template, url_for, redirect

app=Flask(__name__)

notas=[]
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', notas=notas)
    elif request.method == 'POST':
        anotação = request.form['nota']
        notas.append(anotação)
        return redirect(url_for('index'))
    
    