# Super Brain 🧠

A console quiz game written in Python. My second game, built for exercise 45
("You Make a Game") of Zed Shaw's book "Learn Python the Hard Way".

## How to play

Enter your name, then pick questions from the list one by one: math, logic,
history, English and a few "yes or no" questions.

Answer all of them to win. You can make only 2 mistakes — the third one ends
the game.

## Features

- 8 questions on different topics
- you choose the order of the questions
- every question can be answered only once
- 3 mistakes — game over
- a victory screen with your mistake count

## How it's built

The game is written with classes:

- `Question` — the base class for every question (`question.py`)
- question classes and the question map (`questions.py`)
- `Board` — keeps the player's name, mistakes and used questions (`board.py`)
- `Engine` — runs the game loop (`engine.py`)

## How to run

You need [Python 3](https://www.python.org/downloads/) installed.

```bash
python main.py
```

The questions and answers are in Russian.

## Tests

```bash
pip install pytest
python -m pytest
```

---

## На русском

Консольная игра-викторина на Python. Моя вторая игра, написанная по
упражнению 45 («Ты делаешь игру») из книги Зеда Шоу «Learn Python the Hard Way».

### Как играть

Введи своё имя и выбирай вопросы из списка по одному: математика, логика,
история, английский и вопросы «да или нет».

Чтобы выиграть, нужно ответить на все. Ошибиться можно только 2 раза —
на третий раз игра окончена.

### Что есть в игре

- 8 вопросов на разные темы
- порядок вопросов выбираешь сам
- на каждый вопрос можно ответить только один раз
- 3 ошибки — проигрыш
- экран победы с количеством ошибок

### Как устроена

Игра написана на классах:

- `Question` — базовый класс для всех вопросов (`question.py`)
- классы вопросов и карта вопросов (`questions.py`)
- `Board` — хранит имя игрока, ошибки и пройденные вопросы (`board.py`)
- `Engine` — запускает игровой цикл (`engine.py`)

### Как запустить

Нужен установленный [Python 3](https://www.python.org/downloads/).

```bash
python main.py
```

### Тесты

```bash
pip install pytest
python -m pytest
```
