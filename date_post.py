from flask import Flask, jsonify, request
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_date():
    ## POST method
    if request.method == 'POST':
        try:
            wich_date =json.loads(request.form['flag'].lower())
            
            if wich_date:
                formated_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")#aaaa-mm-dd hh:ii:ss
            else:
                formated_date=datetime.now().strftime("%Y-%m-%d")#aaaa-mm-dd
            print(wich_date)  
            response_object = dict({
                'date': formated_date
            })
            return jsonify(response_object), 200
        except: ## Catch exception if bad Request
            response_object = dict({
                'Error': 'Bad Request. Expecting body with boolean variable named flag.'
            })
            return response_object, 400
    ## GET method
    else:
        response_object = dict({
            'Error': 'Method Not Allowed.'
        })
        return response_object, 405
