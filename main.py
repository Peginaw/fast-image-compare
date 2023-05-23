from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic, QtCore
import PyQt5.QtGui as qtg
from PyQt5.QtGui import QPixmap
import sys, os

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.setWindowTitle("Picture Compare")

        self.visible_picture = -1
        self.isPic1Loaded = False
        self.isPic2Loaded = False

        # Load the ui file, if created in QtDesigner
        uic.loadUi("CompareImages.ui", self)

        # Define our Widgets
        self.button1 = self.findChild(QPushButton, "pushButton_main")
        self.button2 = self.findChild(QPushButton, "pushButton_comp")
        self.button_swap = self.findChild(QPushButton, "pushButton_swap")
        self.button_prev = self.findChild(QPushButton, "pushButton_prev")
        self.button_next = self.findChild(QPushButton, "pushButton_next")
        self.button_refresh = self.findChild(QPushButton, "pushButton_refresh")
        
        self.info_label = self.findChild(QLabel, "info_label")
        self.info_label2 = self.findChild(QLabel, "info_label2")
        self.canvas_label = self.findChild(QLabel, "canvas_label")
        UI.setMinimumSize(self.canvas_label, 1, 1)

        # Click the box
        self.button1.clicked.connect(self.load_image1)
        self.button2.clicked.connect(self.load_image2)
        self.button_swap.clicked.connect(self.swap_images)
        self.button_next.clicked.connect(self.load_next)
        self.button_prev.clicked.connect(self.load_prev)
        self.button_refresh.clicked.connect(self.refresh)

        #Show The App
        self.show()

    def refresh(self):
        if self.isPic1Loaded: 
            self.format_image1()
        if self.isPic2Loaded: 
            self.format_image2()
            dir = os.path.dirname(self.fname2[0])
            self.fileList = []
            for file in os.scandir(dir):
                if file.is_file() and file.name.endswith(
                    (".png", ".jpg", ".jpeg", ".tiff", ".dmg")):
                    self.fileList.append(file.name)

        ##################################### IMAGE 1

    def load_image1(self):
        self.select_image1()
        if self.fname1[0] != '':
            self.format_image1()
            self.show_image1()
    
    def select_image1(self):
        # Open File Dialog, returns tuple of (filename, filetype)
        self.fname1 = QFileDialog.getOpenFileName(self, "Select the Base Picture", "./", "All Files (*);; PNG Files (*.png);; Jpg Files (*.jpg)")
        # Output filename to screen
        if self.fname1:
            self.info_label.setText(os.path.basename(self.fname1[0]))

    def format_image1(self):
        # Open the image
        self.pixmap1 = QPixmap(self.fname1[0])
        self.pixmap1 = self.pixmap1.scaled(self.canvas_label.size().width(), self.canvas_label.size().height(), QtCore.Qt.KeepAspectRatio)
        self.isPic1Loaded = True
       
    def show_image1(self):
        # Apply pic to canvas label
        self.canvas_label.setPixmap(self.pixmap1)
        self.visible_picture = 1

        ##################################### IMAGE 2
    
    def load_image2(self):
        self.select_image2()
        if self.fname2[0] != '':
            self.format_image2()
            self.show_image2()
            self.refresh()

    def select_image2(self):
        # Open File Dialog, returns tuple of (filename, filetype)
        try:
            self.fname2 = QFileDialog.getOpenFileName(self, "Select the Second Picture For Comparison", f"{os.path.dirname(self.fname2[0])}", "All Files (*);; PNG Files (*.png);; Jpg Files (*.jpg)")
        except:
            self.fname2 = QFileDialog.getOpenFileName(self, "Select the Second Picture For Comparison", "./", "All Files (*);; PNG Files (*.png);; Jpg Files (*.jpg)")

    def format_image2(self):
        self.info_label2.setText(os.path.basename(self.fname2[0])) # Update Comp file name label
        self.pixmap2 = QPixmap(self.fname2[0])
        self.pixmap2 = self.pixmap2.scaled(self.canvas_label.size().width(), self.canvas_label.size().height(), QtCore.Qt.KeepAspectRatio)         
        self.isPic2Loaded = True
     
    def show_image2(self):
        # Apply pic to canvas label
        self.canvas_label.setPixmap(self.pixmap2)
        self.visible_picture = 2

    def swap_images(self):
        if self.isPic1Loaded == False or self.isPic2Loaded == False:
            print("Two pictures haven't been selected yet. Unable to swap.")
            return
        if self.visible_picture == 1:
            self.show_image2()
        elif self.visible_picture == 2:
            self.show_image1()
        else:
            print("Neither pictures are currently visible. Unable to swap.")

    def load_next(self):
        # Extract path and filename
        dir = os.path.dirname(self.fname2[0])
        filename = os.path.basename(self.fname2[0])
        
        nextIndex = self.fileList.index(filename) + 1
        if nextIndex == len(self.fileList):
            nextIndex = 0

        # Open the image
        self.fname2 = (os.path.join(dir, self.fileList[nextIndex]), 0)
        self.format_image2()
        self.show_image2()

    def load_prev(self):
        # Extract path and filename
        dir = os.path.dirname(self.fname2[0])
        filename = os.path.basename(self.fname2[0])
        
        prevIndex = self.fileList.index(filename) - 1
        if prevIndex == -1:
            prevIndex = len(self.fileList) - 1

        # Open the image
        self.fname2 = (os.path.join(dir, self.fileList[prevIndex]), 0)
        self.format_image2()
        self.show_image2()


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()