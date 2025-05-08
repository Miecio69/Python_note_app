Simple python object oriented note app using command line interface. Lets the sure add new notes, delete them and list all. 
Adds the notes by addign a new folder on the desktop 'MyNotesApp' and then folders the files by their priority.

Usage example:
- To add new note simple type in programs folder:
  </ python main.py add "Shopping list" "Buy milk and egs for tomorow" --priority 1 --tags shop, breakfast />
- To delete a note simply type:
  </ python main.py delete "Shopping list" />
- To list all notes type:
  </ python main.py list />
  ![obraz](https://github.com/user-attachments/assets/18aebcf6-9b9c-4247-b018-a0ffb119dd09)


To get help type -h or </ command /> -h for better info about single command

***Class description***
- note.py simply is a object class holding all notes parameters
- noteMethods.py holds all methods to add new notes, delete them and list all
- main.py is where all the argparser methods exist making a interface for a user 
  - also sets the location of where all notes are stored
- helpClass self-made class to remake on my own the argparser module

***Plans for futere***
- Search by tags
- Add .exe file to make it standalone program
- Finish helpClass 

