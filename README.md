# FileOrganizerApp

This project was inspired by my incredibly messy computer. It is designed to easily sort all files from a given directory and then go into any directories under it and sort those recursively. I completed this project using the python libraries time, sys, os, watchdog, shutil, logging and threading. I hope you can find use in my work like I have!


## Features

- Sorts files by default types based on their extension. ".csv" files go into csv-files folder etc
- 7 Default file types are ".csv" ".txt" ".jpeg" ".png" ".pdf" ".py" ".java" and they go into the 6 folders "csv-files" "text-files" "image-files" "pdf-files" "python-files and "java-files" respectively 
- User is prompted to customize their sorting by giving an extension type ex. "lisp" and folder name ex. "lisp-files"
- Recursive sorting. This program goes into the given directory and sorts them based on the criteria above and continuosly sorts any sub directories
- Program runs continuosly until user types in "done". this makes it so that if any files are added or modified in the given directory they are also sorted


## Requirements
- Python 3.x
- watchdog
## Installation



```bash  
  pip3 install watchdog

```
    
## Screenshots
<img width="1440" alt="usage1" src="https://github.com/user-attachments/assets/3cb0e3d4-d982-4422-b6c5-e29bce98ab51">

<img width="1440" alt="Usage3" src="https://github.com/user-attachments/assets/d74e14ee-a898-40b3-84ed-f6182fa4e5d7">



