from PyInquirer import prompt
from csv import writer

user_questions = [

]

def add_user():
    name = input("Enter your name: ")
    if name != "" and name != "\n":
        with open('users.csv', 'a', newline='') as f_object:  
            writer_object = writer(f_object)
            l = []
            l.append(name)
            writer_object.writerow(l)
            f_object.close()
    return