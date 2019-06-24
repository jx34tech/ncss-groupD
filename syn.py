import re
import requests
from words import no_query_on_input_all, word_on_enter_all, word_on_input_all, word_no_on_input_all, word_no_on_enter_all, on_enter_all, on_input_all

global_no_input_state_set = {"WORD+NO"}

def no_query_on_input(text, context):
    return no_query_on_input_all("synonym", text, context)
    
def SYNONYM_WORD_on_enter(context):
    return word_on_enter_all("synonym", context)

def SYNONYM_WORD_on_input(text, context):
    return word_on_input_all("synonym", text, context)

def SYNONYM_WORD_NO_on_input(text,context):
    return word_no_on_input_all("synonym", text, context)

def SYNONYM_WORD_NO_on_enter(context):
    return word_no_on_enter_all("synonym", context)

def on_enter(state,context):
    return on_enter_all("synonym", state, context)

def on_input(state, text,context):
    return on_input_all('synonym', state, text, context)

