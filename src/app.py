from flask import Flask
app = Flask(_name_)
@app.route('/')
def index():
return "Bye Jesus!"
@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int):
return a + b