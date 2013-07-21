# TSC! executes 'visca-cli memory_recall [0-5]'
# we don't check if camera is running or if client is installed. So make sure it is.

from subprocess import Popen

def recall(preset):
    Popen(['visca-cli', 'memory_recall', str(preset)])
