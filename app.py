import dice
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QTextEdit, QGridLayout, QApplication, QPushButton, QComboBox)


class SimpleDiceRoller(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Row 1
        dietype = QLabel('Type')
        modifier = QLabel('Modifier')
        number = QLabel('Number')

        # Row 2
        self.cbDieType = QComboBox()
        self.cbDieType.addItems(['Coin', 'D4', 'D6', 'D8', 'D10',
                            'D20', 'D100'])
        self.cbModifier = QComboBox()
        self.cbModifier.addItems(['-10', '-9', '-8', '-7', '-6', '5',
                                  '-4', '-3', '-2', '-1', '0', '1',
                                  '2', '3', '4', '5', '6', '7',
                                  '8', '9', '10'])
        self.cbModifier.setCurrentIndex(10)
        self.cbNumber = QComboBox()
        self.cbNumber.addItems(['1', '2', '3', '4', '5',
                                '6', '7', '8', '9', '10',
                                '11', '12', '13', '14', '15',
                                '16', '17', '18', '19', '20'])

        # Row 3
        btnRoll = QPushButton('Roll', self)
        btnRoll.clicked.connect(self.clickRoll)
        btnClear = QPushButton('Clear', self)
        btnClear.clicked.connect(self.clickClear)

        # Output
        self.txtedtOutput = QTextEdit()
        self.txtedtOutput.setReadOnly(True)


        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(dietype, 0, 0)
        grid.addWidget(modifier, 0, 1)
        grid.addWidget(number, 0, 2)

        grid.addWidget(self.cbDieType, 1, 0)
        grid.addWidget(self.cbModifier, 1, 1)
        grid.addWidget(self.cbNumber, 1, 2)

        grid.addWidget(btnRoll, 2, 0)
        grid.addWidget(btnClear, 2, 2)

        grid.addWidget(self.txtedtOutput, 3, 0, 5, 0)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Simple Dice Roller')
        self.show()

    def clickRoll(self):
        result = dice.roll(self.cbDieType.currentText(),
                           int(self.cbModifier.currentText()),
                           int(self.cbNumber.currentText()))
        if self.cbDieType.currentText() == 'Coin':
            for idx, item in enumerate(result[1]):
                if item == 1:
                    result[1][idx] = 'Heads'
                else:
                    result[1][idx] = 'Tails'
            postToOutput = ('Total Heads: ' + str(result[1].count('Heads')) + '\n' +
                            'Total Tails: ' + str(result[1].count('Tails')) + '\n' +
                            'Flips: ' + str(result[1]))
            self.txtedtOutput.setText(postToOutput)
        else:
            self.txtedtOutput.setText('Total: ' + str(result[0]) + '\n' + 'Rolls: ' + str(result[1]))
        print("Rolling the dice...")

    def clickClear(self):
        self.txtedtOutput.setText('')
        self.cbModifier.setCurrentIndex(10)
        self.cbNumber.setCurrentIndex(0)
        print('Clearing output...')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = SimpleDiceRoller()
    sys.exit(app.exec_())
