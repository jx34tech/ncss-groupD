import re
import requests
from words import no_query_on_input_all, word_on_enter_all, word_on_input_all, word_no_on_input_all, word_no_on_enter_all, on_enter_all,on_input_all

global_no_input_state_set = {"RHYME+WORD+NO"}

def no_query_on_input(text,context):
   return no_query_on_input_all("rhyme", text, context)
    
def RHYME_WORD_on_enter(context):
    return word_on_enter_all("rhyme", context)

def RHYME_WORD_on_input(text,context):
    return word_on_input_all("rhyme", text, context)

def RHYME_WORD_NO_on_input(text,context):
    return word_no_on_input_all("rhyme", text, context)

def RHYME_WORD_NO_on_enter(context):
    return word_no_on_enter_all("rhyme", context)

def on_enter(state,context):
    return on_enter_all("rhyme", state, context)

def on_input(state, text,context):
    return on_input_all('rhyme', state, text, context)


    

