
import sys
from PyQt5.QtWidgets import *
from tetris_board import TetrisBoard
from mainwindow import TetrisMainWindow

if __name__ == '__main__':
    app = QApplication([])
    window = TetrisMainWindow()
    # window = TetrisBoard()
    sys.exit(app.exec_())