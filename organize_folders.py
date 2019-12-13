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

NOTE: Create the folders contained in the FOLDERS list
"""

#Add more extension as you need them
EXT_PDF = ['.pdf', '.epub', '.mobi']
EXT_VIDEO = ['.mp4', '.mkv', '.wav', '.m4a', '.mov', '.avi', '.flv']
EXT_MUSIC = ['.mp3']
EXT_IMAGE = ['.jpeg', '.jpg', '.png', '.svg', '.bmp']
EXT_DOCUMENT = ['.txt', '.doc','.docx','.html','.odt', '.xlsx']
EXT_ZIP = ['.rar', '.zip', '.gz']
EXT_EXE = ['.exe', '.msi']

EXTS = [EXT_PDF, EXT_VIDEO, EXT_MUSIC, EXT_IMAGE, EXT_DOCUMENT, EXT_ZIP, EXT_EXE]
FOLDERS = ['PDFs', 'VIDEOS', 'MUSIC', 'IMAGES', 'DOCUMENTS', 'ZIPs', 'EXEs']

#Modify this to the folder you want to track
path = "C:\\Users\\simon\\Downloads\\"
folder_to_track = os.path.abspath(path)

time_to_sleep = 10

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
