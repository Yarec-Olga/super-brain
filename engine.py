from sys import exit

from board import Board
from questions import create_question_map
from questions import GameOver
from questions import Win


class Engine():

    def __init__(self, board):
        self.board = board
        self.question_map = create_question_map()
        self.game_over_scene = GameOver()
        self.win_scene = Win()


    def play(self):
        question_name = self.board.opening_question()
        while True:
            scene = self.question_map[question_name]
            result = scene.enter(self.board)
            status = self.board.check_answer(result, question_name)
            if status == "game_over":
                self.game_over_scene.enter(self.board)
                return
            question_map = set(self.question_map.keys())
            second_question_map = question_map.difference(self.board.used_questions)
            if not second_question_map:
                self.win_scene.enter(self.board)
                return
            print("\nДоступные вопросы")
            for name in second_question_map:
                print(f" - {name}")
            while True:
                question_name = input("Выберите следующий вопрос:")
                if question_name not in self.question_map:
                    print("Такого вопроса нет. Попробуйте снова.")
                elif question_name in self.board.used_questions:
                    print("Этот вопрос уже был. Выберите снова")
                else:
                    break
