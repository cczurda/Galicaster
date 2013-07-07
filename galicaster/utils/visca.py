# executes 'visca-cli memory_recall [0-5]'
# we don't check if daemon is running or if client is installed

from subprocess import Popen

def recall(preset):
    Popen(['visca-cli', 'memory_recall', str(preset)])
