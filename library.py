from DataManager import JsonManager
from member import SpecialCredit, NormalCredit
from user import User

jsLib = JsonManager()

class Library:
    def __init__(self, name):
        self.__name = name
    
    def __repr__(self):
        data = jsLib.pullData()
        return "Library {}; with {} members and {} books".format(
            self.__name, 
            len(data["Users"]), 
            len(data["Books"])
        )

    def register(self, Id:str, name:str, password:str, creditType:str):
        if len(Id) < 1:
            print("InputError: Id is wrong!")
            return -1
      
        elif Id in jsLib.pullData()["Users"]:
            print("InputError: This id has already used!")
            return -1
    
        elif len(name) < 1:
            print("InputError: Name is wrong!")
            return -1
        
        elif len(password) < 5:
            print("InputError: Your password shoud be have at least five characters!")
            return -1
        
        elif creditType not in ["Special", "Normal"]:
            raise ValueError("Credit type must be Special or Normal.")
        
        jsForm = {
            Id:{
                "Name":name, 
                "Password":password, 
                "RentedBooks":{}, 
                "CreditType":creditType, 
                "BlockedStatus":[], 
                "History":[]
                }
            }  
        jsLib.appendDataToCategory("Users", jsForm)
        
        print("Register successfully(^,^)")
        print("+Please Login to your account.")

    def login(self, Id:str, password:str):
        users = jsLib.pullData()["Users"]
        if Id not in users:
            print("InputError: Your id is wrong!")
            return -1
        
        elif users[Id]["Password"] != password:
            print("InputError: Password is wrong!")
            return -1
        
        print("Login successfully(^,^)")
        if users[Id]["CreditType"] == "Special":
            return SpecialCredit(Id, users[Id]["Name"], password)
        else:
            return NormalCredit(Id, users[Id]["Name"], password)