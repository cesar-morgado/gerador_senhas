from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    return senha

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar_senha', methods=['GET'])
def senha():
    comprimento = int(request.args.get('comprimento'))
    nova_senha = gerar_senha(comprimento)
    return nova_senha

if __name__ == '__main__':
    app.run(debug=True)
