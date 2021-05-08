from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    data = {'title': 'Inicio', 'header': 'Bienvenido(a)'}
    return render_template('index.html', data=data)


@app.route('/contact')
def contact():
    data = {'title': 'Contacto', 'header': 'Contactanos'}
    return render_template('contact.html', data=data)


@app.route('/greetings/<name>')
def greetings(name):
    return 'Hola {}'.format(name)


@app.route('/sum/<int:a>/<int:b>')
def sum(a, b):
    return '{a} + {b} = {c}'.format(a=a, b=b, c=a+b)


@app.route('/languages')
def languages():
    data = {'title': 'Lengaujes', 'languages': [
        'Python', 'Java', 'Dart', 'JavaScript']}
    return render_template('languages.html', data=data)

# /data?name=Frank&age=25
@app.route('/data')
def data():
    name = request.args.get('name')
    age = request.args.get('age')
    return 'Nombre: {name} y Edad: {age}'.format(name=name, age=age)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
