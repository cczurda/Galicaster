# call 'visca-cli memory_recall [0-5]'
# we don't check if daemon is running, we don't check if client is installed
#

import subprocess

#from galicaster.core import context

#logger = context.get_logger()

def recall(preset):
    #logger.info("recall visca camera preset %d", preset)
    subprocess.call("visca-cli", "memory_recall", preset) #????

