from memo___card_layout import card, menu_btn, setQuestionstoCard, generateQuestion, give_rest_time, rest_btn
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QTimer
from memo___app import app
from memo__start_window import menu, start_btn, setQuestionstoMain
from memo__classes import QuestionsProvider, Question

card_width, card_height = 600, 500
timer = None

questions = QuestionsProvider()
questions.addQuestion(Question("Якого кольору ялинка", "Green", "Blue", "Yellow", "Black"))
questions.addQuestion(Question("В якому році відбулася перша згадка про Україну", "1187", "1256", "1769", "1903"))
questions.addQuestion(Question("Скільки буде 100*25", "2500", "250", "500", "750"))
questions.addQuestion(Question("В якої країни найбільше населення", "Китай", "Індія", "Японія", "США"))

menu_win = QWidget()
card_win = QWidget()

#Вікно меню
menu_win.setWindowTitle('Memory Card')
new_menu = menu()
menu_win.setLayout(new_menu)
menu_win.resize(card_width, card_height)
setQuestionstoMain(questions)

#Вікно карти
card_win.setWindowTitle('Memory Card')
new_card = card()
card_win.setLayout(new_card)
card_win.resize(card_width, card_height)
setQuestionstoCard(questions)

#Події
def show_menu():
    menu_win.show()
    card_win.hide()
    questions.reset_answers()
    
def show_card():
    generateQuestion()
    menu_win.hide()
    card_win.show()

def rest_card():
    card_win.hide()
    
def stop_rest_card():
    card_win.show()
    
def rest() :
    global timer
    
    rest_card()
    timer = QTimer()
    timer.setSingleShot(True)
    timer.timeout.connect(stop_rest_card)
    timer.start(give_rest_time()) 

menu_btn.clicked.connect(show_menu)
start_btn.clicked.connect(show_card)
rest_btn.clicked.connect(rest)

show_menu()
app.exec_()