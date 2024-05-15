class Singleton:
    _instance = None

    # Приватный конструктор
    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("Этот класс является синглтоном! Используйте метод getInstance() для получения экземпляра.")
        else:
            Singleton._instance = self

    # Статический метод для получения экземпляра Singleton
    @staticmethod
    def getInstance():
        if Singleton._instance is None:
            Singleton()
        return Singleton._instance

    # Метод, который можно вызвать на экземпляре Singleton
    def showMessage(self):
        print("Привет, я Singleton!")


# Пример использования Singleton
if __name__ == "__main__":
    # Получение экземпляра Singleton
    singleton1 = Singleton.getInstance()
    singleton1.showMessage()

    # Попытка создать еще один экземпляр, который не должен быть создан
    try:
        singleton2 = Singleton()  # Эта строка должна вызвать исключение
    except Exception as e:
        print(e)

    # Проверка, что оба указателя указывают на один и тот же экземпляр Singleton
    if singleton1 is Singleton.getInstance():
        print("Оба указателя указывают на один и тот же экземпляр Singleton.")
    else:
        print("Ошибка! Был создан лишний экземпляр Singleton.")
