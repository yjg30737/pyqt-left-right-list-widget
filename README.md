# pyqt-left-right-list-widget
PyQt QListWidget which can add QListWidgetItem consist of two words. One word is left-aligned, the other is right-aligned.

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-left-right-list-widget.git --upgrade```

## Usage
```addLeftRightItem(left_str: str, right_str: str)``` to insert a pair of word at the end of the list widget.

## Example
Code Sample
```python
from PyQt5.QtWidgets import QHBoxLayout, QApplication, \
    QVBoxLayout, QPushButton, QWidget

from pyqt_left_right_list_widget import LeftRightListWidget


class LeftRightListWidgetTestExample(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        delBtn = QPushButton('Delete')
        delBtn.clicked.connect(self.__delete)

        lay = QHBoxLayout()
        lay.addWidget(delBtn)
        lay.setContentsMargins(0, 0, 0, 0)

        topWidget = QWidget()
        topWidget.setLayout(lay)

        self.__listWidget = LeftRightListWidget()
        # Add three pair of words
        self.__listWidget.addLeftRightItem('Ganon', 'Villain')
        self.__listWidget.addLeftRightItem('Zelda', 'Princess')
        self.__listWidget.addLeftRightItem('Link', 'Hero')
        lay = QHBoxLayout()
        lay.addWidget(self.__listWidget)
        lay.setContentsMargins(0, 0, 0, 0)

        bottomWidget = QWidget()
        bottomWidget.setLayout(lay)

        lay = QVBoxLayout()
        lay.addWidget(topWidget)
        lay.addWidget(bottomWidget)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.setLayout(lay)

    # Remove selected item
    def __delete(self):
        item = self.__listWidget.currentItem()
        if item:
            self.__listWidget.takeItem(self.__listWidget.currentRow())


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = LeftRightListWidgetTestExample()
    ex.show()
    sys.exit(app.exec_())
```

Result

![image](https://user-images.githubusercontent.com/55078043/148160564-b280439f-3a9c-403d-8976-395d9c750f82.png)
