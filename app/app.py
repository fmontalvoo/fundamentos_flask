from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    data = {'title': 'Inicio', 'header': 'Bienvenido(a)'}
    return render_template('index.html', data=data)


@app.route('/contact')
def contact():
    data = {'title': 'Contacto', 'header': 'Contactanos'}
    return render_template('contact.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
