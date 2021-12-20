class DataBases:
    users = "users.txt"
    quiz = "quizzes.txt"
    questions = "questions.txt"
    quiz_results = "quiz_results.txt"
    reasons = "reasons.txt"


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
    write_reason = 3


class Substates:
    default = 0


class RandomStates:
    default = 0


shutdown = None


class QuizTypes:
    easy = 0
    medium = 1
    hard = 2


