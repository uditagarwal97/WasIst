from PyQt4 import QtCore, QtGui
import urllib,json
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Google PySearch"))
        Dialog.resize(800, 500)
        Dialog.setAutoFillBackground(True)
        
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 70, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 70, 98, 27))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.submit_clicked)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 141, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(30, 100, 731, 192))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "Submit", None))
        self.label.setText(_translate("Dialog", "Enter your query:", None))
    
    def submit_clicked(self):
        query=self.lineEdit.text()
        print("button pressed: "+str(query))
        self.textBrowser.setText("gotcha... searching web")
        response=self.google(query)
        self.textBrowser.setText(response)
        
    def google(self,query):
        try:
            
            data=urllib.urlopen("https://www.googleapis.com/customsearch/v1?key=<MY_API_KEY>&cx=009788607993331168607:dhlgzmvvg-m&q="+str(query))
            response=json.load(data)
            search_title=response['queries']['request'][0]['title']
            no_of_results=response['queries']['request'][0]['count']
            print("title: "+str(search_title))
            print("Total number of results = "+str(no_of_results))
            data.close()        
            text=''
            for handle in response['items']:
                text=str(text)+str(handle['title'])
                text=text+'\n'
                text=text+str(handle['link'])
                text=text+'\n'
            return text
        except:
            print("error encountered")
            return "Seach failed!! Please try with a modified key word"
        
if __name__ == "__main__":
    import sys,os
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    #thread=Thread(target=Dialog.show)
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    try:
        sys.exit(app.exec_())
    except:
        print("error while closing")
        python=sys.executable
        os.execl(python,python,* sys.argv)

