import re
import requests
global_no_input_state_set = {"WORD+NO"}

def no_query_on_input_all(text, context):
    match_word_no = re.match(r".*?(?P<number>[0-9]+) .*(?P<kind>rhyme|synonym|association|homophone|adjective|antonym)s? (?:with|for) (?P<word>.*)", text.lower())
    match_word = re.match(r".*?(?P<kind>rhyme|synonym|association|homophone|adjective|antonym)s? (?:with|for) (?P<word>.*)", text.lower())
    if match_word_no:
        number = match_word_no.group('number')
        word = match_word_no.group('word')
        kind = match_word_no.group('kind')
        context['word'] = word
        context['number'] = number
        context['kind'] = kind
        return "WORD+NO",context, ""
    elif match_word:
        word = match_word.group('word')
        kind = match_word.group('kind')
        context['word'] = word
        context['kind'] = kind
        return "WORD",context, ""
    else:
        return "NO QUERY",context, "That request is invalid. Try again."

def word_on_enter_all(context):

    return f"How many {context['kind']}s were you after?"

def word_on_input_all(text, context):
    number = text
    if number.isdigit():
        context['number'] = number
        return "WORD+NO",context, ""
    else:
        return "WORD",context, "That request is invalid. Try again."

def word_no_on_input_all(text, context):
    return 'NO QUERY',context,''

def word_no_on_enter_all(context):
    number = context['number']
    word = context['word']
    kind = context['kind']
    if kind == "synonym":
        url = f"https://api.datamuse.com/words?rel_syn={word}&max={number}"
    elif kind == "rhyme":
        url = f"https://api.datamuse.com/words?rel_rhy={word}&max={number}"
    elif kind == 'association':
        url = f"https://api.datamuse.com/words?rel_trg={word}&max={number}"
    elif kind == 'homophone':
        url = f'https://api.datamuse.com/words?sl={word}&max={number}'
    elif kind == 'adjective':
        url = f'https://api.datamuse.com/words?rel_jjb={word}&max={number}'
    elif kind == 'antonym':
        url = f"https://api.datamuse.com/words?rel_ant={word}&max={number}"
    response = requests.get(url)
    result = response.json()
    return_values = []
    for i in result:
        return_values.append(i['word'])
    if len(return_values) == 0:
        return f'There are no {kind}s for "{word}"'
    else:
        number_of_values = len(return_values)
        value_string = ', '.join(return_values)
        if number_of_values == 1:
            return f'Here is {number_of_values} {kind} for "{word}": {value_string}\n'
        else:
            return f'Here is {number_of_values} {kind}s for "{word}": {value_string}\n'

def on_enter_all(state, context):
    if state == 'WORD':
        return word_on_enter_all(context)
    elif state == 'WORD+NO':
        return word_no_on_enter_all(context)
    elif state == 'NO QUERY':
        return ''
    elif state == 'ON LAUNCH':
        return "Hey, welcome to the writing assistant!"

def on_input_all(state, text,context):
    if state == 'NO QUERY': 
        return no_query_on_input_all(text,context)
    elif state == 'ON LAUNCH':
        return no_query_on_input_all(text,context)
    elif state == 'WORD':
        return word_on_input_all(text,context)
    elif state == 'WORD+NO':
        return word_no_on_input_all(text,context)


def on_launch_enter_all(context):
    return "Hey, welcome to the writing assistant!"
