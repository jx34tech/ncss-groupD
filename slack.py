from flaskapp import app
from flask import request
import requests
from flask import jsonify
from words import no_query_on_input_all, word_on_enter_all, word_on_input_all, word_no_on_input_all, word_no_on_enter_all, on_enter_all,on_input_all
import re
state = 'NO QUERY'
context={}
from words import global_no_input_state_set

@app.route('/writing', methods=['GET', 'POST'])
def kind_word():
    global state,context
    output = []
    text = request.values['text']
    state, context, input_output = on_input_all(state, text,context)
    enter_output = on_enter_all(state,context)
    output.append(input_output)
    output.append(enter_output)
    while state in global_no_input_state_set:
        state, context, input_output = on_input_all(state, '',context)
        enter_output = on_enter_all(state,context)
        output.append(input_output)
        output.append(enter_output)
    response = ' '.join(i for i in output if i).strip()
    return jsonify({"text": response,
"response_type": "in_channel"})