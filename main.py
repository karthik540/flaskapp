from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "<center><h1>It Worked !!</h1></center>"

if __name__ == '__main__':
    app.run(host = '0.0.0.0' , port = 5000)