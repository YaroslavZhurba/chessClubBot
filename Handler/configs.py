class DataBases:
    users = "users.txt"
    quiz = "quiz.txt"
    questions = "questions.txt"
    quiz_results = "quiz_results.txt"

class Messages:
    admin_greeting = "Здоров, командир! Че делаем?"
    user_greeting = "Здравствуйте уважаемые дамы и господа!"
    why_no_attendance = "Че не ходим? + долг по физре"
    no_rights = "Кажется, что у вас недостаточно прав. Очень жаль.."
    bye_bye = "Я умир :("


class Permissions:
    admin = 1
    user = 0


class States:
    default = 0
    quiz = 1
    board_task = 2


class Substates:
    default = 0


class RandomStates:
    default = 0


shutdown = None


class QuizTypes:
    easy = 0
    medium = 1
    hard = 2


