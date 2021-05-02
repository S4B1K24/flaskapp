print("Hello world")
from flask import flask
app = flask(__name__)
#декоратор для вывода страницы по умолчанию
@app.route("/")
def hello():
 return " <html><head></head> <body> Hello World! </body></html>"
if __name__ == "__main__":
 app.run(host='127.0.0.1',port=5000) 
from flask import render_template
@app.route("/data_to")
def data_to():
 #создаем переменные с данными для передачи в шаблон
 some_pars = {'user':'Ivan','color':'red'}
 some_str = 'Hello my dear friends!'
 some_value = 10
 #передаем данные в шаблон и вызываем его
 return render_template('simple.html',some_str = some_str, some_value = some_value,some_pars=some_pars)
