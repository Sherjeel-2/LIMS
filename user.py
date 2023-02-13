from DataManager import JsonManager
import datetime

jsLib = JsonManager()

class User:
    def __init__(self, Id, name, password, creditType):
        self._id = Id
        self._name = name
        self._passowrd = password
        self._creditType = creditType
    
    @property    
    def Id(self):
        return self._id
   
    @property
    def name(self):
        return self._name
    
    @property
    def password(self):
        return len(self._passowrd) * "*"
    
    @property
    def creditType(self):
        return self._creditType

    

    

