from PyQt6.QtWidgets import (QWidget, QLabel,
                             QRadioButton, QPushButton,
                              QGroupBox, QButtonGroup,
                               QVBoxLayout, QHBoxLayout,
                               QLineEdit
                               )


menu_window = QWidget()


menu_v_line = QVBoxLayout()

menu_h_line_1 = QHBoxLayout()
menu_h_line_2 = QHBoxLayout()
menu_h_line_3 = QHBoxLayout()
menu_h_line_4 = QHBoxLayout()
menu_h_line_5 = QHBoxLayout()
menu_h_line_6 = QHBoxLayout()

menu_question_text_lb = QLabel("Введіть текст питання:")
menu_question_text_input = QLineEdit()

menu_h_line_1.addWidget(menu_question_text_lb)
menu_h_line_1.addWidget(menu_question_text_input)
menu_v_line.addLayout(menu_h_line_1)


menu_answer_text_lb = QLabel("Введіть текст відповіді:")
menu_answer_text_input = QLineEdit()

menu_h_line_2.addWidget(menu_answer_text_lb)
menu_h_line_2.addWidget(menu_answer_text_input)
menu_v_line.addLayout(menu_h_line_2)


menu_wrong1_text_lb = QLabel("Введіть текст неправильної відповіді:")
menu_wrong1_text_input = QLineEdit()

menu_h_line_3.addWidget(menu_answer_text_lb)
menu_h_line_3.addWidget(menu_answer_text_input)
menu_v_line.addLayout(menu_h_line_3)


menu_wrong3_text_lb = QLabel("Введіть текст неправильної відповіді:")
menu_wrong3_text_input = QLineEdit()

menu_h_line_4.addWidget(menu_answer_text_lb)
menu_h_line_4.addWidget(menu_answer_text_input)
menu_v_line.addLayout(menu_h_line_4)


menu_wrong4_text_lb = QLabel("Введіть текст неправильної відповіді:")
menu_wrong4_text_input = QLineEdit()

menu_h_line_5.addWidget(menu_answer_text_lb)
menu_h_line_5.addWidget(menu_answer_text_input)
menu_v_line.addLayout(menu_h_line_5)


menu_add_text_lb = QPushButton("Додати:")
menu_add_text_input = QPushButton()

menu_h_line_6.addWidget(menu_answer_text_lb)
menu_h_line_6.addWidget(menu_answer_text_input)
menu_v_line.addLayout(menu_h_line_6)


menu_clear_text_lb = QLabel("Введіть текст відповіді:")
menu_clear_text_input = QLineEdit()

menu_h_line_6.addWidget(menu_answer_text_lb)
menu_h_line_6.addWidget(menu_answer_text_input)
menu_v_line.addLayout(menu_h_line_6)








menu_window.setLayout(menu_v_line)