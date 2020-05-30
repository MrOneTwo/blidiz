import sys
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from pathlib import Path
from enum import Enum
import socket

if len(sys.argv)< 2:
    print("Please call this script with a path to watch as the first argument.")
    quit()

EXPORT_PATH = Path(sys.argv[1])
HOST = 'localhost'
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(20)

artifacts = []
connection_established = False

class ArtifactState(Enum):
    NEW = 1
    MODIFIED = 2

class Artifact():
    def __init__(self, name: str, state: ArtifactState = ArtifactState.NEW):
        self.name = name
        self.state = state

def f_created(event):
    print(f"Created... {event.src_path}")

def f_deleted(event):
    print(f"Deleted... {event.src_path}")
    f_name = Path(event.src_path).name
    if 'obj' in event.src_path.lower():
        # Check if object is already in the list.
        for a in artifacts:
            if a.name == f_name:
                artifacts.remove(a)
                break

def f_modified(event):
    print(f"Modified... {event.src_path}")
    f_name = Path(event.src_path).name
    if 'obj' in event.src_path.lower():
        # Check if object is already in the list.
        known_files = [f.name for f in artifacts]
        if f_name in known_files:
            pass
        else:
            artifacts.append(Artifact(f_name, ArtifactState.MODIFIED))
            if connection_established:
                sock.send(bytes(event.src_path, 'ascii'))
                data = sock.recv(4)
                print(data)

def f_moved(event):
    print(f"Moved... {event.src_path}")


if __name__ == "__main__":
    observer = Observer()
    event_handler = PatternMatchingEventHandler(patterns=("*.obj", "*.OBJ"), ignore_directories=True, case_sensitive=True)
    observer.schedule(event_handler, str(EXPORT_PATH), recursive=False)
    observer.start()

    event_handler.on_created = f_created
    event_handler.on_deleted = f_deleted
    event_handler.on_modified = f_modified
    event_handler.on_moved = f_moved

    try:
        sock.connect((HOST, PORT))
        connection_established = True
    except socket.timeout:
        print("Trying to connect to server timed out...")
    except ConnectionRefusedError:
        print("Connection refused...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

