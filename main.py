from flask import Flask, jsonify
from flask_restful import Resource, Api
from algoPrediction import * 

app = Flask(__name__)
api = Api(app)

class Algo(Resource):
    def get(self,ticker):

        finalScore,mVal,rVal,sVal = getAPIData(ticker)
        recLine = "recommendation: " + finalScore
        macdLine = "Name: MACD" + "\n\tScore:" + str(mVal) + "\n"
        rocLine = "Name: ROC" + " \n\tScore:"+ str(rVal) + "\n"
        stochLine = "Name: STOCH" + "\n\tScore:" + str(sVal) + "\n"
        returnString = recLine + ",\n" + "kpis: [\n{\n\t" + macdLine + "},\n\n{\n\t" + rocLine + "},\n\n{\n\t" + stochLine + "}\n]"

        return jsonify({'data':returnString})

api.add_resource(Algo, '/add/<string:ticker>')

if __name__ == '__main__':
    app.run()
