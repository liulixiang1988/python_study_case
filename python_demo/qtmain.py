#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui

from qtdemo import *


class AppUI(Ui_Dialog):
	def setupUi(self, Dialog):
		super(AppUI, self).setupUi(Dialog)
		self.pushButton.clicked.connect(self.sayHello)

	def sayHello(self):
		self.lineEdit.setText('你好')

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = AppUI()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())