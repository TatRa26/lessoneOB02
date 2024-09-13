class User:
    def __init__(self, user_id: int, name: str):
        """Инициализация пользователя с приватными атрибутами"""
        self.__id = user_id
        self.__name = name
        self.__access_level = 'user'  # Уровень доступа для обычных пользователей

    # Геттеры (методы для получения значения атрибутов)
    def get_id(self) -> int:
        """Возвращает ID пользователя"""
        return self.__id

    def get_name(self) -> str:
        """Возвращает имя пользователя"""
        return self.__name

    def get_access_level(self) -> str:
        """Возвращает уровень доступа пользователя"""
        return self.__access_level

    # Сеттер (метод для изменения имени пользователя)
    def set_name(self, name: str) -> None:
        """Устанавливает новое имя пользователя"""
        self.__name = name


class Admin(User):
    def __init__(self, user_id: int, name: str):
        """Инициализация администратора с приватными атрибутами"""
        super().__init__(user_id, name)
        self.__access_level = 'admin'  # Приватный атрибут уровня доступа для администратора
        self.__users_list = []  # Приватный список пользователей

    # Переопределяем метод get_access_level для администратора
    def get_access_level(self) -> str:
        """Возвращает уровень доступа администратора"""
        return self.__access_level

    def add_user(self, user: User) -> None:
        """Добавляет пользователя в список"""
        self.__users_list.append(user)

    def remove_user(self, user_id: int) -> None:
        """Удаляет пользователя по ID"""
        self.__users_list = [user for user in self.__users_list if user.get_id() != user_id]

    def get_users_list(self) -> list:
        """Возвращает список пользователей"""
        return self.__users_list

    def display_users(self) -> None:
        """Выводит список пользователей с их информацией"""
        for user in self.__users_list:
            print(f"ID: {user.get_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")


# Пример использования

# Создание пользователей
user1 = User(1, "Алиса")
user2 = User(2, "Женя")

# Создание администратора
admin = Admin(0, "Антон")

# Администратор добавляет пользователей
admin.add_user(user1)
admin.add_user(user2)

# Показать список пользователей
admin.display_users()

# Администратор удаляет пользователя
admin.remove_user(1)

# Показать обновленный список пользователей
admin.display_users()