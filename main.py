from flask import Flask, render_template, request
import jabutiGPIO

#instacia o jabuti passando os pinos do controle do servo
jabuti = jabutiGPIO.motor(11,7)

app = Flask(__name__)
comandos = [] 
print(comandos)

@app.route('/', methods=['GET', 'POST'])
def hello_name():
   global comandos
   print("request", request.method)
   if request.method == 'POST':
      if request.form['submit_button'] == 'direitaR':
         print("DireitaR")
         jabuti.queue(['direita'])
      if request.form['submit_button'] == 'reR':
         print("reR")
         jabuti.queue(["re"])
      if request.form['submit_button'] == 'frenteR':
         print("frenteR")
         jabuti.queue(['frente'])
      if request.form['submit_button'] == 'esquerdaR':
         print("esquerdaR")
         jabuti.queue(["esquerda"])

      if request.form['submit_button'] == 'direita':
         print("Direita")
         comandos.append("direita")
      if request.form['submit_button'] == 're':
         print("re")
         comandos.append("re")
      if request.form['submit_button'] == 'frente':
         print("frente")
         comandos.append("frente")
      if request.form['submit_button'] == 'esquerda':
         print("esquerda")
         comandos.append("esquerda")
      if request.form['submit_button'] == 'enviar':
         print("enviado")
         jabuti.queue(comandos)
         comandos = []
      if request.form['submit_button'] == 'limpar':
         print("limpo")
         comandos = []
      
   print(comandos)
   return render_template("jabuti.html", comandos= comandos)

   

if __name__ == '__main__':
   app.run(host='0.0.0.0',  debug=True)