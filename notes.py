"""
Реализовать консольное приложение заметки, с сохранением, чтением, 
добавлением, редактированием и удалением заметок. 
Заметка должна содержать идентификатор, заголовок, тело заметки 
и дату/время создания или последнего изменения заметки. 
Сохранение заметок необходимо сделать в формате json или csv формат
(разделение полей рекомендуется делать через точку с запятой). 
Реализацию пользовательского интерфейса студент может делать как ему
удобнее, можно делать как параметры запуска программы
(команда, данные), можно делать как запрос команды с консоли и 
последующим вводом данных, как-то ещё, на усмотрение студента.
"""

import json

notes = {}
fn = "notes.json"
functions = ["open", "add", "read", "find", "change", "del", "exit"]

# open notes automatically
def openNotes():
    try:
        date = json.load(open(fn))
    except:
        data = {}

# add note and save it in file
def addNote():
    try:
        notes = json.load(open(fn))
    except:
        notes = {}  

    with open(fn, "w", encoding="utf-8") as file:
        notes[input('Put the name your note: ')] = input("Enter the record your note: ")
        # if keys only numbers we can sort them
        # sorted(notes, key=lambda t: tuple(map(int,t.split(": "))))
        file.seek(0, 0)
        json.dump(notes, file, indent=2, ensure_ascii=False)
        print("Your notes was added and saved")

# read all notes
def readNotes():
    try:
        notes = json.load(open(fn))
        with open(fn) as jsonFile:
            notes = json.load(jsonFile)

            for key, value in notes.items():
                print(f"\n Note #{key}: Record: {value}")
    except:
        notes = {}
        print("You do not have any note, please enter add in terminal")

    with open(fn, 'w') as file:
        json.dump(notes, file, indent=2, ensure_ascii=False)

# find note
def find():
    notes = json.load(open(fn))
    with open(fn) as jsonFile:
        notes = json.load(jsonFile)

        yourKey = input('Put the name your note: ')
        for key, value in notes.items():    
            if key == yourKey:
                print(f"Record #{yourKey}: {value}")
                # value = notes.get(key)
        #     else:
        #         print(f"Note #{yourKey} not found, try again")
        #     #     break
        # return print(f"Record #{yourKey}: {value}") 
        
# change note if you need
def change():
    notes = json.load(open(fn))
    with open(fn) as jsonFile:
        notes = json.load(jsonFile)
        
        yourKey = input('Put the name your note: ')
        for key in notes.items():    
            if key == yourKey:
                notes[key] = input("Enter the record your note: ")
    with open(fn, 'w') as file:
        json.dump(notes, file, indent=2, ensure_ascii=False)
        print("Your note was changed")

# delite note on key
def delite():
    notes = json.load(open(fn))
    with open(fn) as jsonFile:
        notes = json.load(jsonFile)
        
        yourKey = input('Put the name your note: ')
        for key in list(notes):    
            if key == yourKey:
                del notes[key]
    with open(fn, 'w') as file:
        json.dump(notes, file, indent=2, ensure_ascii=False)
        print("Your note was delite")
        print(f"Your notes: {notes}")

def putCommand():
    while True:
        command = input(f"Put a command: '{functions}': ")
        if command == "open":
            print("Your notes were opened")
            openNotes()
        elif command == "exit":
            print("Goodbye!")
            break
        elif command == "add":
            addNote()
        elif command == "read":
            readNotes()    
        elif command == "find":
            find()
        elif command == "change":
            change()
        elif command == "del": 
            delite()
        else:
            print(f"Unidentified command, please put only command for using the notes")


def main():
    putCommand()

if __name__ == '__main__':
    main()