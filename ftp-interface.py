import sys
from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    label = QtWidgets.QLabel('Hello World!')
    # window = QtWidgets.QMainWindow()
    # button = QtWidgets.QPushButton("Hello, PyQt!")
    # window.setCentralWidget(button)
    # window.show()
    label.show()
    app.exec_()

if __name__ == '__main__':
    main()