import os
from pathlib import Path
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QWidget
import win32api  
import win32con  
import win32ui  
import win32gui
from win32com.shell import shell, shellcon    
from PIL import Image, ImageTk,ImageQt

class FileList(QtWidgets.QListWidget):

    fileDropped = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(FileList, self).__init__(parent)

    def _getFileTypes(self):
        _fileTypes = []
        for index in range(self.count()):
            _fileTypes.append(self.item(index).suffix)
        return _fileTypes

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()

            for url in event.mimeData().urls():
                if os.path.exists(url.toLocalFile()):
                    _listItem = FileListItem(str(url.toLocalFile()).replace("/", "\\"))
                    if _listItem.suffix.lower() in [".ppt", ".pptx",".pptm", ".ppsx", ".ppsm", ".pps", ".potx", ".docm", ".doc", ".docx",".dot", ".dotx"]:
                        self.addItem(_listItem)
                    else:
                        event.ignore()  
            self.fileDropped.emit()
        else:
            event.ignore()
            

class FileListItem(QtWidgets.QListWidgetItem):
    def __init__(self, path):
        super().__init__()
        
        self.filePath = path
        self.stem = str(Path(self.filePath).stem)
        self.suffix = str(Path(self.filePath).suffix)
        self.outputFilePath = None
        self.icon = self._getIcon(self)
        self.fileName = str(Path(self.filePath).name)
        self.setIcon(self.icon)
        self.setText(self.fileName)
    
        
    def _getIcon(self, item):
        SHGFI_ICON = 0x000000100  
        SHGFI_ICONLOCATION = 0x000001000  
        SHIL_SIZE = 0x00001  

        ret, info = shell.SHGetFileInfo(item.filePath, 0, SHGFI_ICONLOCATION | SHGFI_ICON | SHIL_SIZE)  
        hIcon, iIcon, dwAttr, name, typeName = info  
        ico_x = win32api.GetSystemMetrics(win32con.SM_CXICON)  
        hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))  
        hbmp = win32ui.CreateBitmap()  
        hbmp.CreateCompatibleBitmap(hdc, ico_x, ico_x)  
        hdc = hdc.CreateCompatibleDC()  
        hdc.SelectObject(hbmp)  
        hdc.DrawIcon((0, 0), hIcon)  
        win32gui.DestroyIcon(hIcon)  

        bmpinfo = hbmp.GetInfo()  
        bmpstr = hbmp.GetBitmapBits(True)  
        img = Image.frombuffer(  
            "RGBA",  
            (bmpinfo["bmWidth"], bmpinfo["bmHeight"]),  
            bmpstr, "raw", "BGRA", 0, 1  
        )  

        img = img.resize((20, 20), Image.ANTIALIAS)  
        qt_image = ImageQt.ImageQt(img)
        pixmap = QtGui.QPixmap.fromImage(qt_image)
        icon = QtGui.QIcon(pixmap)
        return icon
        
class CustomDialog(QtWidgets.QDialog):
    failFileNaming = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.mergeFileName = None
        self.closed = False

        self.setWindowTitle("Insert file name")
        self.okBtn = QtWidgets.QPushButton("Convert")
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setMaxLength(100)
        self.okBtn.setEnabled(False)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.okBtn)
        self.setLayout(self.layout)
        self.lineEdit.textChanged.connect(self._controlLineEdit)
        self.okBtn.clicked.connect(self._getLineText)

    def closeEvent(self, event):
            event.accept() 
            self.closed = True

    def _controlLineEdit(self):
        if self.lineEdit.text() == "":
            self.okBtn.setEnabled(False)
        else:
            self.okBtn.setEnabled(True)
        
    def _getLineText(self):
        _forbiddenChars = '<>:"/\>|?*'
        if any(c in _forbiddenChars for c in self.lineEdit.text()):
            self.failFileNaming.emit("Forbidden characters.")
        else:
            self.mergeFileName = self.lineEdit.text()
            self.close()
            self.closed = False



    







