import random
import tkinter
import tkinter as tk

import mysql.connector

database = mysql.connector.connect(host="localhost", user="root", passwd="", database="besucher")

cursor = database.cursor()


def getRowOfUserTable(i):
    cursor.execute("select * from user")
    result = cursor.fetchall()

    print(result[i])


def getColumnOfUserTable(columnName):
    cursor.execute("select " + columnName + " from user")
    result = cursor.fetchall()

    return result


def deleteRowOfUserTable(i):
    cursor.execute("select * from user")
    result = cursor.fetchall()
    print("Deleted the row: " + str(result[i]))

    idOfRow = str(result[i][0])

    cursor.execute("delete from user where id='" + idOfRow + "'")

    database.commit()


def deleteAllRows():
    cursor.execute("delete from user")
    database.commit()


def insertNewRowIntoUserTable(username, password, repeatedPassword):
    if (password != repeatedPassword):
        print("The passwords are not the same!")
        return None

    if(checkIfUsernameExists(username)):
        print("This username already exists!")
        return None

    id = random.randint(0, 10000000)

    while (checkIfIdExists(id)):
        id = random.randint(0, 10000000)

    cursor.execute(
        "insert into user (id,username,password) VALUES ('" + str(id) + "','" + username + "','" + password + "')")
    database.commit()


def checkIfIdExists(id):
    idColumn = getColumnOfUserTable("id")

    for element in idColumn:
        for entry in element:
         if(entry==id):
            return True

    return False


def checkIfUsernameExists(username):
    usernameColumn = getColumnOfUserTable("username")

    for element in usernameColumn:
        for entry in element:
            if (entry == username):
                return True

    return False

def buildInsertNewRowGUI():
    mainWindow = tk.Tk()
    mainWindow.title("Insert a new row")
    mainWindow.resizable(False,False)
    mainWindow.geometry("400x300")
    mainWindow.eval('tk::PlaceWindow . center')

    label1 = tk.Label(mainWindow, text="Username:")
    label1.pack()

    textinput1 = tk.Entry(mainWindow,width="200")
    textinput1.pack()

    label2 = tk.Label(mainWindow, text="Password:")
    label2.pack()

    textinput2 = tk.Entry(mainWindow,width="200")
    textinput2.pack()

    label3 = tk.Label(mainWindow, text="Repeat password:")
    label3.pack()

    textinput3 = tk.Entry(mainWindow,width="200")
    textinput3.pack()

    newUserButton = tk.Button(mainWindow, text="Create new user",
                              command=lambda: insertNewRowIntoUserTable(textinput1.get(),textinput2.get(),textinput3.get()))
    newUserButton.pack()

    mainWindow.mainloop()



buildInsertNewRowGUI()





