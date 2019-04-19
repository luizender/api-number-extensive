"""
This module has the settings of project
"""

import os

# General configuration of API
LOGGING_FILE = os.path.join(os.path.dirname(__file__), 'logging.json')
MAX_NUMBER_SUPPORT = int(os.environ.get('MAX_NUMBER_SUPPORT', '99999'))
MIN_NUMBER_SUPPORT = int(os.environ.get('MIN_NUMBER_SUPPORT', '-99999'))
