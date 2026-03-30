from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    # Listen on all interfaces (0.0.0.0) so it works in Docker/Kubernetes
    app.run(host='0.0.0.0', port=8080)
