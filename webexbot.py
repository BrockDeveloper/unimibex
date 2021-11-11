# Brock DEV and LoryPota
# See LICENSE file.
#
# Developed by
# Brock DEV (https://github.com/BrockDeveloper).
# WebSite: https://brockdev.it
#
# This source code is distributed under the CC BY-NC-SA 4.0 license:
# https://creativecommons.org/licenses/by-nc-sa/4.0/
# you are FREE to SHARE and ADAPT UNDER THE FOLLOWING TERMS:
# 
# ATTRIBUTION You must give appropriate credit, provide a link to the
# license, and indicate if changes were made.
#
# NON COMMERCIAL You may not use the material for commercial purposes.
#
# SHARE ALIKE If you remix, transform, or build upon the material, you
# must distribute your contributions under the same license as the original.
#
#
# This source code is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY.


import urllib.request
import json
import pyperclip
import webbrowser
from datetime import datetime
from cryptography.fernet import Fernet


SHARED_DATA = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"     # link to the json blob: shared lesson links
KEY = b'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'                    # private key to retrive and decrypt a lesson link
CODER = Fernet(KEY)                                                      # crittografia con la chiave definita


# return the currente date and time of the system
def retrieve_datetime():

    now = datetime.now()

    current_datetime = {
        "time":now.strftime("%H:%M"),
        "dotw":now.date().weekday()
    }

    return current_datetime


if __name__ == "__main__":

    # retrive the json blob from the server and decode it
    with urllib.request.urlopen(SHARED_DATA) as url:
        lessons = json.loads(url.read().decode())

    # retrive current date and time from the system
    current_datetime = retrieve_datetime()

    # check if there is a lesson
    for lesson in lessons:

        #check if the lesson is today (in the current date is day of the week)
        if lesson.get("day")==current_datetime.get("dotw"):

            #check if the time is now (in the current date is time)
            if current_datetime.get("time")>=lesson.get("begin_at") and current_datetime.get("time")<=lesson.get("end_at"):

                # open the chrome tab (or the default web browser software) on the webex link
                webbrowser.open(CODER.decrypt(lesson.get("link").encode()).decode())

                # if there is a password, it will be copied to clipboard
                if "pass" in lesson:
                    pyperclip.copy(CODER.decrypt(lesson.get("pass").encode()).decode())
