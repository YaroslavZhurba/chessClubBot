import questions_collection
import quiz_collection
import user_handler
import quiz_handler


def get_id(question):
    return question["id"]


def get_question(question):
    return question["question"]


def get_answers(question):
    return question["answers"]


def get_answer_for_message(question):
    answers = get_answers(question)
    string_answers = ""
    answers_amount = len(answers)
    for i in range(answers_amount):
        string_answers += str(i + 1) + ") " + answers[i] + "\n"
    return string_answers


def get_correct_answer(question):
    return question["correct_answer_no"]


def get_question_by_user(user):
    substate = user_handler.get_user_substate(user)
    cur_question_pos = quiz_handler.get_questions(quiz_collection.get_user_quiz(user))[substate]
    return questions_collection.get_question_by_position(cur_question_pos[0], cur_question_pos[1])
