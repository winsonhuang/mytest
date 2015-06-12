# -*- coding: utf-8 -*-

'''
Created on 2015年6月12日上午11:12:48

@author: Huang
'''

import sys 
from PyQt4 import QtGui
from PyQt4 import QtCore

from ui_widget import Ui_MainWindow

 
class PyqtDemo(QtGui.QWidget,Ui_MainWindow):
    
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.setupUi(self)
    
        #c1 12px ×3/4 =9pt
        #c2 1.5em ×16 =24px
        # acc accuracy 位数精度
        self.c1 = 0.75
        self.c2 = 16
        self.acc = 3
#     def opStr(self, ctype): 
#         if(self.indexOf(ctype)==True):
#             print self
#             return self
#         else:
#             print self+ctype
#             return self+ctype
    
    def calcPxto(self):
        txt = self.txt_Pixels.text()
        if(txt.indexOf("px")!=True): txt+="px"
        txt = float(txt[0:-2])
        
        px = round(txt,self.acc)
        pt = round(txt*self.c1,self.acc)
        em = round(txt/self.c2,self.acc)
                
        self.txt_Pixels.setText(str(px)+"px")
        self.txt_Points.setText(str(pt)+"pt")
        self.txt_EMS.setText(str(em)+"em")
        
    def calcPtTo(self):
        txt = self.txt_Points.text()
        if(txt.indexOf("pt")!=True): txt+="pt"
        txt =  float(txt[0:-2])
        
        px = round(txt/self.c1,self.acc)
        pt = round(txt,self.acc)
        em = round(txt/self.c1/self.c2,self.acc)
        
        self.txt_Pixels.setText(str(px)+"px")
        self.txt_Points.setText(str(pt)+"pt")
        self.txt_EMS.setText(str(em)+"em")
        
    def calcEmTo(self): 
        txt = self.txt_EMS.text()
        if(txt.indexOf("em")!=True): txt+="pt"
        txt =  float(txt[0:-2])
        
        px = round(txt*self.c2,self.acc)
        pt = round(txt*self.c1*self.c2,self.acc)
        em = round(txt,self.acc)
        
        self.txt_Pixels.setText(str(px)+"px")
        self.txt_Points.setText(str(pt)+"pt")
        self.txt_EMS.setText(str(em)+"em")
        
    @QtCore.pyqtSignature("")
    def on_btn_PxTo_clicked(self):
        self.calcPxto()
    
    @QtCore.pyqtSignature("")
    def on_btn_PtTo_clicked(self):
        self.calcPtTo()
        
    @QtCore.pyqtSignature("")
    def on_btn_EmTo_clicked(self):
        self.calcEmTo()

        
    @QtCore.pyqtSignature("")
    def on_txt_pixels_keyPressEvent(self):
        self.calcPxto()
    
    

        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    widget = PyqtDemo()
    widget.show()
    sys.exit(app.exec_())
