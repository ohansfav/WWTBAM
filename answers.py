class Answers:
    def __init__(self, correct_answer: str, wrongs_answers: tuple([str, str, str])) -> None:
        self._correct_answer = correct_answer
        self._wrong_answers = wrongs_answers

    #function for correct answers ..
        def get_correct_answer(self) -> str:
        return self._correct_answer

    #function for wrong answers...
        def get_wrong_answers(self) -> tuple:
        return self._wrong_answers
