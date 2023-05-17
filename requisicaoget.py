import pyodbc
from flask import Flask, jsonify
from flask_cors import CORS


conectionString = 'Driver={SQL Server Native Client 11.0};Server=DESKTOP-HL3N4UQ;Database=Pizzaria;Trusted_Connection=yes;'

# Instancia aplicação
app = Flask(__name__)
CORS(app)

#Criar controller api get

@app.route('/materiaprimas')
def materiaprimas():
    try: 
        #conection banco
        connection = pyodbc.connect(conectionString)

        #cursor para realizar a consulta
        cursor = connection.cursor()

        #Execução da consulta SELECT 
        cursor.execute('SELECT Id, Descricao, Estoque FROM dbo.MateriaPrimas')

        #Recuperação da query , resultados
        results = cursor.fetchall()

        #converte para json
        json_results = []

        for resultado in results:
            json_results.append ({
                'Id': resultado[0],
                'Descricao': resultado[1],
                'Estoque': resultado[2]
            })

        #fechar resultado
        cursor.close()

        connection.close()



        #retorno formato json
        return jsonify(json_results)
    
    except Exception as e:
        return str(e)
    
if __name__ == '__main__':
    app.run()






