import os

def subproc(cmd):
    #string = subprocess.check_output(cmd, shell=True).decode("utf-8") # utf-8
    #string = subprocess.check_output(cmd, shell=True).strip()
    #output = subprocess.check_output(cmd)
    #os.system(cmd)
    f = os.popen(cmd)
    string = f.read()
    return string
 
# Lets get some details on the .wav file
seconds = subproc("sox tones.wav -n stat 2>&1 | sed -n 's#^Length (seconds):[^0-9]*\([0-9.]*\)$#\1#p'")
nsamples = subproc("sox tones.wav -n stat 2>&1 | sed -n 's#^Length (seconds):[^0-9]*\([0-9.]*\)$#\1#p'")
print("seconds:'{}' samples:'{}'".format(seconds, nsamples))

