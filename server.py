from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Bienvenido al curso de Telemática - Prueba final'

@app.route('/render')
def render():
    return render_template('hello.html')

if __name__ == "__main__":
    app.run (host="0.0.0.0", port=5050)
