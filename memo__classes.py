from random import choice

class Question() :
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3) :
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        
class QuestionsProvider() :
    def __init__(self):
        self.questions = []
        self.attempts = 0
        self.right_answers = 0

    def increase_answers(self):
        self.right_answers +=1
        self.attempts += 1

    def reset_answers(self):
        self.right_answers = 0
        self.attempts = 0
    
    def increase_attempts(self):
        self.attempts += 1

    def addQuestion(self, question) :
        self.questions.append(question)
    
    def giveRandomQuestion(self) :
        return choice(self.questions)
    
    def giveAllQuestions(self) :
        return self.questions
    
    def isCorrect(self, question, answer) :
        return (question.right_answer == answer)
    