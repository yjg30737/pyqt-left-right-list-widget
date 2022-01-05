from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QWidget, QFormLayout, QLabel
from PyQt5.QtCore import Qt, QSize


class LeftRightListWidget(QListWidget):

    def __init__(self):
        super().__init__()
        self._initUi()

    def _initUi(self):
        pass

    def addLeftRightItem(self, left_str: str, right_str: str):
        item = QListWidgetItem(self)

        left_lbl = QLabel(left_str)
        left_lbl.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        right_lbl = QLabel(right_str)
        right_lbl.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        right_lbl.setStyleSheet('QLabel { color: #888888 }')

        lay = QFormLayout()
        lay.addRow(left_lbl, right_lbl)

        widget = QWidget()
        widget.setLayout(lay)

        item.setSizeHint(QSize(self.sizeHint().width(), widget.sizeHint().height()))
        self.setItemWidget(item, widget)
        self.setCurrentItem(item)

    def getWidget(self, idx):
        return self.itemWidget(self.item(idx))