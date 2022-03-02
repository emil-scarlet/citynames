import re
from natsort import natsorted
state_ids = (input("states"))
state_ids_array = state_ids.split(",")
state_ids_array_output = natsorted(state_ids_array)
state="state = "
sharp=" #"
for state_output in state_ids_array_output:
    print('state = ' + state_output + ' #')

lang = input("lang")
for state_output_yml in state_ids_array_output:
    print('STATE_' + state_output_yml + '_' + lang + ':0 ""')