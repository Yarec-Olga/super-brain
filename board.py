class Board():

    def __init__(self, start_question):
        self.start_question = start_question
        self.mistakes = 0
        self.used_questions = set()
        self.player_name = None

    def opening_question(self):
        return self.start_question

    def check_answer(self, result, question_name):
        self.used_questions.add(question_name)

        if result is False:
            self.mistakes += 1

            if self.mistakes >= 3:
                return "game_over"
        return "continue"

    def next_question(self, question_name):

        if question_name in self.used_questions:
            return "used"
        return "ok"