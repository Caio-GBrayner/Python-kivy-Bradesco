class User:
    def __init__(self, name: str, email: str, password: int):
        self.__name = name
        self.__email = email
        self.__password = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    def __str__(self):
        return f"Name:{self.__name} - E-mail: {self.__email} Password "