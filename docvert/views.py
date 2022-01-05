import os
from PyQt5 import QtCore
from docvert.ui.custom_widgets import FileListItem, CustomDialog
from pathlib import Path
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QFileDialog
from .ui.window import Ui_Form
from .converter import Converter, Merger



BASE_PATH = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + "\\"

class Window(QWidget, Ui_Form):
    cancelled = pyqtSignal()
    def __init__(self):
        super().__init__()
        self._setupUI()
        
        self._anyConversionDone = False   
        self._isCancelled = False         
        self._mergedPdfPath = None          
        self._checkedRadio = None         
        self._anyConversionDone = False

        self._radioButtons = [
            self.PPTtoPDF,
            self.WORDtoPDF,
        ]
        self._conversionType = None
        self._conversionType = None
        self._connectSignals()
          
    def _setupUI(self):
        self.setupUi(self)
        self._updateStateFirstTime()

    def _connectSignals(self):
        self.inputList.fileDropped.connect(self._isReady)
        self.clearAllBtn.clicked.connect(self._clearAll)
        self.convertBtn.clicked.connect(self.convertFiles)
        self.saveFolderBtn.clicked.connect(self._getSavePath)
        self.cancelBtn.clicked.connect(self.cancelled.emit)
        self.mergeBtn.clicked.connect(self._showMergeDialog)
        for rb in self._radioButtons:
            rb.clicked.connect(self._whichRadioChecked)     
    
    def _showErrorMessage(self, error):
        QtWidgets.QMessageBox.warning(
                                      self,
                                      "Warning!",
                                      error,
                                      QtWidgets.QMessageBox.Ok
                                    )
    @QtCore.pyqtSlot()
    def _showMergeDialog(self):
        self._mergedPdfPath = None
        dlg = CustomDialog()
        dlg.failFileNaming.connect(self._showErrorMessage)
        dlg.exec()
        text = dlg.mergeFileName

        if text != None:
            if text.endswith(".pdf"):
                self._mergedPdfPath = BASE_PATH + text
            else:
                self._mergedPdfPath = BASE_PATH + text + ".pdf"
        
            if self.sender() == self.mergeBtn:
                _merger = Merger(self._createOutputPaths(), self._mergedPdfPath)
                _merger.mergeFiles()
                
    def _showCancelDialog(self):
        # Don't show the message box unless at least one file is converted.
        if self.outputList.count() != 0 and self._isCancelled == True:
            messageBox = QtWidgets.QMessageBox.warning(
                self,
                "Warning!",
                "Do you want to remove converted files?",
                QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel,
            )
            if messageBox == QtWidgets.QMessageBox.Ok:
                for index in range(self.outputList.count()):
                    os.remove(self.outputList.item(index).text())
                self.outputList.clear()
    
    def _updateStateFirstTime(self):
        self.inputList.setStyleSheet("QListWidget{\n"
"    border: 2px solid rgb(186, 129, 255);\n"
"    background-image: url(:/icons/drop-file.png);\n"
"    background-position: center;\n"
"}\n"
"")
        self.convertBtn.setEnabled(False)   
        self.cancelBtn.setVisible(False)
        self.clearAllBtn.setEnabled(False)
        self.mergeBtn.setVisible(False)
        self.progressBar.setVisible(False)
        self.saveFolderEdit.setText(BASE_PATH)
        self.statusLabel.setText("Please drag and drop the files to be converted and select a conversion.")
               
    def _updateStateWhenReady(self):
        self.inputList.setStyleSheet("QListWidget{\n"
"    border: 2px solid rgb(186, 129, 255);\n"
"}\n"
"")
        self.convertBtn.setEnabled(True)
        self.convertBtn.setVisible(True)
        self.clearAllBtn.setEnabled(True)
        self.clearAllBtn.setVisible(True)
        self.cancelBtn.setVisible(False)
        self.progressBar.setVisible(False)
        self.statusLabel.setText("Please click the convert button to start conversion.")
    
    def _updateStateWhileRunning(self):
        self.convertBtn.setEnabled(False)
        self.clearAllBtn.setEnabled(False)
        self.convertBtn.setVisible(False)
        self.clearAllBtn.setVisible(False)
        self.cancelBtn.setVisible(True)
        self.saveFolderBtn.setEnabled(False)
        self.progressBar.setVisible(True)
        self.inputList.setAcceptDrops(False)
        self.statusLabel.setText("Converting...")
        for rb in self._radioButtons:
            rb.setEnabled(False)

    def _updateStateWhenFileConverted(self, outputFile):  
        self.inputList.takeItem(0)
        _outputItem = FileListItem(outputFile)
        _outputItem.setText(_outputItem.filePath)
        self.outputList.addItem(_outputItem) 

    def _updateStateForNextConversion(self):
        self.statusLabel.setText("Please drag and drop the files to be converted.")
        self._willMerged = False
        self.convertBtn.setEnabled(False)
        self.clearAllBtn.setEnabled(False)
        self.cancelBtn.setVisible(False)
        self._clearAll()
        self.progressBar.setVisible(False)
        self.progressBar.setValue(0)
        for rb in self._radioButtons:
            rb.setEnabled(True)

    def _updateStateWhenFinished(self):
        
        if self._isCancelled:
            self.statusLabel.setText("Conversion cancelled.")
            self.progressBar.setVisible(False)
            self.progressBar.setValue(0)
            
            self.cancelBtn.setVisible(False)
            
            self.convertBtn.setVisible(True)
            self.convertBtn.setEnabled(True)
            
            self.clearAllBtn.setVisible(True)
            self.clearAllBtn.setEnabled(True)
            
            self.saveFolderBtn.setEnabled(True)
        else:
            self.statusLabel.setText("Conversation has been completed. To start a new converstion please click clear button.")
            self.clearAllBtn.setEnabled(True)
            self.saveFolderBtn.setEnabled(True)
            self.convertBtn.setVisible(True)
            self.clearAllBtn.setVisible(True)
            self.cancelBtn.setVisible(False)
            self.mergeBtn.setVisible(True)
            for rb in self._radioButtons:
                rb.setEnabled(True)
        self.inputList.setAcceptDrops(True)

    def _updateProgressBar(self, fileNumber, fileCount):
        progressPercent = int(fileNumber / fileCount * 100)
        self.progressBar.setValue(progressPercent)
    
    def _clearAll(self):
        self.inputList.clear()
        self.outputList.clear()
        self.inputList.filePaths = []
        self._isReady()
               
    def _isReady(self):
        if self.inputList.count() != 0:
            self._updateStateWhenReady()
        elif self.inputList.count() == 0:
            self._updateStateFirstTime()
                     
    def _whichRadioChecked(self):
        for rb in self._radioButtons:
            if rb.isChecked():
                self._checkedRadio = rb.objectName()
        self._isReady()
                      
    def _runConverterThread(self, merge):
        self._thread = QThread()
        self._converter = Converter(
            itemList=self._createItemList(),
            outputList=self._createOutputPaths(),
            count=self.inputList.count(),
            saveFolder=merge
        )

        self._converter.moveToThread(self._thread)
        
        if self._checkedRadio == "PPTtoPDF":
            self._thread.started.connect(self._converter.PPTtoPDF)
        else:
            self._thread.started.connect(self._converter.WORDtoPDF)
              
        self._converter.renamedFile.connect(self._updateStateWhenFileConverted)
        self._converter.progressed.connect(self._updateProgressBar)
        
        self.cancelled.connect(lambda: self._converter._stopThread())
        self.cancelled.connect(self._cancelled)
        self._converter.finished.connect(self._thread.quit)
        self._converter.finished.connect(self._converter.deleteLater)
        self._converter.finished.connect(self._showCancelDialog)
        self._converter.failFileOpen.connect(self._showErrorMessage)
        self._converter.failFileOpen.connect(self._updateStateWhenReady)
        self._converter.failFileSave.connect(self._showErrorMessage)
        self._converter.failObjectCreation.connect(self._showErrorMessage)
        self._converter.failFileRemove.connect(self._showErrorMessage)
        self._converter.failFileRemove.connect(self._updateStateWhenFinished)
        self._thread.finished.connect(self._thread.deleteLater) 
        self._converter.finished.connect(self._updateStateWhenFinished)
        self._thread.start()

    def _controlFileTypes(self):
        _multipleFileType = False
        _fileSuffixes = self.inputList._getFileTypes()
        while _multipleFileType == False:    
            for type in _fileSuffixes:
                if self.WORDtoPDF.isChecked() and type.lower() not in [".docm", ".doc", ".docx",".dot", ".dotx"]:
                    _multipleFileType = True
                elif self.PPTtoPDF.isChecked() and type.lower() not in [".ppt", ".pptx",".pptm", ".ppsx", ".ppsm", ".pps", ".potx"]:
                    _multipleFileType = True
            break
        return _multipleFileType

    def convertFiles(self):
        self._isCancelled = False 
        try:    
            _isMultipleFileType  = self._controlFileTypes()
            if _isMultipleFileType:
                raise Exception
            if self.mergeCB.isChecked():  
                self._showMergeDialog()
                if self._mergedPdfPath == None:
                    self._updateStateWhenReady()
                else:
                    self._runConverterThread(self._mergedPdfPath)
                    self._updateStateWhileRunning()
                    self._anyConversionDone = True
                    self.clearAllBtn.clicked.connect(self._updateStateForNextConversion)
            else:
                self._runConverterThread(None)
                self._updateStateWhileRunning()
        except Exception:
            self._showErrorMessage("Inappropriate file type for selected file convertion. Make sure all the files in the list are the same file type or correct convertion type selected.")

    def _cancelled(self):
        self._isCancelled = True   
    
    def _getSavePath(self):
        _folder = str(QFileDialog.getExistingDirectory(self, "Select Directory")).replace("/","\\") + "\\"
        self.saveFolderEdit.setText(_folder)
        global BASE_PATH
        BASE_PATH = _folder 

    def _createOutputPaths(self):
        _outputPaths = []
        for index in range(self.inputList.count()):
            _outputPath = BASE_PATH + Path(self.inputList.item(index).filePath).stem + ".pdf"   # test.test.doc fixed by adding .pdf
            _outputPaths.append(_outputPath)
        return _outputPaths

    def _createItemList(self):
        _itemList = []
        for index in range(self.inputList.count()):
            _itemList.append(self.inputList.item(index).filePath)
        return _itemList
    
    