from rhyme import on_enter, on_input, global_no_input_state_set
state = 'NO QUERY'
context={}
while state != 'END':
  output = on_enter(state,context)
  if output:
    print(output)
  if state not in global_no_input_state_set:
    user_input = input('> ')
  state, context, output = on_input(state, user_input,context)
  if output:
    print (output)