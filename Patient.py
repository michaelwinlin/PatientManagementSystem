
from abc import ABCMeta,abstractmethod
class Patient(metaclass=ABCMeta):
    def __init__(self,id,name,age,gender,citizen_status):
        self.__id=id
        self.__age=age
        self.__name=name
        self.__gender=gender
        self.__citizen_status=citizen_status
        self.__status='Registered'
        self.__stay_list=[]

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        self.__age = age

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self,gender):
        self.__gender = gender

    @property
    def citizen_status(self):
        return self.__citizen_status

    @citizen_status.setter
    def citizen_status(self,citizen_status):
        self.__citizen_status = citizen_status

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self,status):
        self.__status = status

    @property
    def stay_list(self):
        return self.__stay_list

    @abstractmethod
    def calculate_charges(self):
        pass

    def add_stay(self,Stay):
        self.__stay_list.append(Stay)

    def __repr__(self):
        return self.__class__.__name__ + "('{:s}','{:s}','{:d}','{:s}','{:s}','{:s}')".format(
            self.__id,self.__name,self.__age,self.__gender,self.__citizen_status,self.__status)

    



    
