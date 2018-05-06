#
#    ___          _     _            __  ___     __          	 /\_______/\
#   / _ \___ ____(_)__ (_)__  ___   /  |/  /__ _/ /_____ ____ 	 /_  ___   \
#  / // / -_) __/ (_-</ / _ \/ _ \ / /|_/ / _ `/  '_/ -_) __/	/ @\/ @ \   \
# /____/\__/\__/_/___/_/\___/_//_//_/  /_/\_,_/_/\_\\__/_/   	\__/\___/   /
#																 \_\/______/
#  DecisionMaker.py 											 /     /\\\\\ 
#  Dylan Everingham for Marissa Kohan							|      \\\\\\\ 
#																 \      \\\\\\\ 
#																  \______/\\\\\
#																	_||_||_

# Main execution thread for DecisionMaker app
# Contains all GUI elements

# Dependencies
import sys
import time
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, \
	QDesktopWidget, QVBoxLayout, QPushButton, QSlider, QGridLayout, QLabel
from PyQt5.QtGui import QIcon
from DecisionMaker import *

# DecisionMakerWindow class
# Defines QtWidget representing DecisionMaker GUI window
class DecisionMakerWindow(QMainWindow):
	# DecisionMakerWindow class constructor
	def __init__(self):
		# Call supercalss constructor
		super().__init__()

		# Initialize backend
		self.decision_maker = DecisionMaker('Possibilities.csv')

		# These parameter values get adjusted by the fron panel controls
		self.hunger_level = 0
		self.thirst_level = 0
		self.energy_level = 0
		self.introvert_level = 0
		self.stress_level = 0
		
		# Initialize UI elements

		# Status bar
		#self.statusBar().showMessage('Ready')

		# Menu bar
		#menu_bar = self.menuBar()
		#file_menu = menu_bar.addMenu('&File')

		# Parameter sliders
		self.slider_hunger = QSlider(Qt.Horizontal, self)
		self.slider_hunger.valueChanged.connect(self.setHungerLevel)
		self.slider_hunger.setRange(-5,5)

		self.slider_thirst = QSlider(Qt.Horizontal, self)
		self.slider_thirst.valueChanged.connect(self.setThirstLevel)
		self.slider_thirst.setRange(-5,5)

		self.slider_energy = QSlider(Qt.Horizontal, self)
		self.slider_energy.valueChanged.connect(self.setEnergyLevel)
		self.slider_energy.setRange(-5,5)

		self.slider_introvert = QSlider(Qt.Horizontal, self)
		self.slider_introvert.valueChanged.connect(self.setIntrovertLevel)
		self.slider_introvert.setRange(-5,5)

		self.slider_stress = QSlider(Qt.Horizontal, self)
		self.slider_stress.valueChanged.connect(self.setStressLevel)
		self.slider_stress.setRange(-5,5)

		# Test decision button
		self.button_decide = QPushButton('DECIDE', self)
		self.button_decide.resize(self.button_decide.sizeHint())
		self.button_decide.move(100,50)
		self.button_decide.clicked.connect(self.buttonClicked)

		# Output display
		self.result_str = "Select some parameters and hit 'DECIDE'"
		self.result_display = QLabel(self.result_str, self)

		# Quit button
		self.button_quit = QPushButton('QUIT', self)
		self.button_quit.resize(self.button_quit.sizeHint())
		self.button_quit.move(100,100)
		self.button_quit.clicked.connect(QApplication.instance().quit)

		# Set up central widget and layout
		self.vbox = QVBoxLayout()
		self.central = QWidget(self)
		self.setCentralWidget(self.central)
		self.vbox.addWidget(self.slider_hunger)
		self.vbox.addWidget(self.slider_thirst)
		self.vbox.addWidget(self.slider_energy)
		self.vbox.addWidget(self.slider_introvert)
		self.vbox.addWidget(self.slider_stress)
		self.vbox.addWidget(self.button_decide)
		self.vbox.addWidget(self.result_display)
		self.vbox.addWidget(self.button_quit)
		self.central.setLayout(self.vbox)

		# Window properties
		self.setGeometry(300, 300, 300, 220)
		window_geom = self.frameGeometry()
		center_pos = QDesktopWidget().availableGeometry().center()
		window_geom.moveCenter(center_pos)
		self.move(window_geom.topLeft())
		self.setWindowTitle('DecisionMaker')
		self.setWindowIcon(QIcon('icon.png'))

		# Show window
		self.show()

	# Setters for parameter values, triggered by changing front panel controls
	def setHungerLevel(self, level):
		self.hunger_level = level
	def setThirstLevel(self, level):
		self.thirst_level = level
	def setEnergyLevel(self, level):
		self.energy_level = level
	def setIntrovertLevel(self, level):
		self.introvert_level = level
	def setStressLevel(self, level):
		self.stress_level = level

	# Button event handler
	def buttonClicked(self):
		sender = self.sender()
		if (sender == self.button_decide):
			# Construct Parameters and make a decision
			p = Parameters(*tuple([1]*len(Parameter_Fields)))
			self.result_str = "YOU SHOULD: {}".format(self.decision_maker.choose(p))
			self.result_display.setText(self.result_str)

if __name__ == '__main__':
	# Create app
	app = QApplication(sys.argv)

	# Create window widget
	w = DecisionMakerWindow()

	# Start event handling
	sys.exit(app.exec_())