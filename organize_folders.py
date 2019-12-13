from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler

import os
import time
import json

"""
Inspired by this youtube video
LINK => https://www.youtube.com/watch?v=HcZ3gS1Rgcs

This script checks the folder_to_track is being modified (when something is being downloaded)
and automatically moves to the correct folder based on the file's extension.
Some exception might be triggered.

Example: A file is currently in use by a program.
"""

EXT_PDF = ['.pdf', '.epub']
EXT_VIDEO = ['.mp4', '.mkv', '.wav', '.m4a', '.mov', '.avi', '.flv']
EXT_IMAGE = ['.jpeg', '.jpg', '.png', '.svg', '.bmp']
EXT_DOCUMENT = ['.txt', '.doc','.docx','.html','.odt', '.xlsx']
EXT_ZIP = ['.rar', '.zip', '.gz']
EXT_EXE = ['.exe']

EXTS = [EXT_PDF, EXT_VIDEO, EXT_IMAGE, EXT_DOCUMENT, EXT_ZIP]
FOLDERS = ['PDF', 'VIDEO', 'IMAGE', 'DOCUMENT', 'ZIP']

path = "C:\\Users\\simon\\Downloads\\"
folder_to_track = os.path.abspath(path)
exceptions = []
time_to_sleep = 5

class myHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            for i in range(len(EXTS)):
                for ext in EXTS[i]:
                    if(filename.endswith(ext)):
                        src = os.path.join(folder_to_track, filename)
                        tmp_path = os.path.join(FOLDERS[i], filename)
                        destination_folder = os.path.join(folder_to_track, tmp_path)
                        try:
                            os.rename(src, destination_folder)
                        except(Exception) as e:
                            print(e)


event_handler = myHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=False)
observer.start()

try:
    while(True):
        time.sleep(time_to_sleep)
except(KeyboardInterrupt):
    observer.stop()

observer.join()
