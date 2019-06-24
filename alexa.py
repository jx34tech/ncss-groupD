from flask import jsonify,request
from flaskapp import app
import words
import syn
state = 'ON LAUNCH'
context={}

@app.route('/alexa', methods=['POST', 'GET'])
def alexa():
    global state,context
    output = []
    data=request.get_json()
    request_type=data['request']['type']
    if request_type=='LaunchRequest':
        enter_output = syn.on_enter_all(state,context)
        output.append(enter_output)
    elif request_type=='IntentRequest':
        text=data['request']['intent']['slots']['query']['value']
        
        state, context, input_output = syn.on_input_all(state, text,context)
        enter_output = syn.on_enter_all(state,context)
        output.append(input_output)
        output.append(enter_output)
        while state in syn.global_no_input_state_set:
            state, context, input_output = syn.on_input_all(state, '',context)
            enter_output = syn.on_enter_all(state,context)
            output.append(input_output)
            output.append(enter_output)
    return jsonify({
        'version': '0.1',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': '. '.join(i for i in output if i),
            },
            'shouldEndSession': False,
        },
    })