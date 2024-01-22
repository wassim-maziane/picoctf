analysing the code, especially the check-key function, we notice that it compares character by character the input of the user. the code calculates the sha256 of b"FREEMAN" and compares them.
if we just concatenate the comparisons that the code does, we obtain the flag:
input = key_part_static1_trial + hashlib.sha256(bUsername_trial).hexdigest()[4] + hashlib.sha256(bUsername_trial).hexdigest()[5] + hashlib.sha256(bUsername_trial).hexdigest()[3] + hashlib.sha256(bUsername_trial).hexdigest()[6] + hashlib.sha256(bUsername_trial).hexdigest()[2] + hashlib.sha256(bUsername_trial).hexdigest()[7] + hashlib.sha256(bUsername_trial).hexdigest()[1] + hashlib.sha256(bUsername_trial).hexdigest()[8] + key_part_static2_trial 
executing the test.py file gives us the flag
