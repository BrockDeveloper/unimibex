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
#


import urllib.request
import json
import pyperclip
import webbrowser
from datetime import datetime, time

# link to the json blob: shared lesson links
SHARED_DATA = "xxxx"

# private key to retrive and decrypt a lesson link
KEY = b'xxxx'


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
        if lesson.get("day")==current_datetime.get("dotw"):
            if current_datetime.get("time")>=lesson.get("begin_at") and current_datetime.get("time")<=lesson.get("end_at"):
                # open the chrome tab on the webex link
                webbrowser.open(lesson.get("link"))

                # if there is a password, it will be copied to clipboard
                if "pass" in lesson:
                    pyperclip.copy(lesson.get("pass"))
