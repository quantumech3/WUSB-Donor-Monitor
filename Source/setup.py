from distutils.core import setup

setup(
    name='Source',
    version='1.0',
    packages=[''],
    url='',
    license='Copyright',
    author='Scott Burgert',
    author_email='quantumech3@gmail.com',
    description='People who help run the WUSB Radiothon currently don\'t have an easy and accessible way to efficiently view information about the WUSB Radiothon. This program allows anyone working for WUSB to get near real time access to current information regarding a Radiothon.',
    install_requires=['gspread', 'oauth2client', 'Flask', 'eventlet', 'Flask-SocketIO']
)
