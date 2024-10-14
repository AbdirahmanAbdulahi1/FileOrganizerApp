#Abdirahman Abdulahi's File organizer program
import os, shutil, sys
import time
import logging
import threading
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler




print("Fileorganizer.py organize files based on it's extension .txt .pdf .png etc")
time.sleep(2)

print("you can also add files you want sorted and")
time.sleep(2)

print("example \n folder: lisp-files \n extension: .lisp")

time.sleep(2)
print("type done to end program")
time.sleep(2)

folder_names = { ".csv" : "csv-files",
                ".txt" : "text-files",
                ".jpeg" : "image-files",
                ".png" : "image-files",
                ".pdf" : "pdf-files",
                ".java": "java-files",
                ".py": "python-files",     
}
time.sleep(2)
print("default folders: ")

for key in folder_names.keys():
    print(folder_names.get(key) + '(' + key + ')')

time.sleep(2)

#read in 
print("type done to skip")
while True:
    folder = input("folder: ")
    if folder == "done":
        break
    extension = input("extension: ")
    if extension == "done":
        break
    time.sleep(2)
    print("type 'done' if you have no more folders and files")
    folder_names[extension] = folder


# Get the directory that should be organized from user
path = input("Give an absolute path name ")
# if it doesnt exist tell user and end
if not os.path.exists(path):
    print("path does not exist")
    sys.exit()




#folder_names = ["csv-files", "text-files", "image-files", "python-files", "java-files" ,"pdf-files"]
#main organize function
def organize(path):
    #create list of folder types files can be sorted into
     
    
    #loop over folders check if folder exist in given directory if not make it
    for key in folder_names.keys():
        if not os.path.exists(path + "/" + folder_names[key]):
            os.makedirs(path + "/" + folder_names[key])
        
            
    #loop over each entry in the given directory and sort it into files
    #if entry is a directory call the organize function on it to sort it as well
    for entry in os.listdir(path):
        
        #if entry is a file check if it belongs in one of our folders
        # if so, move it to that folder
        if os.path.isfile(path + "/" + entry):
            for key in folder_names.keys():
                if entry.endswith(key) and not os.path.exists(path + "/" + folder_names.get(key) + "/" + entry):
                    shutil.move(path + "/" + entry, path + "/" + folder_names.get(key) + "/" + entry )
            

        #if entry is a directory then sort that directrory
        elif os.path.isdir(path + "/" + entry) and entry not in folder_names.values():
            organize(path + "/" + entry)
        
#custom handler inherits firm loggingeventhandler
class Myhandler(LoggingEventHandler):
    # calls organize when a file is created
    def on_created(self,event):
        super().on_created(event)
        if not event.is_directory:
            organize(path)
    #calls organize when a file is modified
    def on_modified(self, event):
        super().on_modified(event)
        if not event.is_directory:
            organize(path)

# Function to listen for user input to stop the program
def listen_for_exit(observer):
    while True:
        user_input = input()
        if user_input.strip().lower() == "done":
            observer.stop()
            break


#main execution starts here
if __name__ == "__main__":
    # set up logging configuration
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    # Initial organization of files in the specified path
    organize(path)

    # Create an instance of the custom event handler
    event_handler = Myhandler()

    # Set up the observer to monitor the specified path for changes
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    # Start a thread to listen for the exit command
    exit_thread = threading.Thread(target=listen_for_exit, args=(observer,))
    exit_thread.start()


    try:
        # Keep the script running, checking for changes
        while observer.is_alive():

            # Sleep for a second between checks
            time.sleep(1)

            # Stop the observer if a keyboard interrupt is received
    except KeyboardInterrupt:
        observer.stop()

    observer.join() # Wait for the observer to finish


    











