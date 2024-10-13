from random import choice, shuffle
from PyQt6.QtWidgets import QApplication
app = QApplication([])

from main_window import *
from menu_window import *

class Question():
    def __init__(self, question_text, answer_text, wrong:tuple) -> None:
        self.question_text = question_text
        self.answer_text = answer_text
        self.wrong_answers = wrong

    def got_right(self):
        ...
    def got_wrong(self):
        ...


q1 = Question("Яблуко", "apple", ("application", "ape", "pineapple"))
q2 = Question("Фортнайт", "fortnite", ("fornite", "fronti", "firtneto"))
q3 = Question("Меч", "sword", ("sord", "swodr", "hoorse"))
q4 = Question("Асасин", "Assassins", ("ashansin", "adolfsin", "ananasin"))


questions_list = [q1,q2,q3,q4 ]
radio_button_list = [rb_answer_1, rb_answer_2, rb_answer_3, rb_answer_4]

def new_question():
    global random_question
    random_question = choice(questions_list)

    shuffle(radio_button_list)

    question_lb.setText(random_question.question_text)

    radio_button_list[0].setText(random_question.answer_text)

    for i in range(3):
         radio_button_list[i+1].setText(random_question.wrong_answers[i])

new_question()

def check_result():
    correct_answer_lb.setText(random_question.answer_text)
    radio_button_group.setExclusive(False)
    for btn in radio_button_list:
        if btn.isChecked():
            btn.setChecked(False)
            if btn.text () == random_question.answer_text:
                result_lb.setText("Правильно! Молодець")    
                break
       
    else:
        result_lb.setText("Неправильна відповідь!")
    radio_button_group.setExclusive(True)


def change_box():
    if btn_next.text() == "Відповісти":
        check_result()
        radio_button_box.hide()
        answer_box.show()
        btn_next.setText("Наступне питання")
    elif btn_next.text() == "Наступне питання":
        radio_button_box.show()
        answer_box.hide()
        btn_next.setText("Відповісти")
        new_question()



btn_next.clicked.connect(change_box)


def open_menu():
    window.hide()
    menu_window.show()
def close_menu():
    ...

menu_btn.clicked.connect(open_menu)


window.show()
app.exec()

