#     |               |                                 |
                
#                 |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#          |                                  |                                     |
                
#                 |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#  |                          |                       |                    |
#          |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                                                        |
#     |                        |                                 |      |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                       |                    |
                
#                     |                                                |      |                                   |                               |                         |                               |                         |                               |                              |                               |
#          |                                   |                               |                   |                                |                       |                    |          |                                |                       |                    |          |                                |                       |                    |               |                                |                                        |
                
#                 |                     |
#  |                                |                       |                    |            |                                |                       |                    |     |                                |                       |                    |     |                                |                       |                              |                                |
#          |                               |                                         |                              |                       |                    |                           |                       |                    |                           |                       |                    |                                |                       |                    |
                
#  |         |                                    PRESENTATION                                                |                                |                    |   |                                |                    |   |                                |                    |        |                                |                    |
#                                                                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#               |                             /                 \                          |                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
                
#       |                            An overlay placing images top of all                    |                                           |               |                                           |               |                                           |                    |                                           |
                
#                          /                      |    v    |                    \
                
#                  Then allows you to set size, opacity , position of the uploaded picture       |                                |                                          |      |                                |                                          |      |                                |                                          |           |                                |  
#     |                  !      |                                   |     |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                           |
#                               |                                   |     |                  
#                  |            |                   Anyway          !                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |
                
#             |                      |                 have                                                 |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                                           |
                

#                |                                  FUN         |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                                                      |
                
#                                                        =)
                
#
#                               |                      or                                       |                                                            |                    |                |                       |                    |                |                       |                    |                    |                                           |
                

#             |                              |       DIE ! ! !        |                       |                            |                |                       |                    |                |                       |                    |                    |                                           |#     |                        |                                         |                                |
                
#
#                                                    !                                       |                                |                    |  |                                |                    |  |                                |                    |       |                                |                    |
                
#     |               |                                 !
                
#                 |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#          |                                  !                                     |
                
#                 |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#  |                          |                       |                    !
#          |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                    |                                    |
#     |                        |                                 |      |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                           |
                
#                     |                                                |      |                                   |                               |                         |                               |                         |                               |                              |                               |
#          |                                   |                               |                   |                                |                       |                    |          |                                |                       |                    |          |                                |                       |                    |               |                                                                |
              
#_ _  _ ____ ___ ____ _    _    ____ ___ _ ____ _  _
#| |\ | [__   |  |__| |    |    |__|  |  | |  | |\ |
#| | \| ___]  |  |  | |___ |___ |  |  |  | |__| | \|
        
import sys, ctypes,os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
                             QFileDialog, QGraphicsOpacityEffect, QLabel, QSlider, QSpinBox,
                             QGridLayout, QDialog,QFrame)
from PyQt5.QtGui import QPixmap,QFont,QIcon,QRegion,QPainterPath
from PyQt5.QtCore import Qt, QSize,QPoint



#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                

#OPENING | https://www.youtube.com/watch?v=_85LaeTCtV8 :3


    #function to make an exe file with py to exe
def ressource_path(relative_path):
    if getattr(sys, 'frozen', False):
        # The application is frozen (compiled)
        app_path = sys._MEIPASS
    else:
        # The application is not frozen (running from source)
        app_path = os.path.dirname(os.path.abspath(__file__))
#        app_path = os.path.join(script_dir, '..') 

    return os.path.join(app_path, relative_path)
#to make it works, you have to rename all your path with ressource_path (/path/) WHEN YOU WILL TURN THE SCRIPT TO EXE
#Example : /icon/lol.png  BECOME  ressource_path(/icon/lol.png)

# Load the style sheet
def load_stylesheet(file_path):
    with open(file_path, 'r') as file:
        stylesheet = file.read()
    return stylesheet




#____ _   _ ____ ___ ____ _  _    ___  ____ ____ 
#[__   \_/  [__   |  |___ |\/|    |__] |__| |__/ 
#___]   |   ___]  |  |___ |  |    |__] |  | |  \ 
                                                

# Here a mouse listener to make the app moving by holding the customised title bar
class CustomTitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.setMouseTracking(True) # Enable mouse tracking to detect mouse movement

        self.mouse_pressed = False 
        self.mouse_position = QPoint() # Initialize mouse_position to zero


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton: # Check if the left mouse button is pressed
            self.mouse_pressed = True # Set the mouse_pressed flag to true
            self.mouse_position = event.globalPos() - self.parent().pos() # Calculate the position of the mouse click relative to the parent widget
            event.accept()


    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton: # Check if the left mouse button is released
            self.mouse_pressed = False # Set the mouse_pressed flag to false
            event.accept()

    def mouseMoveEvent(self, event):
        if self.mouse_pressed: # Check if the mouse is being dragged
            self.parent().move(event.globalPos() - self.mouse_position) # Move the parent widget to the new mouse position
            event.accept()




#_  _ ____ _ _  _    ____ _    ____ ____ ____ 
#|\/| |__| | |\ |    |    |    |__| [__  [__  
#|  | |  | | | \|    |___ |___ |  | ___] ___] 


class layer0(QMainWindow):
    def __init__(self):
        super().__init__()


        # Make it in overlay, with custom (no)system, without background to make half opacity things
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint) 
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)


        # Style 
        self.central_widget = QFrame()
        self.setFixedSize(180, 200)
        self.setCentralWidget(self.central_widget)
        self.central_widget.setObjectName("centralFrame")

        stylesheet_path = ressource_path("styles/style1.txt")
        stylesheet = load_stylesheet(stylesheet_path)
        self.setStyleSheet(stylesheet)

        self.set_hexagon_shape()



        # Custom title bar
        self.title_bar = CustomTitleBar(self)
        self.title_bar.setGeometry(0, 0, self.width(), 30)

        # Hide button
        self.hide_button = QPushButton(self.title_bar)
        self.hide_button.setIcon(QIcon(ressource_path("assets/ico/hide.png")))
        self.hide_button.setGeometry(0, 5, 30, 20)
        self.hide_button.setStyleSheet("background-color: transparent;")
        self.hide_button.clicked.connect(self.toggle_window)

        # Title label
        self.title_label = QLabel("L A Y E R  O N E", self.title_bar, objectName="title")
        self.title_label.setGeometry(28, 5, 200, 20)
        self.title_label.setStyleSheet("background-color: transparent;")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.title_label.setFont(font)

        # Close button
        self.close_button = QPushButton(self.title_bar)
        self.close_button.setIcon(QIcon(ressource_path("assets/ico/close.png")))
        self.close_button.setGeometry(180, 5, 20, 20)
        self.close_button.setStyleSheet("background-color: transparent; ")
        self.close_button.clicked.connect(self.close_application)

        self.image_window = None
        self.config_popup = None

        # Create and connect widgets
        self.browse_button = QPushButton("BROWSE")
        self.browse_button.clicked.connect(self.upload_image)

        self.config_button = QPushButton("Configure")
        self.config_button.clicked.connect(self.show_config_popup)
        self.config_button.hide()

        self.opacity_slider = QSlider(Qt.Horizontal)
        self.opacity_slider.valueChanged.connect(self.change_opacity)
        self.opacity_slider.hide()

        self.close_image_button = QPushButton("Close Image")
        self.close_image_button.clicked.connect(self.close_image)
        self.close_image_button.hide()



        # Layout
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addSpacing(28) 
        self.layout.addWidget(self.browse_button)
        self.layout.addWidget(self.config_button)
        self.layout.addWidget(self.opacity_slider)
        self.layout.addWidget(self.close_image_button)

        self.layout.setSpacing(10)




        # Create a new widget for the close button
        self.close_button_widget = QWidget()
        self.close_button_widget.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.close_button_widget.setAttribute(Qt.WA_NoSystemBackground, True)
        self.close_button_widget.setAttribute(Qt.WA_TranslucentBackground, True)

        # Move the close button to the new widget
        self.close_button.setParent(self.close_button_widget)
        self.close_button.setGeometry(0,2, 20, 20)
        self.close_button.clicked.connect(self.close_application)

        # Show the close button widget
        self.close_button_widget.show()




# Calculate the new position for the close button widget
    def moveEvent(self, event):
        new_pos = self.mapToGlobal(QPoint(self.width() - 10, 0))
        self.close_button_widget.move(new_pos)



#Draw an hexagon like for the shape of the main window
    def set_hexagon_shape(self):
        path = QPainterPath()
        path.moveTo(30, 0)
        path.lineTo(self.width() - 20, 0)
        path.lineTo(self.width(), 20)
        path.lineTo(self.width(), self.height() - 0)
        path.lineTo(self.width() - 20, self.height())
        path.lineTo(20, self.height())
        path.lineTo(0, self.height() - 20)
        path.lineTo(0, 0)
        path.closeSubpath() 

        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)


# Hide / Show the app
    def toggle_window(self):
        if self.central_widget.isVisible():
            self.central_widget.hide()
            self.title_label.hide()
            self.close_button.hide()
            self.hide_button.setIcon(QIcon(ressource_path("assets/ico/open.png")))
            self.close_button_widget.hide() 
        else:
            self.central_widget.show()
            self.title_label.show()
            self.close_button.show()
            self.hide_button.setIcon(QIcon(ressource_path("assets/ico/hide.png")))
            self.close_button_widget.show() 


    def close_application(self):
        self.close()



# Upload an image and display it in a separate window
    def upload_image(self):
        if not self.image_window:
            file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.xpm *.jpg *.bmp)")

            if file_name:
                pixmap = QPixmap(file_name)
                self.image_window = layer1(pixmap, pixmap)
                self.image_window.show()
                self.config_button.show()
                self.close_image_button.show()
                self.opacity_slider.show()

# Close the image window
    def close_image(self):
        if self.image_window:
            self.image_window.close()
            self.image_window = None
            self.config_button.hide()
            self.close_image_button.hide()
            self.opacity_slider.hide()
            if self.config_popup:
                self.config_popup.close()
                self.config_popup = None

# Handle close event for the main window
    def closeEvent(self, event):
        if self.image_window:
            event.ignore()
            self.close_image()
        else:
            event.accept()


# Change the opacity of the image window
    def change_opacity(self, value):
        if self.image_window:
            self.image_window.set_opacity(value / 100)

# Show configuration popup for the image window

    def show_config_popup(self):
        self.config_popup = layer_config(self.image_window) 
        self.config_popup.show()








# _ _  _ ____ ____ ____    _ _ _ _ _  _ ___  ____ _ _ _ 
# | |\/| |__| | __ |___    | | | | |\ | |  \ |  | | | | 
# | |  | |  | |__] |___    |_|_| | | \| |__/ |__| |_|_| 
                                                      

class layer1(QWidget):
    def __init__(self, pixmap, original_pixmap):
        super().__init__()

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.WindowTransparentForInput)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.pixmap = pixmap
        self.original_pixmap = original_pixmap

        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.resize(pixmap.size())



        # Make the window transparent for input
        # Retrieve the window handle using winId() and convert it to an integer
        hwnd = self.winId().__int__()
        # Get the current window style using GetWindowLongW
        style = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
        # Add the WS_EX_TRANSPARENT style flag to the window style
        style |= 0x00000020  # WS_EX_TRANSPARENT
        # Update the window style with the modified style using SetWindowLongW
        ctypes.windll.user32.SetWindowLongW(hwnd, -20, style)


        self.opacity_effect = QGraphicsOpacityEffect(self.label)
        self.label.setGraphicsEffect(self.opacity_effect)



# Set opacity for the image window
    def set_opacity(self, value):
        self.opacity_effect.setOpacity(value)
        self.setWindowOpacity(value)


# Resize the image in the window
    def resize_image(self, percentage):

        factor = percentage / 100

        # Compute the new size by multiplying the original size with the scaling factor
        new_size = self.original_pixmap.size() * factor

        # Ensure the new size is at least 1x1 pixels
        if new_size.width() < 1 or new_size.height() < 1:
            new_size = QSize(1, 1)

        # Scale the original pixmap to the new size while preserving aspect ratio and using smooth transformations
        new_pixmap = self.original_pixmap.scaled(new_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Set the new pixmap to the QLabel and resize the window to fit the new pixmap size
        self.label.setPixmap(new_pixmap)
        self.resize(new_pixmap.size())



#_ _  _ ____ ____ ____    ____ ____ ___ ___ _ _  _ ____ ____ 
#| |\/| |__| | __ |___    [__  |___  |   |  | |\ | | __ [__  
#| |  | |  | |__] |___    ___] |___  |   |  | | \| |__] ___] 

class layer_config(QDialog):
    def __init__(self, image_window):
        super().__init__()

        self.image_window = image_window
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint) 
        
        # Style 
        self.setObjectName("centralFrame")

        self.setFixedSize(150, 180)
        stylesheet_path = ressource_path("styles/style1.txt")
        stylesheet = load_stylesheet(stylesheet_path)
        self.setStyleSheet(stylesheet)

        self.set_hexagon_shape()


        # Custom title bar
        self.title_bar = CustomTitleBar(self)
        self.title_bar.setGeometry(0, 0, self.width(), 30)

        # Title label
        self.title_label = QLabel("S E T T I N G S", self.title_bar,objectName="title2")
        self.title_label.setGeometry(8, 5, 200, 20)
        self.title_label.setStyleSheet("background-color: transparent;")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.title_label.setFont(font)

        # Create and connect widgets
        self.resize_label = QLabel("Resize",objectName="info")

        self.resize_slider = QSlider(Qt.Horizontal)
        self.resize_slider.setRange(10, 1000)
        self.resize_slider.valueChanged.connect(self.change_image_size)

        self.x_label = QLabel("X",objectName="infoxy")

        self.x_spinbox = QSpinBox()
        self.x_spinbox.setRange(-10000, 10000)
        self.x_spinbox.valueChanged.connect(self.change_image_position)

        self.y_label = QLabel("Y",objectName="infoxy")

        self.y_spinbox = QSpinBox()
        self.y_spinbox.setRange(-10000, 10000)
        self.y_spinbox.valueChanged.connect(self.change_image_position)

        # Set layout
        self.layout = QGridLayout()
        self.layout.setContentsMargins(25, 30, 25, 25)
        self.layout.addWidget(self.resize_label)
        self.layout.addWidget(self.resize_slider, 1, 0, 1, 2)
        self.layout.addWidget(self.x_label, 2, 0)
        self.layout.addWidget(self.x_spinbox, 3, 0)
        self.layout.addWidget(self.y_label, 2, 1)
        self.layout.addWidget(self.y_spinbox, 3, 1)

        self.setLayout(self.layout)

        # Close button
        self.config_close = QPushButton()
        self.config_close.setIcon(QIcon(ressource_path("assets/ico/close.png")))
        self.config_close.setStyleSheet("background-color: transparent;")
        self.config_close.clicked.connect(self.close)

        # Create a new widget for the close button
        self.config_close_widget = QWidget()
        self.config_close_widget.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.config_close_widget.setAttribute(Qt.WA_NoSystemBackground, True)
        self.config_close_widget.setAttribute(Qt.WA_TranslucentBackground, True)

        # Move the close button to the new widget
        self.config_close.setParent(self.config_close_widget)
        self.config_close.setGeometry(0, 0, 20, 20)  # Ajustez la position du bouton de fermeture

        # Show the close button widget
        self.config_close_widget.show()

        # Connect destroyed signal to close_button_widget_close function
        self.destroyed.connect(self.closeEvent)

        # Add offset for the close button
        self.close_button_offset = QPoint(-10,0)  


# Function to close popup window
    def closeEvent(self, event):
        self.config_close_widget.close()
        event.accept()

# Calculate the new position for the close button widget
    def moveEvent(self, event):
        new_pos = self.mapToGlobal(QPoint(self.width() + self.close_button_offset.x(), self.close_button_offset.y()))
        self.config_close_widget.move(new_pos)



# Change image size based on the slider value
    def change_image_size(self, value):
        if self.image_window:
            self.image_window.resize_image(value)

# Change image position based on the spinbox values
    def change_image_position(self):
        if self.image_window:
            new_x = self.x_spinbox.value()
            new_y = self.y_spinbox.value()
            self.image_window.move(new_x, new_y)


# Draw same "hexagon" as layer0
    def set_hexagon_shape(self):
        path = QPainterPath()
        path.moveTo(30, 0)
        path.lineTo(self.width() - 20, 0)
        path.lineTo(self.width(), 20)
        path.lineTo(self.width(), self.height() - 0)
        path.lineTo(self.width() - 30, self.height())
        path.lineTo(30, self.height())
        path.lineTo(0, self.height() - 30)
        path.lineTo(0, 0)
        path.closeSubpath() 

        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)

#____ ____ ____ _  _ ____ ___    _    ____ _  _ _  _ ____ _  _
#|__/ |  | |    |_/  |___  |     |    |__| |  | |\ | |    |__|
#|  \ |__| |___ | \_ |___  |     |___ |  | |__| | \| |___ |  |
                
#ENDING | https://www.youtube.com/watch?v=CgZVrvQZB6U&ab_channel=SECRETGUEST :3


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = layer0()
    main_window.show()
    sys.exit(app.exec_())

