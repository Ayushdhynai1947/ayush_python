from flask import Flask

app = Flask(__name__)

@app.route('/')
def heelo():
    return 'hellow wold'


if __name__ =='__main__':
    app.run(debug=True)