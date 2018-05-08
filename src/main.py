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
import ctypes
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, \
	QDesktopWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSlider, \
	QGridLayout, QLabel, QFrame, QCalendarWidget, QComboBox, QLayout
from PyQt5.QtGui import QIcon, QPixmap, QPalette
from DecisionMaker import *

# Constants
DEFAULT_DB_PATH = '../data/Possibilities.csv'
TITLE_IMAGE_PATH = '../res/DecisionMaker.png'
ICON_PATH = '../res/icon.png'
AUTHOR = 'Dylan Everingham'
VERSION = '0.0.1'

LOAD_ANIM_FRAME_NUM = 20
LOAD_ANIM_FRAME_DELAY = 100

# Makes the taskbar icon work (thanks StackOverflow)
appid = 'decisionmaker.0.0.1'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

# DecisionMakerWindow class
# Defines QtWidget representing DecisionMaker GUI window
class DecisionMakerWindow(QMainWindow):
	# DecisionMakerWindow class constructor
	def __init__(self):
		# Call supercalss constructor
		super().__init__()

		# Initialize backend
		self.decision_maker = DecisionMaker(DEFAULT_DB_PATH)

		# These parameter values get adjusted by the front panel controls
		self.day = 0
		self.year = 0
		self.time = 0
		self.weather = 0
		self.alone = 0
		self.retrograde = 0
		self.hunger_level = 0
		self.thirst_level = 0
		self.energy_level = 0
		self.introvert_level = 0
		self.stress_level = 0
		
		# Status bar
		#self.statusBar().showMessage('Ready')

		# Menu bar
		#menu_bar = self.menuBar()
		#file_menu = menu_bar.addMenu('&File')

		# Set up layout
		vbox = QVBoxLayout()
		title = DecisionMakerTitle()
		controls = DecisionMakerControls(self)
		output = DecisionMakerOutput(self)
		vbox.addWidget(title)
		vbox.addWidget(controls)
		vbox.addWidget(output)
		vbox.insertStretch(1)
		vbox.insertStretch(3)
		vbox.setSpacing(10)
		vbox.addSpacing(10)

		hbox = QHBoxLayout()
		hbox.addLayout(vbox)
		hbox.insertStretch(0)

		central = QWidget(self)
		self.setCentralWidget(central)
		central.setLayout(hbox)

		# Color palette
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(self.backgroundRole(), Qt.black)
		self.setPalette(palette)

		# Window properties
		#self.setGeometry(300, 600, 300, 220)
		#window_geom = self.frameGeometry()
		#center_pos = QDesktopWidget().availableGeometry().center()
		#window_geom.moveCenter(center_pos)
		#self.move(window_geom.topLeft())
		self.setWindowTitle('DecisionMaker')
		self.setWindowIcon(QIcon(ICON_PATH))

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
	def setDay(self, day):
		self.day = day
	def setYear(self, year):
		self.year = year
	def setTime(self, time):
		self.time = time
	def setWeather(self, weather):
		self.weather = weather
	def setAlone(self, alone):
		self.alone = alone
	def setRetrograde(self, retrograde):
		self.retrograde = retrograde

# DecisionMakerTitle class definition
# Widget conatining application title bar
class DecisionMakerTitle(QWidget):
	# DecisionMakerTitle class constructor
	def __init__(self):
		# Call superclass constructor
		super().__init__()

		# Title image
		title_image = QLabel()
		pixmap = QPixmap(TITLE_IMAGE_PATH)
		title_image.setPixmap(pixmap)
		title_image.setAlignment(Qt.AlignLeft | Qt.AlignBottom)

		# Author
		title_author = QLabel(AUTHOR, self)

		# Version
		title_version = QLabel(VERSION, self)

		# Set up layout
		vbox = QVBoxLayout()
		vbox.addWidget(title_image)
		vbox.addWidget(title_author)
		vbox.addWidget(title_version)
		hbox = QHBoxLayout()
		hbox.insertStretch(0)
		hbox.addLayout(vbox)

		self.setLayout(hbox)

# DecisionMakerControls class definition
# Widget containing all input controls for DecisionMaker
class DecisionMakerControls(QWidget):
	# DecisionMakerControls class constructor
	def __init__(self, parent):
		# Call superclass constructor
		super().__init__()

		# Save parent instance
		self.parent = parent

		# Slider box
		slider_box = QVBoxLayout()
		slider_box.addWidget(DecisionMakerSlider('How hungry are you?', parent.setHungerLevel))
		slider_box.addWidget(DecisionMakerSlider('Thirsty?', parent.setThirstLevel))
		slider_box.addWidget(DecisionMakerSlider('Energy level?', parent.setEnergyLevel))
		slider_box.addWidget(DecisionMakerSlider('Introversion level?', parent.setIntrovertLevel))
		slider_box.addWidget(DecisionMakerSlider('Stress level?', parent.setStressLevel))

		# Box containing calendar control, time control, weather control, alone toggle and retrograde toggle
		right_box = QVBoxLayout()

		# Box containing all of the above minus calendar
		#lowerright_box = QHBoxLayout()

		# Box containing labels for contorl in lower right box
		#lowerright_label_box = QVBoxLayout()

		# Box containing controls in lower right box
		#lowerright_control_box = QVBoxLayout()

		# Calendar control
		self.calendar = QCalendarWidget()
		self.calendar.setHorizontalHeaderFormat(QCalendarWidget.SingleLetterDayNames)
		self.calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
		self.calendar.selectionChanged.connect(self.calendarChanged)
		self.calendar.setFixedWidth(325)
		right_box.addWidget(self.calendar)

		# Save today's date
		self.today = self.calendar.selectedDate()

		# Initialize day and year
		self.parent.setDay(self.today.dayOfWeek() - 1)

		# Limit year to +- 100 form current
		year = self.today.year()
		if (year > 100):
			year = 100
		elif (year < -100):
			year = -100

		self.parent.setYear(year)

		# Time control
		time_box = QHBoxLayout()
		time_label = QLabel('What time is it?', self)
		self.time_combo = QComboBox()
		self.time_combo.addItems(
			['1:00', '2:00', '3:00', '4:00', '5:00', '6:00', \
			'7:00', '8:00', '9:00', '10:00', '11:00', '12:00' ]
		)
		hour = QTime.currentTime().hour() - 1
		hour_convert = hour
		if (hour_convert < 0):
			hour_convert = 23
		if (hour_convert > 12):
			hour_convert -= 12
		self.time_combo.setCurrentIndex(hour_convert)
		self.time_combo.currentIndexChanged.connect(self.comboChanged)

		self.ampm_combo = QComboBox()
		self.ampm_combo.addItems(['AM', 'PM'])
		if (hour > 12):
			self.ampm_combo.setCurrentIndex(1)
		else:
			self.ampm_combo.setCurrentIndex(0)
		self.ampm_combo.currentIndexChanged.connect(self.comboChanged)

		self.parent.setTime(hour)

		time_box.addWidget(time_label)
		time_box.addWidget(self.time_combo)
		time_box.addWidget(self.ampm_combo)
		right_box.addLayout(time_box)

		# Weather control
		weather_box = QHBoxLayout()
		weather_label = QLabel('What\'s the weather like?', self)
		self.weather_combo = QComboBox()
		self.weather_combo.addItems(['Sunny', 'Cloudy', 'Raining', 'Snowing', 'Natural Disaster'])
		self.weather_combo.currentIndexChanged.connect(self.comboChanged)
		weather_box.addWidget(weather_label)
		weather_box.addWidget(self.weather_combo)
		right_box.addLayout(weather_box)

		# Alone toggle button
		alone_box = QHBoxLayout()
		alone_label = QLabel('Are you alone, or with someone else?', self)
		self.button_alone = QPushButton('Alone')
		self.button_alone.setCheckable(True)
		self.button_alone.clicked.connect(self.buttonClicked)
		alone_box.addWidget(alone_label)
		alone_box.addWidget(self.button_alone)
		right_box.addLayout(alone_box)

		# Retrograde toggle button
		retrograde_box = QHBoxLayout()
		retrograde_label = QLabel('Is Mercury in retrograde?', self)
		self.button_retrograde = QPushButton('Nope')
		self.button_retrograde.setCheckable(True)
		self.button_retrograde.clicked.connect(self.buttonClicked)
		retrograde_box.addWidget(retrograde_label)
		retrograde_box.addWidget(self.button_retrograde)
		right_box.addLayout(retrograde_box)

		# Color palette
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(self.backgroundRole(), Qt.white)
		self.setPalette(palette)

		# Set up layout
		hbox = QHBoxLayout()
		hbox.addLayout(slider_box)
		hbox.insertSpacing(1, 25)
		hbox.addLayout(right_box)
		hbox.setSizeConstraint(QLayout.SetFixedSize)
		self.setLayout(hbox)

	# Button event handler
	def buttonClicked(self):
		sender = self.sender()
		if (sender == self.button_alone):
			if (self.button_alone.isChecked()):
				self.button_alone.setText('With someone else')
				self.parent.setAlone(1)
			else:
				self.button_alone.setText('Alone')
				self.parent.setAlone(0)
		elif (sender == self.button_retrograde):
			if (self.button_retrograde.isChecked()):
				self.button_retrograde.setText('Maybe?')
				self.parent.setRetrograde(1)
			else:
				self.button_retrograde.setText('Nope')
				self.parent.setRetrograde(0)

	# Cobobox event handler
	def comboChanged(self):
		sender = self.sender()
		if ((sender == self.time_combo) or (sender == self.ampm_combo)):
			hour = self.time_combo.currentIndex() + 1
			if (hour == 13):
				hour = 0
			time = (hour + 12 * self.ampm_combo.currentIndex())
			self.parent.setTime(time)
		if (sender == self.weather_combo):
			self.parent.setWeather(self.weather_combo.currentIndex())

	# Calendar event handler
	def calendarChanged(self):
		sender = self.sender()
		if (sender == self.calendar):
			date = self.calendar.selectedDate()
			self.parent.setDay(date.dayOfWeek() - 1)
			year = date.year()

			# Limit year to +- 100 form current
			year = year - self.today.year()
			if (year > 100):
				year = 100
			elif (year < -100):
				year = -100

			self.parent.setYear(year)


# DecisionMakerOutput class definition
# Widget containing DecisionMaker output box
class DecisionMakerOutput(QWidget):
	# DecisionMakerOutput class constructor
	def __init__(self, parent):
		# Call superclass constructor
		super().__init__()

		# Save parent instance
		self.parent = parent

		# Box containing display button
		leftbox = QHBoxLayout()

		# Decide button
		self.button_decide = QPushButton('DECIDE', self)
		self.button_decide.clicked.connect(self.buttonClicked)
		self.button_decide.setFixedWidth(225)
		leftbox.addWidget(self.button_decide)

		# Box conatining output display and label
		rightbox = QHBoxLayout()

		# Result label
		result_label = QLabel('What should you do?:', self)
		result_label.setAlignment(Qt.AlignRight | Qt.AlignCenter)
		rightbox.addWidget(result_label)

		# Result display
		result_str = "Select some parameters and hit 'DECIDE'"
		self.result_display = QLabel(result_str, self)
		self.result_display.setAlignment(Qt.AlignCenter)
		self.result_display.setFrameStyle(QFrame.Panel | QFrame.Sunken)
		self.result_display.setLineWidth(3)
		self.result_display.setFixedWidth(300)
		rightbox.addWidget(self.result_display)

		# Animation timer
		self.anim_timer = QTimer()
		self.anim_timer.timeout.connect(self.doOutput)
		self.frame_count = 0

		# Color palettes
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(self.backgroundRole(), Qt.white)
		self.setPalette(palette)

		# Set up layout
		hbox = QHBoxLayout()
		hbox.addLayout(leftbox)
		hbox.insertSpacing(1,57)
		hbox.addLayout(rightbox)
		hbox.setSizeConstraint(QLayout.SetFixedSize)
		self.setLayout(hbox)

	# Function to do loading animation
	def doOutput(self):
		if (self.frame_count > LOAD_ANIM_FRAME_NUM):
			# Construct Parameters and make a decision
			params = Parameters(*tuple(
				[self.parent.day, \
				 self.parent.year, \
				 self.parent.time, \
				 self.parent.weather, \
				 self.parent.alone, \
				 self.parent.hunger_level, \
				 self.parent.thirst_level, \
				 self.parent.energy_level, \
				 self.parent.introvert_level, \
				 self.parent.stress_level, \
				 self.parent.retrograde]
			))

			# Get decision
			result_str = "{}".format(self.parent.decision_maker.choose(params))

			# Display result
			self.result_display.setText(result_str)

			# Reset animation frame counter and stop timer
			self.frame_count = 0
			self.anim_timer.stop()

		# Do loading animation
		elif(self.frame_count % 4 == 0):
			self.result_display.setText('/ CALCULATING... /')

		elif(self.frame_count % 4 == 1):
			self.result_display.setText('| CALCULATING... |')

		elif(self.frame_count % 4 == 2):
			self.result_display.setText('\ CALCULATING... \\')

		else:
			self.result_display.setText('-- CALCULATING... --')

		# Increment animation frame counter
		self.frame_count += 1

	# Button event handler
	def buttonClicked(self):
		sender = self.sender()
		if (sender == self.button_decide):
			# Start loading animation, will display decisoin when finished
			self.anim_timer.start(LOAD_ANIM_FRAME_DELAY)

# DecisionMakerSlider class definition
# Widget conatining slider and labels
class DecisionMakerSlider(QWidget):
	# DecisionMakerSlider class constructor
	def __init__(self, name, update_func):
		# Call superclass constructor
		super().__init__()

		# Create labels
		slider_label_min = QLabel('-5', self)
		slider_label_min.setAlignment(Qt.AlignLeft)
		slider_label_max = QLabel('5', self)
		slider_label_max.setAlignment(Qt.AlignRight)

		slider_label = QLabel(name, self)
		slider_label.setAlignment(Qt.AlignCenter)

		# Create slider
		slider = QSlider(Qt.Horizontal, self)
		slider.valueChanged.connect(update_func)
		slider.setRange(-5,5)
		slider.setTickPosition(QSlider.TicksAbove)
		slider.setFixedWidth(325)

		# Set up layout
		hbox = QHBoxLayout()
		hbox.addWidget(slider_label_min)
		hbox.addWidget(slider_label)
		hbox.addWidget(slider_label_max)

		vbox = QVBoxLayout()
		vbox.addLayout(hbox)
		vbox.addWidget(slider)
		self.setLayout(vbox)

# Run app
if __name__ == '__main__':
	# Create app
	app = QApplication(sys.argv)

	# Create window widget
	w = DecisionMakerWindow()

	# Start event handling
	sys.exit(app.exec_())