import pytest
from board import Board

def test_mistake():
    board = Board('start')
    assert board.mistakes == 0

def test_game_over():
    board = Board('start')
    board.check_answer(False, 'question_1')
    board.check_answer(False, 'question_2')
    status = board.check_answer(False, 'question_3')
    assert status == "game_over"

def test_used_question():
    board = Board('start')
    board.check_answer(True, 'mathematics_1')
    assert 'mathematics_1' in board.used_questions

def test_continue():
    board = Board('start')
    status = board.check_answer(True, 'question_1')
    assert status == "continue"