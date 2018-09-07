# @script    janCreateTodayFolder
# @version   1.0
# @author    Mitchell Lotierzo
# @email     mitchlotierzo@gmail.com


###############################################################
# GLOBAL
###############################################################
import os
import time


# Function ====================================================
def createTodayFolder():
    """Create a folder in the current working directory and name it after today's date."""

    if not (os.path.exists(".\\" + str(time.strftime("%Y-%m-%d")))):
    	os.makedirs(".\\" + str(time.strftime("%Y-%m-%d")))
    else: quit()


# Execute =====================================================
createTodayFolder()
