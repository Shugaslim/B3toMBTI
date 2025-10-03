import pandas as pd
import numpy as np

class PersonalityConverter:
    def __init__(self):
        self.func2num = {'ne': 1, 'se': 2, 'te': 3, 'fe': 4, 'ti': 5, 'fi': 6, 'si': 7, 'ni': 8}
        self.extrosign2func = {
            'Aries': ['se', 'te'],
            'Leo': ['se', 'fe'],
            'Sagittarius': ['ne', 'te'],
            'Gemini': ['ne', 'te'],
            'Libra': ['se', 'fe'],
            'Aquarius': ['ne', 'te'],
            'Cancer': ['ne', 'fe'],
            'Scorpio': ['ne', 'fe'],
            'Pisces': ['ne', 'fe'],
            'Taurus': ['se', 'fe'],
            'Virgo': ['se', 'te'],
            'Capricorn': ['se', 'te']
        }
        self.introsign2func = {
            'Aries': ['ti', 'si'],
            'Leo': ['ti', 'si'],
            'Sagittarius': ['ti', 'ni'],
            'Gemini': ['ti', 'si'],
            'Libra': ['ti', 'si'],
            'Aquarius': ['fi', 'si'],
            'Cancer': ['fi', 'ni'],
            'Scorpio': ['fi', 'ni'],
            'Pisces': ['fi', 'ni'],
            'Taurus': ['fi', 'si'],
            'Virgo': ['ti', 'si'],
            'Capricorn': ['fi', 'si']
        }
        self.sun_matrix = { 'J': np.array([[0, 0], [0,1]]),
                       'P': np.array([[1, 0], [0,0]])
        }

        self.sun_mappings = {
            'Aries': self.sun_matrix['J'],
            'Leo': self.sun_matrix['P'],
            'Sagittarius': self.sun_matrix['P'],
            'Gemini': self.sun_matrix['P'],
            'Libra': self.sun_matrix['J'],
            'Aquarius': self.sun_matrix['J'],
            'Cancer': self.sun_matrix['J'],
            'Scorpio': self.sun_matrix['P'],
            'Pisces': self.sun_matrix['P'],
            'Taurus': self.sun_matrix['J'],
            'Virgo': self.sun_matrix['J'],
            'Capricorn': self.sun_matrix['J']
        }

        self.extromapping = {
            'Aries': 1,
            'Leo': 1,
            'Sagittarius': 1,
            'Gemini': 1,
            'Libra': 1,
            'Aquarius': 1,
            'Cancer': -1,
            'Scorpio': -1,
            'Pisces': -1,
            'Taurus': -1,
            'Virgo': -1,
            'Capricorn': -1
        }

        self.num2mbti = {
            5: 'ENTP',
            6: 'ENFP',
            10: 'ESTP',
            12: 'ESFP',
            21: 'ESTJ',
            24: 'ENTJ',
            28: 'ESFJ',
            32: 'ENFJ',
            -5: 'INTP',
            -6: 'INFP',
            -10: 'ISTP',
            -12: 'ISFP',
            -21: 'ISTJ',
            -24: 'INTJ',
            -28: 'ISFJ',
            -32: 'INFJ'
        }
    def convert(self, data):
        rs = data["Rising"]
        ss = data["Sun"]
        ms = data["Moon"]

        #Grabbing extroverison vale
        extro_val = self.extromapping[rs]

        #Grabbing functions
        extro_funcs = self.extrosign2func[rs]
        e_num = [self.func2num[f] for f in extro_funcs]
        intro_funcs = self.introsign2func[ms]
        i_num = [self.func2num[f] for f in intro_funcs]

        #Grabbing sun matrix
        sun_matrix = self.sun_mappings[ss]

        #Calculating function stack
        calc = np.matmul(sun_matrix, e_num)
        funcnum = np.dot(calc, i_num)
        fin_num = funcnum * extro_val
        mbti = self.num2mbti[fin_num]
        return mbti