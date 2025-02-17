import datetime

class DataBase:
    def __init__(self, filename):
        self.__filename = filename
        self.__users = None
        self.__file = None
        self.__load()

    def load(self):
        self.__file = open(self.__filename, "r")
        self.__users = {}

        for line in self.__file:
            email, password, name, created = line.strip().split(";")
            self.__users[email] = (password, name, created)

        self.__file.close()

    def get_user(self, email):
        if email in self.__users:
            return self.__users[email]
        else:
            return -1

    def add_user(self, email, password, name):
        if email.strip() not in self.__users:
            self.__users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
            print("E-mail alredy exists")
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.__users[email][0] == password
        else:
            return False

    def save(self):
        with open(self.__filename, "w") as file:
            for user in self.__users:
                file.write(f"{user};{self.__users[user][0]};{self.__users[user][1]};{self.__users[user][2]}\n")

    @staticmethod
    def get_date():
        return datetime.datetime.now().strftime("%d/%m/%Y")