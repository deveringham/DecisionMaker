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
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QPushButton, QSlider, QGridLayout
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
		self.decision_maker = DecisionMaker('possibilities.txt')
		min_params = Parameters(*tuple([[0] for f in Parameter_Fields]))
		max_params = Parameters(*tuple([[0] for f in Parameter_Fields]))
		param_weights = Parameters(*tuple([[0] for f in Parameter_Fields]))
		possibility = Possibility(min_params, max_params, param_weights, 1.0, 'Give Dylan another chance.')
		self.decision_maker.addPossibility(possibility)
		
		# Initialize UI elements
		# Window properties
		self.setGeometry(300, 300, 300, 220)
		window_geom = self.frameGeometry()
		center_pos = QDesktopWidget().availableGeometry().center()
		window_geom.moveCenter(center_pos)
		self.move(window_geom.topLeft())
		self.setWindowTitle('DecisionMaker')
		self.setWindowIcon(QIcon('icon.png'))

		# Status bar
		self.statusBar().showMessage('Ready')

		# Menu bar
		menu_bar = self.menuBar()
		file_menu = menu_bar.addMenu('&File')

		# Quit button
		button_quit = QPushButton('Quit', self)
		button_quit.resize(button_quit.sizeHint())
		button_quit.move(100,100)
		button_quit.clicked.connect(QApplication.instance().quit)

		# Show window
		self.show()

if __name__ == '__main__':
	# Create app
	app = QApplication(sys.argv)

	# Create window widget
	w = DecisionMakerWindow()

	# Start event handling
	sys.exit(app.exec_())

	while True:
		print('Running...')
		time.sleep(1)