from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/verificar', methods=['POST'])  # Define uma rota '/verificar' que aceita apenas requisições POST
def resultado():
    temperatura = float(request.form['temperatura'])
    if temperatura < 37.2:
       mensagem = 'temperatura normal'
    elif 37.3 <= temperatura < 38:
        mensagem = 'estado febril'
    elif 38 <= temperatura < 39:
        mensagem = 'febre'
    else:
        mensagem = 'febre alta'
    return render_template('index.html', msg=mensagem)


if (__name__) == ('__main__'):
    # Inicia o servidor Flask em modo de depuração se este script for executado diretamente
    app.run(debug=True)