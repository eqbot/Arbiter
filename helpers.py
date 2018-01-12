import subprocess

def systemRun(command):
    output = subprocess.run(command, stdout=subprocess.PIPE)
    return output.stdout
    