from datetime import datetime

class User:
    def __init__(self, name: str, email: str, password: str, created: str = None):
        self.__name = name
        self.__email = email
        self.__password = password
        self.__created = created if created is not None else self.get_current_date()

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

    @property
    def created(self):
        return self.__created

    @created.setter
    def created(self, created):
        self.__created = created

    def __str__(self):
        return f"Name: {self.__name}, Email: {self.__email}, Created: {self.__created}"

    @staticmethod
    def get_current_date():
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")