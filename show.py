from PyQt5 import QtWidgets
import sys
import widget
import os

class event(QtWidgets.QMainWindow):
    def __init__(self):
        super(event, self).__init__()
        self.ui = widget.Ui_MainWindow()
        self.ui.setupUi(self)
        self.cwd = os.getcwd()
        self.ui.mybutton.clicked.connect(self.select)

    def select(self):
        filename, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "test", self.cwd, "AllFile(*)")
        self.ui.myline.setText(filename)
        











        

app = QtWidgets.QApplication([])

window = event()

window.show()
sys.exit(app.exec_())
