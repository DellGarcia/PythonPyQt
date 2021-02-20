from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout,
                             QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.label = QLabel('0', self)
        self.init()

    def init(self):

        hbox = QHBoxLayout()

        sld = QSlider(Qt.Horizontal, self)
        sld.setRange(0, 100)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setPageStep(5)

        sld.valueChanged.connect(self.update_label)

        self.label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label.setMinimumWidth(40)

        hbox.addWidget(sld)
        hbox.addSpacing(15)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QSlider')
        self.show()

    def update_label(self, value):

        self.label.setText(str(value))


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

