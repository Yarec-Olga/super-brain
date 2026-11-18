from sys import exit
from question import Question
import question

class GameOver(Question):

    def enter(self,board):
        print(f"Упс, {board.player_name}, ты третий раз ответил неправильно."
              f"\n Игра окончена!")

class Win(Question):

    def enter(self, board):
        print(f"\nПоздравляю, {board.player_name}! Ты ответил на все вопросы!🏆"
              f"\nОшибок: {board.mistakes}. Ты настоящий Super Brain! 🧠")

class Start(Question):

    def enter(self,board):
        board.player_name = input("Добро пожаловать в Super Brain! 🧠"
                                  "\nКак вас зовут? ")
        print(f"Привет, {board.player_name}! Перед тобой появится список вопросов."
              f"\nДля того что бы выйграть, тебе нужно ответить на все. "
              f"\nТы можешь ошибиться только 2 раза, на третий раз ты проиграешь.Удачи!🙌")


class Mathematics_1(Question):

    def enter(self, board):
        answer = int(input(f"В группе 4 музыканта. Каждый играет на 2 инструментах."
                       f"\nСколько инструментов всего?"
                       f"\n{board.player_name}, какой твой ответ?:"))
        if answer == 8:
            print("Верно!!!👌")
            return True
        else:
            print(f"К сожалению ты ошибся. Это неверный ответ!😒")
            return False

class English_1(Question):

    def enter(self, board):
        answer = input(f"Ок {board.player_name}! Проверим твой английский! "
                       f"\nКак переводится слово \"fashion\" на русский? Твой ответ: ")
        if answer.lower() == "мода":
            print(f"Да ты молодец! Правильный ответ! 😎")
            return True
        else:
            print("Это не верный ответ. Стоит поучить английский!🤦‍♀️")
            return False

class Logic_1(Question):

    def enter(self,board):
        answer = input(f"Что всегда идёт, но никуда не проходит? "
                       f"\n{board.player_name}, какой твой ответ?: ")
        if answer.lower() == "время":
            print("Верно!👌")
            return True
        else:
            print("Неверно!🤦‍♀️")
            return False

class History_1(Question):

    def enter(self,board):
        answer = int(input("В каком году человек впервые полетел в космос? Ваш ответ: "))
        if answer == 1961:
            print("Верно! ⚡")
            return True
        else:
            print("Неверно! 🤦‍♂️")
            return False



class Yes_No_1(Question):

    def enter(self, board):
        answer = input(f"Фэйд — это техника стрижки? "
                        f"{board.player_name}, какой твой ответ?: ")
        if answer.lower() == "да":
            print("На этот вопрос не могут ответить даже некоторые 'мастера🤣'"
                  "\nА твой ответ - ПРАВИЛЬНО!👌")
            return True
        else:
            print("Неверно!🤦‍♀️Тут и некоторым горе 'мастерам' разобраться сложно, "
                  "\nне расстраивайся")
            return False

class Logic_2(Question):

    def enter(self,board):
        answer = int(input("Если в комнате 4 угла, и в каждом углу сидит кошка, а напротив "
                           "\nкаждой кошки сидят 3 кошки — сколько кошек в комнате? Ваш ответ: "))
        if answer == 4:
            print("Верно!😁")
            return True
        else:
            print("Неверно! 😒")
            return False



class Yes_No_2(Question):

    def enter(self, board):
        answer = input(f"Gucci — итальянский бренд? "
                       f"Какой твой ответ?: ")
        if answer.lower() == "да":
            print("Это сложный вопрос, для тех кто не в теме) Но ты справился!"
                  "\nТвой ответ верный!😎")
            return True
        else:
            print("Не расстраивайся, но ты не в теме моды😐 Твой ответ неверный!")
            return False



class English_2(Question):

    def enter(self, board):
        answer = input(f"Ок {board.player_name}! Как переводится слово \"monochrome\" на русский? "
                       f"\nТвой ответ: ")
        if answer.lower() == "одноцветный":
            print(f"Да ты молодец! Правильный ответ! 😎")
            return True
        else:
            print("Это не верный ответ!🤦‍♀️")
            return False


def create_question_map():
    return {
        "start": Start(),
        "mathematics_1": Mathematics_1(),
        "logic_1": Logic_1(),
        "history": History_1(),
        "english_1": English_1(),
        "yes_no_1": Yes_No_1(),
        "logic_2": Logic_2(),
        "yes_no_2": Yes_No_2(),
        "english_2": English_2()
}