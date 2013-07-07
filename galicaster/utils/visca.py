# executes 'visca-cli memory_recall [0-5]'
# we don't check if daemon is running or if client is installed

from subprocess import call

def recall(preset):
    call(['visca-cli', 'memory_recall', str(preset)])
