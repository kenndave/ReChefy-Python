from PyQt5.QtWidgets import *
import sys
import controller

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = controller.Controller()
    main.show()
    sys.exit(app.exec_())
