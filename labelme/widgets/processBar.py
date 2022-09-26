from select import select
from PyQt5.QtCore import (QCoreApplication)
from PyQt5.QtWidgets import (QLabel, QProgressBar, QSizePolicy,
                             QSpacerItem, QVBoxLayout, QWidget)


# class ProcessBar(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.verticalLayout_2 = QVBoxLayout()
#         self.verticalLayout_2.setObjectName(u"verticalLayout_2")
#         self.verticalLayout = QVBoxLayout()
#         self.verticalLayout.setObjectName(u"verticalLayout")
#         self.label_2 = QLabel()
#         self.label_2.setObjectName(u"label_2")

#         self.verticalLayout.addWidget(self.label_2)

#         self.verticalSpacer = QSpacerItem(
#             20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

#         self.verticalLayout.addItem(self.verticalSpacer)

#         self.progressBar = QProgressBar()
#         self.progressBar.setObjectName(u"progressBar")
#         self.progressBar.setValue(0)

#         self.verticalLayout.addWidget(self.progressBar)

#         self.label = QLabel()
#         self.label.setObjectName(u"label")

#         self.verticalLayout.addWidget(self.label)

#         self.verticalLayout_2.addLayout(self.verticalLayout)


class ProcessBar(QWidget):
    def __init__(self, title="进度条"):
        super(ProcessBar, self).__init__()
        self.resize(511, 135)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel()
        self.label_2.setText(title)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.progressBar = QProgressBar(self)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        self.label = QLabel(self)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.setLayout(self.verticalLayout_2)

    def setProcessValue(self, num):
        self.progressBar.setValue(num)

    def getProcessValue(self):
        return self.progressBar.value()
    
    def setProcessBarLabel(self,text):
        self.label.setText(text)
