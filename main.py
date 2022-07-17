import PySimpleGUI as sg
sg.theme('LightBlue2')
layout = [
    [sg.Text('Welcome to the task list maker!')],
    [sg.Text('Please enter the task name and due date.')],
    [sg.Text('Task Name', size=(15, 1)), sg.InputText(key='TaskName')],
    [sg.Text('Due Date', size=(15, 1)), sg.InputText(key='DueDate')],

    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Test', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break


    def readfile(file):  # function to read file #
        f = open(file, "r")
        filecontent = f.readlines()
        f.close()
        print(filecontent)


    class Tasks:
        def __init__(self, taskname, duedate):  # task class
            self.taskname = taskname
            self.duedate = duedate
            self.tasks=[]

        def writeonfile(self):  # write file based on input
            f = open("C:\\Users\\xande\\Documents\\Rainmeter\\Skins\\Enigma\\@Resources\\User\\Notes\\Notes.txt", "a")
            f.write(str(self))
            f.close()

    def __str__(self):  # formats the writing of file
        return self.taskname + " " + self.duedate + "\n"

    Task1 = Tasks(values['TaskName'], values['DueDate'])
    Tasks.writeonfile(Task1)
    readfile("C:\\Users\\xande\\Documents\\Rainmeter\\Skins\\Enigma\\@Resources\\User\\Notes\\Notes.txt")

