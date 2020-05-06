# BEFORE YOU DO ANYTHING, PLEASE DO FF
# CLICK THE 'FORK' BUTTON ABOVE

# READ`Instructions` file. You can access it by clicking on the 'Files' icon on the left side/column of the screen (i.e. the top most icon, above Packages and Settings) and then clicking on the 'Instructions' file to show the contents

# This is the main.py script. It's the only script that you can run on this REPL platform via the run button above. This script takes care of displaying the output of stock price feed script you need to change in the `jpm_module_1` folder. 

# YOU SHOULD NOT CHANGE ANYTHING HERE AS IT ONLY RUNS THE STOCK PRICE FEED SCRIPT AND SHOWS THE OUTPUT

# IF YOU WISH TO DO THE BONUS TASK DESCRIBED IN THE INSRUCTIONS FILE, UNCOMMENT THE CODE BELOW

import os
import subprocess
import time
import signal

os.chdir(os.getcwd()+'/jpm_module_1')

process = subprocess.Popen(['python', 'server3.py'], cwd=os.getcwd(), preexec_fn=os.setsid)

time.sleep(.300)

process2 = subprocess.Popen(['python', 'client3.py'], cwd=os.getcwd(), preexec_fn=os.setsid)
process2.wait()
os.killpg(os.getpgid(process.pid), signal.SIGTERM)

# FOR BONUS TASK 
# IF YOU WANT TO DO IT THEN UNCOMMENT THE CODE BELOW
# Comments are anything that's preceded with '#'
# TO UNCOMMENT JUST REMOVE THE '#'

print("UNIT TEST RESULTS BELOW...")
process2 = subprocess.Popen(['python', 'client_test.py'], cwd=os.getcwd(), preexec_fn=os.setsid)
process2.wait()