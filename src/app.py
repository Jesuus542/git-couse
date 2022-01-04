from flask import Flask
app = Flask(_name_)
@app.route('/')
def index():
return "Bye Jesus!"
@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int):
  nums_sum = a + b
return f"la suma es : {str(nums_sum)}"
@app.route('/multiply/<int:a</<int:b>')
def multiply = floar (a * b)
retur f"el resultado de la multipli es: {str(result)}"
