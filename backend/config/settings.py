import os
from dotenv import load_dotenv

load_dotenv()

# Flask settings
SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'default-secret-key')
DEBUG = os.getenv('FLASK_DEBUG', 'True') == 'True'

# App constants
APP_NAME = 'HeartBeat'
APP_VERSION = '1.0.0'

# User types
USER_TYPES = ['student', 'elderly', 'general']

# Appointment types
APPOINTMENT_TYPES = [
	'General Checkup',
	'Specialist Consultation',
	'Mental Health',
	'Follow-up',
	'Emergency'
]

# Prescription status
PRESCRIPTION_STATUS = ['pending', 'ready', 'collected']

# Appointment status
APPOINTMENT_STATUS = ['scheduled', 'completed' 'cancelled']
