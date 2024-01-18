import sys
from pathlib import Path

from game import WhoWantsToBeAMillionaire
from question_service import QuestionService

#this is the main page you start the program from here..
if __name__ == "__main__":
    game = WhoWantsToBeAMillionaire(QuestionService(Path("demo_questions.txt")))
    sys.exit(game.start_game())
