# AC01 - FrameworksFullStack
from flask import Flask, request 

app = Flask(__name__)

@app.route('/media', methods=['POST', 'GET']) # Nova Rota http://localhost:5000/media
def calcular_media():
    resultado = 'Entre as notas na URL'

    nota1 = request.args.get('nota1')
    nota2 = request.args.get('nota2')

    if nota1 and nota2:

        nota1 = float(nota1)
        nota2 = float(nota2)

        media = (nota1 + nota2) / 2
        if media >= 7:
            resultado = 'Aprovado'
        elif media >= 4:
            reultado = 'DP'
        else:
            resultado = 'Reprovado'
    
    return resultado
    

if __name__ == '__main__':
    app.run(debug=True)  # Executando a aplicação 

# URL http://127.0.0.1:5000/media?nota1=5.5&nota2=1 