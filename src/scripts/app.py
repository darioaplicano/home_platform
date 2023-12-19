from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '¡Hola, esta es tu primera web con Flask!'

if __name__ == '__main__':
    app.run(debug=True, port=8080)
