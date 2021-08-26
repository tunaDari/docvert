# -*- coding: utf-8 -*-

"""This module provides the Converter class to convert files."""
import os, time
import pythoncom
import comtypes.client
from PyQt5.QtCore import QObject, pyqtSignal
from PyPDF2 import PdfFileMerger

class Converter(QObject):
    progressed = pyqtSignal(int, int)
    renamedFile = pyqtSignal(str)
    finished = pyqtSignal()
    failObjectCreation = pyqtSignal(str)
    failFileOpen = pyqtSignal(str)
    failFileSave = pyqtSignal(str)
    failFileRemove = pyqtSignal(str)

    def __init__(self, itemList, outputList, count, saveFolder):
        super().__init__()
        
        self._inputList = itemList
        self._outputList = outputList
        self._numOfConversion = count
        self._isRunning = True
        self._saveFolder = saveFolder

        
    def PPTtoPDF(self, formatType = 32):
        _counter = 0
        try:
            pythoncom.CoInitialize()  # allows multi-threading
            powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
            powerpoint.Visible = 1
  
            while self._isRunning and _counter < self._numOfConversion:
                ppt = powerpoint.Presentations.Open(self._inputList[_counter])
                ppt.SaveAs(self._outputList[_counter], formatType) # formatType = 32 for ppt to pdf
                ppt.Close()
                self.renamedFile.emit(self._outputList[_counter])
                _counter = _counter + 1
                self.progressed.emit(_counter, self._numOfConversion)
            self.finished.emit()
            powerpoint.Quit()
        except Exception:
            self.failFileOpen.emit("Not supported file type.")
            powerpoint.Quit()
        except Exception:
            self.failFileSave.emit("The file could not be saved.")

        if self._saveFolder != None and self._isRunning == True:
            _merger = PdfFileMerger()
            
            try:
                for pdf in self._outputList:
                    _merger.append(pdf)
                _merger.write(self._saveFolder)
                _merger.close()
                    # Deleting converted files since the files going to be merged
                for pdf in self._outputList:
                        os.remove(pdf)
            except:
                self.failFileRemove.emit(pdf + " could not be found and merging failed. Did you accidently deleted the file?")
                _merger.close()


    def WORDtoPDF(self, formatType = 17):
        _counter = 0
        try:
            pythoncom.CoInitialize()  # allows multi-threading
            word = comtypes.client.CreateObject('Word.Application')
            while self._isRunning and _counter < self._numOfConversion:
                doc = word.Documents.Open(self._inputList[_counter])  
                doc.SaveAs(self._outputList[_counter], formatType) # formatType = 17 for word to pdf        
                doc.Close()         
                self.renamedFile.emit(self._outputList[_counter])  
                _counter = _counter + 1    
                self.progressed.emit(_counter, self._numOfConversion)       
            self.finished.emit()
            word.Quit()       
        except Exception:
            self.failFileOpen.emit("Not supported file type.")
            word.Quit()
        except Exception:
            self.failFileSave.emit("The file could not be saved.")

        if self._saveFolder != None and self._isRunning == True:
            _merger = PdfFileMerger()
            try:
                for pdf in self._outputList:
                    _merger.append(pdf)
                _merger.write(self._saveFolder)
                _merger.close() 
                for pdf in self._outputList:
                    os.remove(pdf)
            except:
                self.failFileRemove.emit(pdf + " could not be found and merging failed. The file might be deleted before convertion done.")
                _merger.close()
        
    def _stopThread(self):
        self._isRunning = False

class Merger:

    def __init__(self, outputList, saveFolder):
        super().__init__()
        
        self._outputList = outputList
        self._saveFolder = saveFolder

    def mergeFiles(self):
        _merger = PdfFileMerger()
        try:
            for pdf in self._outputList:
                _merger.append(pdf)
            _merger.write(self._saveFolder)
            _merger.close() 
            for pdf in self._outputList:
                os.remove(pdf)
        except:
            self.failFileRemove.emit(pdf + " could not be found and merging failed. The file might be deleted before convertion done.")
            _merger.close()