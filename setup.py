from setuptools import setup

APP = ['Timer.py']
DATA_FILES = []
OPTIONS = {
	'iconfile': 'timer.icns',
	'argv_emulation': True, 
	'packages': ['pyttsx3'],
	'includes': ['time', 'tkinter', 'pyttsx3']
}

setup(
	app=APP,
	data_files=DATA_FILES,
	options={'py2app': OPTIONS},
	setup_requires=['py2app'],
)
