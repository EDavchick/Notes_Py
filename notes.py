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
functions = ["open", "add", "read", "save", "change", "del", "exit"]
# print("Hello to the notes!")

# always open empty file after reloaded, bad idea
# with open(fn, 'w+') as file:
#     json.dump(notes, file)
    
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
        notes[input('Put number or name your note: ')] = input("Put the body your note for added: ")
        file.seek(0, 0)
        json.dump(notes, file, indent=2, ensure_ascii=False)
        print("Your notes was added and saved")    
    

    # try:
    #     with open(fn, "r+", encoding="utf-8") as file:
    #         notes = json.load(file)
    #         notes[input('Put name your note: ')] = input("Put the body your note for added: ")
    #         file.seek(0, 0)
    #         json.dump(notes, file, indent=2, ensure_ascii=False)
    #         print("Your notes was added and saved")    
    # except:
    #     notes = {}    

def writeNote(note):
    try:
        date = json.load(open(fn))
    except:
        data = {}
    
    data.update(note)

    with open(fn, 'w') as file:
        json.dump(date, file, indent=2, ensure_ascii=False)

# read all notes
def readNotes():
    try:
        notes = json.load(open(fn))
        with open(fn) as jsonFile:
            notes = json.load(jsonFile)

            for key, value in notes.items():
                print(f"Note #{key}: Record: {value} \n")
    except:
        notes = {}
        print("You do not have any note, please enter add in terminal")

    with open(fn, 'w') as file:
        json.dump(notes, file, indent=2, ensure_ascii=False)

    # try:
    #     notes = json.load(open(fn))
    # except:
    #     notes = {}  
    #     print("You do not have any note, please enter add in terminal")
    
    # with open(fn) as jsonFile:
    #     notes = json.load(jsonFile)

    #     for key, value in notes.items():
    #         print(f"Note #{key}: Record: {value} \n")

def putCommand():
    while True:
        command = input(f"Put a command: '{functions}': ")
        # with open(fn, 'w+') as file:
        #     json.dump(notes, file)
        if command == "open":
            print('OPEN command')
            print("Your notes were opened")
            openNotes()
        elif command == "exit":
            print('EXIT command')
            # save()
            print("Goodbye!")
            break
        elif command == "add":
                print('ADD command')
                addNote()
        elif command == "read":
            print('READ command')
            readNotes()    
        elif command == "save":
                print('SAVE command')
        elif command == "change":
                print('CHANGE command')
        elif command == "del": 
                print('DEL command')
        else:
            print('ERROR command')
            print(f"Unidentified command, please put only command for using the notes")


def main():
    putCommand()

if __name__ == '__main__':
     main()