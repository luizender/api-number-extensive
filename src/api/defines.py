"""This module has the settings of project

"""

# -*- coding: utf-8 -*-

import os

# General defines of API
LOGGING_FILE = os.path.join(os.path.dirname(__file__), 'logging.json')

# Limits
MAX_NUMBER_SUPPORT = 99999
MIN_NUMBER_SUPPORT = -99999

# Numbers in extensive form
NUMBER_EXTENSIVE = [
    [
        'zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez'
    ],
    [
        'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove'
    ],
    [
        None, None, 'vinte', 'trinta', 'quarenta', 'cinquenta',
        'sessenta', 'setenta', 'oitenta', 'noventa'
    ],
    [
        None, 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos',
        'seiscentos', 'setecentos', 'oitocentos', 'novecentos'
    ]
]
UNIT_EXTENSIVE = [
    None, 'mil'
]
