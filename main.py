from PyQt5 import QtCore, QtGui, QtWidgets
from mplwidget import MplWidget
from mplwidget_2 import MplWidget_2
import numpy as np
import pandas as pd
import random


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1246, 572)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dice.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.total_label = QtWidgets.QLabel(Form)
        self.total_label.setObjectName("total_label")
        self.horizontalLayout.addWidget(self.total_label)
        self.total = QtWidgets.QLineEdit(Form)
        self.total.setObjectName("total")
        self.horizontalLayout.addWidget(self.total)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.button = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../dice.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button.setIcon(icon1)
        self.button.setObjectName("button")
        self.horizontalLayout_4.addWidget(self.button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.MplWidget = MplWidget(Form)
        self.MplWidget.setObjectName("MplWidget")
        self.horizontalLayout_2.addWidget(self.MplWidget)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.MplWidget_2 = MplWidget_2(Form)
        self.MplWidget_2.setObjectName("MplWidget_2")
        self.horizontalLayout_3.addWidget(self.MplWidget_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.label = QtWidgets.QLabel(Form)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        # Trigger Button
        self.button.clicked.connect(self.update_graph)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Rolling Dice probability"))
        self.total_label.setText(_translate("Form", "Number of rolling"))
        self.total.setText(_translate("Form", "5000"))
        self.label.setText(_translate("Form", "<html><head/><body><p>Created by Mohammad Torkaman Dehnavi</p><p>Email: mtorkaman69@gmail.com</p><p>Github: mohammaddehnavi</p></body></html>"))
        self.button.setText(_translate("Form", "Calculate!"))

    def update_graph(self):
        num_sides = 6
        prob_die = num_sides * [1. / num_sides]

        # Simulate numerical dice roll
        def roll_die(N, prob=prob_die, num_sides=6):
            return np.random.choice(np.arange(1, num_sides + 1), size=N, p=prob)

        # Convenience Function to roll a die x *times*, and plot the results.
        # Build an array of die rolls
        number = int(self.total.text())
        times = number
        p = prob_die
        ns = num_sides
        rolls = roll_die(times, p, ns)

        # Now histogram them.
        results, bins = np.histogram(rolls, bins=ns)

        # For simplicity turn into a Pandas Series.
        rolls = pd.Series(results, index=np.arange(1, ns + 1)) / np.sum(results)

        ##
        # Setting the seed
        random.seed(1991)

        # Defining a function for rolling the dice
        def Roll_2(n):
            """This function simulates rolling a dice for n-times"""

            # Empty vector to store the result of dice roll
            result_2 = []

            for i in range(1, n + 1):
                result_2.append(random.choice([1, 2, 3, 4, 5, 6]))
            return result_2

        # Now, lets roll the dice for a certain amount of times
        result_2 = Roll_2(number)

        # Now, I want to plot how the average of dice rolls converge to the expected value (3.5)
        # Empty list to store the values of averages
        averages = []

        _cumsum = np.cumsum(result_2)
        for index in range(len(_cumsum)):
            averages.append(_cumsum[index] / (index + 1))
        ##
        # Create canvas
        colormap = np.array(['blue', 'orange', 'green', 'red', 'purple', 'lightcoral'])
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.bar(rolls.index, rolls.values, width=0.5, bottom=None, color=colormap, edgecolor="black")
        self.MplWidget.canvas.axes.axhline(xmin=0, xmax=1, y=1 / ns, color='black', linewidth=4.0, linestyle='-.', label='Theory=0.16666')
        self.MplWidget.canvas.axes.legend(fontsize=8, loc ='upper right')
        self.MplWidget.canvas.axes.set_title(f'{times} Rolls', fontsize=24)
        self.MplWidget.canvas.axes.set_ylabel("Probability", fontsize=12)
        self.MplWidget.canvas.axes.set_xticklabels(np.arange(0, 7), fontsize=18)
        self.MplWidget.canvas.draw()

        self.MplWidget_2.canvas.axes.clear()
        self.MplWidget_2.canvas.axes.axhline(y=21 / ns, color='black', linewidth=4.0, linestyle='-.', label='Theory=3.5')
        self.MplWidget_2.canvas.axes.legend(fontsize=8, loc='upper right')
        self.MplWidget_2.canvas.axes.plot(averages, 'o-', alpha=0.75, label='Simulation')
        self.MplWidget_2.canvas.axes.set_title("Average value of Dice rolled", fontsize=16)
        self.MplWidget_2.canvas.axes.set_xlabel("Trials", fontsize=12)
        self.MplWidget_2.canvas.axes.set_ylabel("Average of all outcomes", fontsize=12)
        self.MplWidget_2.canvas.axes.set_xlim(0, number)
        self.MplWidget_2.canvas.draw()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
