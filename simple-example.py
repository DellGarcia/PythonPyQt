from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QSlider

import sys

states = ["SP", "MG", "ES", "RJ"]


def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 500, 300)  # sets the windows x, y, width, height
    win.setWindowTitle("My first window!")  # setting the window title

    label = QLabel(win)
    label.setGeometry(50, 50, 230, 50)
    label.setText("My first label with PyQT")
    label.setFont(QFont('Verdana', 14))

    select = QComboBox(win)
    select.setGeometry(50, 100, 230, 30)
    select.addItems(states)
    select.setFont(QFont('Verdana', 10))

    slider = QSlider(Qt.Horizontal, win)
    slider.setGeometry(50, 150, 230, 30)

    win.show()
    sys.exit(app.exec_())


main()
