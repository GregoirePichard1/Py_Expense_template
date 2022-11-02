from PyInquirer import prompt
from csv import writer
from user import *


expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },
    {
        "type":"input",
        "name":"involved",
        "message":"New Expense - Involved: ",
    },
]


def new_expense(*args):
    getListUser()
    infos = prompt(expense_questions)
    if not checkExistingUser(infos["spender"]):
        print("Please enter a valid spender")
        new_expense(*args)
    with open('expense_report.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        l = []
        l.append(infos["amount"])
        l.append(infos["label"])
        l.append(infos["spender"])
        l.append(infos["involved"])
        writer_object.writerow(l)
        f_object.close()
    print("Expense Added !")
    return True

def checkExistingUser(name):
    with open("users.csv") as fp:
        line = fp.readline()
        cnt = 1
        while line:
            if line.rstrip() == name:
                return True
            line = fp.readline()
            cnt += 1
        return False
    return False

def getListUser():
    with open("users.csv") as fp:
        line = fp.readline()
        cnt = 1
        l = []
        print("Users: ", end=' ')
        while line:
            print(line.rstrip() + ", ", end= ' ')
            line = fp.readline()
            cnt += 1
        print()