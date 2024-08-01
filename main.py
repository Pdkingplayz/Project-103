import os
import shutil
import sys

import random
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/david/Downloads"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey! {event.src_path} has been created!")
    
    def on_modified(self, event):
        print(f"Hey! {event.src_path} has been edited!")
    
    def on_moved(self, event):
        print(f"Hey! {event.src_path} has been moved!")
    
    def on_deleted(self, event):
        print(f"Hey! {event.src_path} has been deleted!")

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive= True)
observer.start()

try:
    while True:
        print("Running.......")
        time.sleep(2)
except KeyboardInterrupt:
    print("Stopped.....")
    observer.stop()
