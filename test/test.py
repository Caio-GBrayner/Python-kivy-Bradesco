from repositories import FileUserRepository
from services import UserService

if __name__ == "__main__":

    user_repository = FileUserRepository("users.txt")
    user_service = UserService(user_repository)


    user_service.create_user("test@example.com", "password123", "Test User", "2023/12/10")


    print(user_service.login("test@example.com", "password123"))
    print(user_service.login("test@example.com", "wrongpassword"))


    user_info = user_service.get_user_info("test@example.com")
    print(user_info.name, user_info.email, user_info.created)