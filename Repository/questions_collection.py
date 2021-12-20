import configs
import rw

# local functions and variables
db = None


# read database if needed
def before_questions():
    global db
    if db is None:
        db = rw.read_database(configs.DataBases.questions)
        for complexity_questions in db:
            complexity_questions["amount"] = len(complexity_questions["questions"])


def get_amount_by_complexity(complexity):
    before_questions()
    return db[complexity]["amount"]


def get_questions_by_complexity(complexity):
    before_questions()
    return db[complexity]["questions"]


def get_question_by_position(complexity, id):
    questions = get_questions_by_complexity(complexity)
    return questions[id]
