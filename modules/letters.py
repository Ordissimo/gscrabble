# -*- coding: utf-8 -*-

##############################################################################
#a########  "قُلۡ بِفَضلِ ٱللَّهِ وَبِرَحمَتِهِۦ فَبِذَٰلِكَ فَليَفرَحُواْ هُوَ خَيرُُ مِّمَّا يَجمَعُونَ"  ########
##############################################################################

from araby import *

COMPLEX_LETTERS = {
    'en': {}, 'ar': {}, 'ru': {}, 'fi': {}, 'fr': {}, 'de': {}, 'hy': {}, 'af': {}, 'ang': {}, 'bm': {}, 'sr': {}, 'eu': {}, 'bg': {},
    'cs': {},  'da': {},  'nl': {},  'eo': {}, 'et': {}, 'gl': {}, 'el': {}, 'is': {}, 'id': {}, 'ga': {}, 'it': {}, 'hira': {}, 'romaji': {}, 'la': {},
    'lv': {}, 'lt': {}, 'mg': {}, 'math': {}, 'no': {}, 'pl': {}, 'pt': {}, 'ro': {}, 'sk': {}, 'sl': {}, 'sv': {}, 'tn': {}, 'tr': {}, 'uk': {}, 'bopo': {}, 'ms': {},
    #----------------------------------------------
    'hu': {'4': 'CS', '1': 'SZ', '5': 'LY', '7': 'TY', '6': 'ZS', '2': 'GY', '3': 'NY'},
    'cy': {'4': 'CH', '1': 'DD', '5': 'LL', '7': 'RH', '6': 'NG', '2': 'FF', '3': 'TH'},
    'hr': {'1': 'LJ', '3': 'DŽ', '2': 'NJ'},
    'ht': {'1': 'OU', '3': 'UI', '2': 'CH'},
    'es': {'1': 'LL',  '2': 'RR'},
    'bcl': {'1': 'NG'},
    'br': {'1': 'ZH', '2': 'CH', '3': "C'H"},
    'ca': {'1': 'L·L', '2': 'NY'},
    }

DICT_LETTERS  = {
    'ar': arbic_letters,
    
    
    'es': {"*": (2,0), 'A': (11,1), "B": (3,3), "C": (4,2), "D": (4,2), "E": (11,1), "F": (2,4), "G": (2,2), "H": (2,4), "I": (6,1), "J": (2,5), "K": (1,8), "Ñ": (1,8), 
           "L": (4,1), "1": (1,8), "M": (3,3), "N": (5,1), "O": (8,1), "P": (2,3), "Q": (1,8), "R": (4,1), "2": (1,8), "S": (7,1), "T": (4,1), "U": (5,1), "V": (2,4),
           "W": (1,8), "X": (1,8), "Y": (1,4), "Z": (1,10)},
                 
                 
    'de': {"*": (2,0), "A": (5,1), "B": (2,3), "C": (2,4), "D": (4,1), "E": (15,1), "F": (2,4), "G": (3,2), "H": (4,2), "I": (6,1), "J": (1,6), "K": (2,4), 
           "L": (3,2), "M": (4,3), "N": (9,1), "O": (3,2), "P": (1,4), "Q": (1,10), "R": (6,1), "S": (7,1), "T": (6,1), "U": (6,1), "V": (1,6),
           "W": (1,3), "X": (1,8), "Y": (1,10), "Z": (1,3), "Ü": (1,6), "Ä": (1,6), "Ö": (1,8)},
                 
                 
    'en': {"*": (2,0), 'A': (9,1), "B": (2,3), "C": (2,3), "D": (4,2), "E": (12,1), "F": (2,4), "G": (3,2), "H": (2,4), "I": (9,1), "J": (1,8), "K": (1,5),
           "L": (4,1), "M": (2,3), "N": (6,1), "O": (8,1), "P": (2,3), "Q": (1,10), "R": (6,1), "S": (4,1), "T": (6,1), "U": (4,1), "V": (2,4),
           "W": (2,4), "X": (1,8), "Y": (2,4), "Z": (1,10)},
                 
                 
    'fi': {"*": (2,0), "A": (10,1), "B": (1,8), "C": (1,10), "D": (1,7), "E": (8,1), "F": (1,8), "G": (1,8), "H": (2,4), "I": (10,1), "J": (2,4), "K": (5,2),
           "L": (5,2), "M": (3,3), "N": (9,1), "O": (5,2), "P": (2,4), "R": (2,4), "S": (7,1), "T": (9,1), "U": (4,3), "V": (2,4), "Y": (2,4),
           "Ä": (5,2), "Ö": (1,7)},
                 
                 
    'fr': {"*": (2,0), "A": (9,1), "B": (2,3), "C": (2,3), "D": (3,2), "E": (15,1), "F": (2,4), "G": (2,2), "H": (2,4), "I": (8,1), "J": (1,8), "K": (1,10),
           "L": (5,1), "M": (3,3), "N": (6,1), "O": (6,1), "P": (2,3), "Q": (1,8), "R": (6,1), "S": (6,1), "T": (6,1), "U": (6,1), "V": (2,4),
           "W": (1,10), "X": (1,10), "Y": (1,10), "Z": (1,10)},
                 
                 
    'sr': {"*": (2,0), "А": (13,1), "Б": (2,4), "В": (4,1), "Г": (2,3), "Д": (4,1), "Ђ": (1,10), "Е": (10,1), "Ж": (1,8), "З": (2,3), "И": (11,1), "Ј": (3,2),
           "К": (4,1), "Л": (3,2), "Љ": (8,1), "М": (4,2), "Н": (7,1), "Њ": (1,6), "О": (10,1), "П": (3,2), "Р": (6,1), "С": (6,1), "Т": (5,1),
           "Ћ": (1,7), "У": (5,1), "Ф": (1,10), "Х": (1,7), "Ц": (1,6), "Ч": (1,5), "Џ": (1,10), "Ш": (1,5)},
                 
                 
    'ru': {'*': (2, 0), "О" : (10,1), "А" : (8,1), "Е" : (8,1), "И" : (5,1), "Н" : (5,1), "Р" : (5,1), "С" : (5,1), "Т" : (5,1), "В" : (4,1), "Д" : (4,2), "К" : (4,2), "Л" : (4,2), 
           "П" : (4,2), "У" : (4,2), "М" : (3,2), "Б" : (2,3), "Г" : (2,3), "Ь" : (2,3), "Я" : (2,3), "Ë" : (1,3),  "Ы" : (2,4), "Й" : (1,4), 
            "З" : (2,5), "Ж" : (1,5), "Х" : (1,5), "Ц" : (1,5), "Ч" : (1,5), "Ш" : (1,8), "Э" : (1,8), "Ю" : (1,8), "Ф" : (1,10),"Щ" : (1,10),"Ъ" : (1,10)},
                 
                 
    'hy': {'*': (3, 0), 'Դ': (3, 3), 'Ք': (3, 3), 'Ս': (6, 1), 'Ը': (1, 10), 'Ւ': (5, 2), 'Է': (4, 2), 'Ո': (8, 1), 'Ռ': (2, 4), 'Տ': (5, 2), 'Յ': (4, 2), 'Ճ': (1, 6), 'Ի': (10, 1), 'Ձ': (1, 8), 
           'Խ': (2, 4), 'Ա': (18, 1), 'Լ': (4, 3), 'Վ': (2, 3), 'Զ': (1, 6), 'Շ': (2, 4), 'Փ': (1, 8), 'Ֆ': (1, 10), 'Ջ': (1, 6), 'Թ': (2, 5), 'Ղ': (2, 5), 'Բ': (3, 3), 
           'Ր': (5, 2), 'Կ': (7, 1), 'Մ': (4, 2), 'Չ': (1, 6), 'Հ': (4, 2), 'Գ': (3, 3), 'Ց': (2, 5), 'Ե': (10, 1), 'Ն': (7, 1), 'Օ': (1, 8), 'Ժ': (1, 8), 'Ծ': (2, 5), 'Պ': (4, 2)},
                 
                 
    'af': {'*': (2, 0), 'V': (2, 5), 'I': (8, 1), 'B': (1, 8), 'N': (8, 1), 'R': (6, 1), 'L': (3, 2), 'O': (6, 1), 'J': (1, 10), 'A': (9, 1), 'P': (2, 5), 'G': (4, 2), 'D': (6, 1), 
           'T': (6, 1), 'H': (3, 2), 'K': (3, 3), 'F': (1, 8), 'W': (3, 3), 'U': (2, 4), 'E': (16, 1), 'Y': (2, 4), 'M': (2, 4), 'S': (6, 1)},
                 
                 
    'ang': {'*': (2, 0), 'S': (5, 1), 'W': (3, 2), 'Ð': (2, 4), 'P': (1, 8), 'T': (3, 2), 'E': (14, 1), 'C': (3, 3), 'D': (5, 1), 'L': (4, 1), 'Æ': (3, 3), 'Þ': (2, 4), 'X': (1, 10), 'M': (3, 2), 
            'I': (4, 1), 'Y': (2, 4), 'A': (8, 1), 'B': (1, 5), 'N': (9, 1), 'O': (6, 1), 'G': (4, 1), 'F': (3, 2), 'R': (6, 1), 'U': (3, 3), 'H': (4, 1)},
                 
                 
    'bm': {'*': (2, 0), 'T': (2, 3), 'U': (5, 2), 'F': (2, 4), 'Ɔ': (3, 3), 'Y': (4, 2), 'H': (1, 10), 'P': (1, 10), 'D': (2, 3), 'K': (6, 1), 'G': (2, 4), 'Ɲ': (1, 8), 'E': (6, 1), 
           'Z': (1, 10), 'Ɛ': (6, 1), 'R': (3, 2), 'W': (2, 4), 'N': (6, 1), 'S': (4, 2), 'L': (6, 1), 'B': (5, 1), 'M': (5, 1), 'O': (6, 1), 'C': (1, 8), 'I': (6, 1), 'J': (2, 8), 'A': (15, 1), 'Ŋ': (1, 10)},
                 
                 
    'eu': {'*': (2, 0), 'R': (1, 8), 'S': (2, 5), 'N': (8, 1), 'J': (1, 8), 'G': (2, 5), 'M': (1, 8), 'T': (1, 8), 'P': (1, 8), 'E': (12, 1), 'K': (5, 2), 'A': (14, 1), 'D': (4, 3), 
           'Z': (3, 4), 'I': (9, 1), 'O': (6, 1), 'H': (2, 5), 'F': (1, 10), 'U': (6, 1), 'B': (3, 4), 'X': (1, 10), 'L': (2, 5)},
                 
                 
    'bcl': {'*': (2, 0), 'K': (3, 2), 'O': (8, 1), 'E': (2, 8), 'H': (2, 8), 'U': (5, 1), 'G': (4, 2), 'W': (2, 5), 'Y': (2, 5), 'L': (3, 3), 'B': (3, 4), 'I': (12, 1), '1': (6, 3), 'M': (5, 1), 
            'R': (3, 2), 'S': (5, 1), 'P': (3, 3), 'A': (16, 1), 'D': (3, 4), 'T': (5, 1), 'N': (8, 1)},
                 
                 
    'br': {'*': (2, 0), 'S': (3, 3), 'O': (6, 1), 'B': (2, 4), 'G': (3, 3), 'F': (1, 10), 'J': (1, 10), 'A': (12, 1), 'W': (1, 10), 'K': (2, 4), 'R': (7, 1), 'I': (4, 1), 'N': (9, 1), 'Y': (1, 10), 
           'M': (2, 4), 'U': (5, 1), 'V': (3, 3), '2': (1, 4), '3': (1, 4), 'L': (4, 1), 'D': (4, 2), 'T': (5, 1), 'H': (2, 3), 'P': (1, 5), 'E': (14, 1), 'Z': (2, 4), '1': (2, 4)},
                 
                 
    'bg': {'*': (2, 0), 'Ц': (1, 8), 'Щ': (1, 10), 'П': (4, 1), 'Т': (5, 1), 'Р': (4, 1), 'Д': (4, 2), 'Ж': (2, 4), 'С': (4, 1), 'Ш': (1, 8), 'К': (3, 2), 'Б': (3, 2), 'З': (2, 4), 'В': (4, 2), 
           'Н': (4, 1), 'Г': (3, 3), 'А': (9, 1), 'И': (8, 1), 'Ч': (2, 5), 'Ь': (1, 10), 'Х': (1, 5), 'Ю': (1, 8), 'О': (9, 1), 'Л': (3, 2), 'Ъ': (2, 3), 'Е': (8, 1), 'М': (4, 2), 
           'Й': (1, 5), 'Ф': (1, 10), 'У': (3, 5), 'Я': (2, 5)},
                 
                 
    'ca': {'*': (2, 0), 'M': (3, 2), 'Ç': (1, 10), 'Z': (1, 8), 'Q': (1, 8), 'P': (2, 3), 'D': (3, 2), 'N': (6, 1), 'S': (8, 1), 'T': (5, 1), 'F': (1, 4), 'J': (1, 8), 'O': (5, 1), 'B': (2, 3), 
           'L': (4, 1), 'C': (3, 2), 'G': (2, 3), 'E': (13, 1), 'X': (1, 10), 'U': (4, 1), 'V': (1, 4), 'A': (12, 1), 'H': (1, 8), 'I': (8, 1), 'R': (8, 1), '1': (1, 10), '2': (1, 10)},
                 
                 
    'hr': {'*': (2, 0), 'B': (1, 3), 'U': (4, 1), 'T': (5, 1), '1': (1, 4), 'K': (3, 2), 'F': (1, 8), 'R': (5, 1), 'P': (3, 2), 'D': (3, 3), '3': (1, 10), 'I': (10, 1), 'Đ': (1, 10), 
           'V': (3, 2), 'G': (2, 3), 'Z': (2, 3), 'O': (9, 1), 'H': (1, 4), 'E': (9, 1), 'Ć': (1, 5), 'J': (4, 1), 'Č': (1, 3), 'N': (6, 1), '2': (1, 4), 'A': (11, 1), 'L': (2, 3), 
           'Ž': (1, 4), 'M': (3, 2), 'Š': (1, 4), 'C': (1, 4), 'S': (5, 1)},
                 
                 
    'cs': {'*': (2, 0), 'Ú': (1, 5), 'B': (2, 3), 'X': (1, 10), 'V': (4, 1), 'T': (4, 1), 'Y': (2, 2), 'K': (3, 1), 'F': (1, 5), 'R': (3, 1), 'P': (3, 1), 'Ť': (1, 7), 'D': (3, 1), 
           'I': (4, 1), 'Ý': (2, 4), 'U': (3, 2), 'Č': (1, 4), 'G': (1, 5), 'Z': (2, 2), 'O': (6, 1), 'H': (3, 2), 'Ř': (2, 4), 'E': (5, 1), 'Ó': (1, 7), 'Ů': (1, 4), 'J': (2, 2), 
           'Ě': (2, 3), 'N': (5, 1), 'Ď': (1, 8), 'A': (5, 1), 'É': (2, 3), 'L': (3, 1), 'Ž': (1, 4), 'M': (3, 2), 'Á': (2, 2), 'Í': (3, 2), 'Š': (2, 4), 'C': (3, 2), 'Ň': (1, 6), 'S': (4, 1)},
                 
                 
    'da': {'*': (2, 0), 'B': (4, 3), 'U': (3, 3), 'T': (5, 2), 'Y': (2, 4), 'K': (4, 3), 'F': (3, 3), 'R': (6, 1), 'P': (2, 4), 'Ø': (2, 4), 'D': (5, 2), 'S': (5, 2), 'V': (3, 3), 
           'G': (3, 3), 'Z': (1, 8), 'O': (5, 2), 'H': (2, 4), 'E': (9, 1), 'X': (1, 8), 'J': (2, 4), 'Å': (2, 4), 'N': (6, 1), 'A': (7, 1), 'L': (5, 2), 'M': (3, 3), 'Æ': (2, 4), 'C': (2, 8), 'I': (4, 3)},
                 
                 
    'nl': {'*': (2, 0), 'B': (2, 3), 'U': (3, 4), 'T': (5, 2), 'Y': (1, 8), 'K': (3, 3), 'F': (2, 4), 'R': (5, 2), 'P': (2, 3), 'D': (5, 2), 'I': (4, 1), 'V': (2, 4), 'G': (3, 3), 
           'Z': (2, 4), 'O': (6, 1), 'H': (2, 4), 'E': (18, 1), 'X': (1, 8), 'J': (2, 4), 'N': (10, 1), 'A': (6, 1), 'W': (2, 5), 'L': (3, 3), 'M': (3, 3), 'C': (2, 5), 'Q': (1, 10), 'S': (5, 2)},
                 
                 
    'eo': {'*': (2, 0), 'B': (2, 4), 'Ŭ': (1, 8), 'U': (4, 1), 'T': (4, 1), 'Ĥ': (1, 10), 'K': (4, 2), 'F': (2, 3), 'R': (6, 1), 'P': (3, 2), 'D': (3, 2), 'I': (8, 1), 'V': (2, 3), 
           'G': (2, 3), 'Z': (1, 5), 'O': (8, 1), 'H': (1, 8), 'E': (8, 1), 'Ĵ': (1, 10), 'Ĝ': (2, 3), 'J': (3, 2), 'N': (6, 1), 'A': (8, 1), 'L': (4, 1), 'Ŝ': (1, 4), 'M': (4, 2), 'Ĉ': (2, 4), 'C': (1, 4), 'S': (6, 1)},
                 
                 
    'et': {'*': (2, 0), 'B': (1, 4), 'U': (5, 1), 'T': (7, 1), 'K': (5, 1), 'F': (1, 8), 'R': (2, 2), 'P': (2, 4), 'D': (4, 2), 'I': (9, 1), 'V': (2, 3), 'G': (2, 3), 'Z': (1, 10), 
           'O': (5, 1), 'H': (2, 4), 'E': (9, 1), 'Õ': (2, 4), 'Ä': (2, 5), 'Ö': (2, 6), 'J': (2, 4), 'N': (4, 2), 'Ü': (2, 5), 'A': (10, 1), 'L': (5, 1), 'Ž': (1, 10), 'M': (4, 2), 'Š': (1, 10), 'S': (8, 1)},
                 
                 
    'gl': {'*': (2, 0), 'B': (2, 3), 'U': (3, 2), 'T': (4, 1), 'Y': (1, 9), 'K': (1, 8), 'F': (1, 5), 'Ñ': (1, 7), 'R': (8, 1), 'P': (2, 3), 'D': (3, 2), 'I': (6, 1), 'V': (1, 4), 
           'G': (2, 4), 'Z': (1, 6), 'O': (9, 1), 'H': (1, 5), 'E': (10, 1), 'X': (1, 5), 'J': (1, 10), 'N': (6, 1), 'A': (12, 1), 'W': (1, 9), 'L': (6, 1), 'M': (4, 3), 'C': (5, 1), 'Q': (1, 7), 'S': (7, 1)},
                 
                 
    'el': {'*': (2, 0), 'Τ': (8, 1), 'Γ': (2, 4), 'Ν': (6, 1), 'Α': (12, 1), 'Η': (7, 1), 'Κ': (4, 2), 'Υ': (4, 2), 'Ω': (3, 3), 'Δ': (2, 4), 'Χ': (1, 8), 'Φ': (1, 8), 'Σ': (7, 1), 
           'Λ': (3, 3), 'Ρ': (5, 2), 'Π': (4, 2), 'Ο': (9, 1), 'Θ': (1, 10), 'Ι': (8, 1), 'Β': (1, 8), 'Ε': (8, 1), 'Ξ': (1, 10), 'Μ': (3, 3), 'Ψ': (1, 10), 'Ζ': (1, 10)},
                 
                 
    'ht': {'*': (2, 0), '1': (4, 2), 'È': (4, 2), 'T': (4, 2), 'Y': (4, 2), 'K': (4, 2), 'F': (2, 4), 'R': (2, 4), 'P': (4, 2), 'D': (3, 3), 'I': (6, 1), 'B': (3, 4), 'V': (2, 4), 
           'G': (2, 4), 'Z': (1, 7), 'O': (4, 2), '3': (1, 8), 'E': (8, 1), 'Ò': (2, 4), 'J': (2, 4), 'N': (9, 1), '2': (2, 4), 'A': (9, 1), 'W': (2, 4), 'L': (4, 2), 'À': (1, 8), 'M': (4, 2), 'H': (1, 10), 'S': (4, 2)},
                 
                 
    'hu': {'*': (2, 0), 'Ú': (1, 7), 'B': (3, 2), 'V': (2, 3), 'T': (5, 1), '1': (2, 3), '7': (1, 10), 'K': (6, 1), 'F': (2, 4), 'Ű': (1, 7), 'R': (4, 1), 'P': (2, 4), 'É': (3, 3), 
           'I': (3, 1), 'U': (2, 4), 'Ó': (3, 2), 'G': (3, 2), 'Z': (2, 4), 'O': (3, 1), 'H': (2, 3), '4': (1, 7), 'E': (6, 1), '5': (1, 8), 'Ö': (2, 4), 'Ő': (1, 7), 'J': (2, 4), 
           'N': (4, 1), '2': (2, 4), 'Ü': (2, 4), 'A': (6, 1), 'D': (3, 2), 'L': (4, 1), 'M': (3, 1), 'Á': (4, 1), '6': (1, 8), 'Í': (1, 5), '3': (1, 5), 'C': (1, 5), 'S': (3, 1)},
                 
                 
    'is': {'*': (2, 0), 'B': (1, 5), 'U': (6, 2), 'Þ': (1, 7), 'T': (6, 2), 'Y': (1, 6), 'K': (4, 2), 'F': (3, 3), 'R': (8, 1), 'P': (1, 5), 'D': (1, 5), 'I': (7, 1), 'Ý': (1, 5), 
           'V': (1, 5), 'Ó': (2, 3), 'G': (3, 3), 'Í': (1, 4), 'O': (1, 5), 'Ú': (1, 4), 'E': (3, 3), 'X': (1, 10), 'Ö': (1, 6), 'J': (1, 6), 'N': (7, 1), 'Ð': (4, 2), 'A': (11, 1), 
           'É': (1, 7), 'L': (5, 2), 'M': (3, 2), 'Á': (2, 3), 'Æ': (2, 4), 'H': (1, 4), 'S': (7, 1)},
                 
                 
    'id': {'*': (2, 0), 'B': (4, 5), 'U': (5, 1), 'T': (5, 1), 'Y': (2, 5), 'K': (3, 2), 'F': (1, 5), 'R': (4, 1), 'P': (2, 4), 'D': (4, 3), 'I': (8, 1), 'V': (1, 8), 'G': (3, 3), 
           'Z': (1, 10), 'O': (3, 1), 'H': (2, 4), 'E': (8, 1), 'J': (1, 10), 'N': (9, 1), 'A': (19, 1), 'W': (1, 5), 'L': (3, 4), 'M': (3, 2), 'C': (3, 8), 'S': (3, 1)},
                 
                 
    'ga': {'*': (2, 0), 'B': (1, 10), 'U': (3, 2), 'T': (4, 2), 'F': (2, 4), 'R': (7, 1), 'P': (1, 10), 'É': (1, 8), 'I': (10, 1), 'Ó': (1, 8), 'G': (3, 2), 'O': (4, 2), 'H': (10, 1), 
           'E': (6, 1), 'N': (7, 1), 'A': (13, 1), 'D': (4, 2), 'L': (4, 2), 'M': (2, 4), 'Á': (2, 4), 'Í': (2, 4), 'Ú': (1, 8), 'C': (4, 2), 'S': (6, 1)},
                 
                 
    'it': {'*': (2, 0), 'B': (3, 5), 'U': (5, 3), 'T': (6, 2), 'F': (3, 5), 'R': (6, 2), 'P': (3, 5), 'D': (3, 5), 'I': (12, 1), 'V': (3, 5), 'G': (2, 8), 'Z': (2, 8), 'O': (15, 1), 
           'H': (2, 8), 'E': (11, 1), 'N': (5, 3), 'A': (14, 1), 'L': (5, 3), 'M': (5, 3), 'C': (6, 2), 'Q': (1, 10), 'S': (6, 2)},
                 
                 
    'hira': {'*': (2, 0), 'て': (4, 1), 'お': (1, 5), 'へ': (1, 8), 'う': (4, 1), 'り': (2, 3), 'め': (1, 6), 'ゆ': (1, 5), 'け': (2, 3), 'ら': (1, 3), 'こ': (3, 2), 'ほ': (1, 6), 
             'ぬ': (1, 12), 'ひ': (1, 5), 'ん': (4, 1), 'み': (1, 8), 'え': (1, 8), 'さ': (1, 4), 'な': (3, 2), 'た': (4, 1), 'き': (3, 2), 'や': (1, 6), 'の': (4, 1), 'し': (4, 1), 
             'む': (1, 10), 'せ': (2, 3), 'そ': (1, 4), 'か': (4, 1), 'ま': (1, 4), 'す': (2, 3), 'わ': (2, 3), 'あ': (2, 3), 'よ': (3, 2), 'と': (4, 1), 'れ': (3, 2), 'に': (3, 2), 
             'ね': (1, 10), 'ふ': (1, 5), 'く': (3, 2), 'ろ': (1, 10), 'る': (2, 3), 'も': (2, 3), 'つ': (3, 2), 'い': (4, 1), 'は': (3, 2), 'ち': (1, 4)},
                 
                 
    'romaji': {'*': (2, 0), 'B': (2, 5), '-': (2, 3), 'U': (12, 1), 'T': (4, 2), 'Y': (2, 4), 'K': (6, 2), 'F': (1, 8), 'R': (4, 2), 'P': (1, 8), 'D': (2, 5), 'I': (11, 1), 'G': (2, 4), 
               'Z': (1, 6), 'O': (10, 1), 'H': (4, 2), 'E': (5, 2), 'J': (1, 6), 'N': (7, 1), 'A': (12, 1), 'W': (1, 8), 'M': (3, 3), 'C': (1, 10), 'S': (6, 2)},
                 
                 
    'la': {'*': (2, 0), 'B': (2, 4), 'E': (12, 1), 'V': (9, 1), 'T': (8, 1), 'G': (2, 4), 'Q': (3, 3), 'R': (7, 1), 'N': (4, 2), 'P': (2, 4), 'A': (9, 1), 'D': (3, 2), 'L': (3, 2), 
           'I': (9, 1), 'M': (4, 2), 'X': (2, 4), 'H': (1, 8), 'C': (4, 2), 'F': (1, 8), 'O': (5, 1), 'S': (8, 1)},
                 
                 
    'lv': {'*': (2, 0), 'B': (1, 5), 'U': (5, 1), 'Ļ': (1, 8), 'T': (6, 1), 'Ķ': (1, 10), 'K': (4, 2), 'F': (1, 10), 'R': (5, 1), 'P': (3, 2), 'Ā': (4, 2), 'D': (3, 3), 'S': (8, 1), 
           'V': (3, 3), 'Č': (1, 10), 'G': (1, 5), 'Z': (2, 3), 'O': (3, 3), 'H': (1, 10), 'Ē': (2, 4), 'E': (6, 1), 'Ģ': (1, 10), 'J': (2, 4), 'A': (11, 1), 'N': (4, 2), 'Ī': (2, 4), 
           'L': (3, 2), 'Ž': (1, 8), 'M': (4, 2), 'Ū': (1, 6), 'Ņ': (1, 6), 'Š': (1, 6), 'C': (1, 5), 'I': (9, 1)},
                 
                 
    'lt': {'*': (2, 0), 'Ų': (1, 3), 'B': (2, 2), 'Į': (1, 4), 'U': (5, 1), 'T': (5, 1), 'Ė': (2, 3), 'K': (4, 2), 'F': (1, 10), 'R': (9, 1), 'P': (3, 2), 'Ū': (1, 5), 'D': (3, 2), 
           'I': (11, 1), 'V': (1, 4), 'G': (2, 2), 'Z': (1, 5), 'O': (5, 1), 'H': (1, 10), 'E': (6, 1), 'Y': (1, 6), 'J': (2, 4), 'Č': (1, 7), 'N': (4, 1), 'Ą': (1, 1), 'A': (9, 1), 
           'L': (6, 1), 'Ž': (1, 4), 'M': (3, 2), 'Ę': (1, 2), 'Š': (2, 3), 'C': (1, 7), 'S': (6, 1)},
                 
                 
    'mg': {'*': (2, 0), 'B': (2, 4), 'V': (2, 2), 'T': (6, 1), 'Y': (4, 1), 'K': (5, 1), 'F': (2, 2), 'R': (1, 6), 'P': (2, 4), 'D': (2, 3), 'I': (11, 1), 'G': (1, 10), 'Z': (1, 6), 
           'O': (14, 1), 'H': (1, 6), 'E': (4, 1), 'J': (1, 6), 'N': (13, 1), 'A': (20, 1), 'L': (2, 3), 'M': (2, 2), 'S': (4, 1)},
                 
                 
    'math': {'*': (2, 0), '0': (7, 1), '1': (7, 1), 'a': (4, 4), '5': (6, 2), '=': (20, 1), '7': (5, 3), '9': (4, 4), '−': (4, 3), '+': (4, 3), '*': (3, 0), '4': (6, 2), '8': (5, 3), 
             '^': (3, 10), '2': (7, 1), '6': (5, 3), '√': (3, 10), '÷': (4, 4), '3': (6, 2)},
                 
                 
    'no': {'*': (2, 0), 'B': (3, 4), 'U': (3, 4), 'T': (6, 1), 'Y': (1, 6), 'K': (4, 2), 'F': (4, 2), 'R': (6, 1), 'P': (2, 4), 'Ø': (2, 5), 'D': (5, 1), 'I': (5, 1), 'V': (3, 4), 
           'G': (4, 2), 'O': (4, 2), 'H': (3, 3), 'E': (9, 1), 'J': (2, 4), 'Å': (2, 4), 'N': (6, 1), 'A': (7, 1), 'W': (1, 8), 'L': (5, 1), 'M': (3, 2), 'Æ': (1, 6), 'C': (1, 10), 'S': (6, 1)},
                 
                 
    'pl': {'*': (2, 0), 'B': (2, 3), 'U': (2, 3), 'Ł': (2, 3), 'T': (3, 2), 'Y': (4, 2), 'K': (3, 2), 'F': (1, 5), 'R': (4, 1), 'P': (3, 2), 'Ź': (1, 9), 'D': (3, 2), 'I': (8, 1), 'Ś': (1, 5), 
           'Ó': (1, 5), 'G': (2, 3), 'Z': (5, 1), 'O': (6, 1), 'H': (2, 3), 'E': (7, 1), 'Ć': (1, 6), 'Ż': (1, 5), 'J': (2, 3), 'N': (5, 1), 'Ą': (1, 5), 'A': (9, 1), 'W': (4, 1), 'L': (3, 2), 
           'Ń': (1, 7), 'M': (3, 2), 'Ę': (1, 5), 'C': (3, 2), 'S': (4, 1)},
                 
                 
    'pt': {'*': (2, 0), 'B': (3, 3), 'U': (7, 1), 'T': (5, 1), 'F': (2, 4), 'R': (6, 1), '*': (3, 0), 'P': (4, 2), 'D': (5, 2), 'I': (10, 1), 'V': (2, 4), 'G': (2, 4), 'Z': (1, 8), 'O': (10, 1), 
           'H': (2, 4), 'E': (11, 1), 'X': (1, 8), 'J': (2, 5), 'N': (4, 3), 'A': (14, 1), 'L': (5, 2), 'M': (6, 1), 'Ç': (2, 3), 'C': (4, 2), 'Q': (1, 6), 'S': (8, 1)},
                 
                 
    'ro': {'*': (2, 0), 'B': (2, 5), 'U': (5, 1), 'T': (7, 1), 'F': (2, 4), 'R': (6, 1), 'P': (4, 2), 'D': (4, 3), 'I': (11, 1), 'V': (2, 4), 'G': (2, 6), 'Z': (1, 8), 'O': (5, 2), 'H': (1, 8), 
           'E': (9, 1), 'X': (1, 10), 'J': (1, 10), 'N': (6, 1), 'A': (10, 1), 'L': (5, 1), 'M': (3, 4), 'C': (5, 1), 'S': (6, 1)},
                 
                 
    'sk': {'*': (2, 0), 'U': (3, 2), 'Ä': (1, 8), 'Q': (1, 10), 'R': (5, 2), 'Ľ': (1, 5), 'É': (1, 3), 'I': (6, 1), 'Ó': (1, 8), 'G': (1, 6), 'Z': (2, 2), 'Ý': (1, 3), 'X': (1, 9), 'A': (9, 1), 
           'N': (5, 1), 'Ď': (1, 8), 'Č': (1, 3), 'Ž': (1, 3), 'M': (3, 2), 'Ť': (1, 4), 'Í': (1, 3), 'H': (1, 3), 'C': (1, 3), 'W': (1, 10), 'B': (2, 2), 'V': (5, 1), 'T': (4, 1), 'Y': (2, 2), 
           'K': (4, 2), 'F': (1, 6), 'E': (8, 1), 'P': (3, 2), 'Á': (2, 2), 'Ŕ': (1, 9), 'Ô': (1, 7), 'O': (10, 1), 'Ú': (1, 3), 'Š': (1, 3), 'J': (2, 2), 'Ň': (1, 7), 'Ĺ': (1, 9), 'D': (3, 2), 'L': (4, 2), 'S': (5, 1)},
                 
                 
    'sl': {'*': (2, 0), 'B': (2, 4), 'V': (4, 2), 'T': (4, 1), 'K': (3, 3), 'F': (1, 10), 'R': (6, 1), 'P': (2, 3), 'D': (4, 2), 'I': (9, 1), 'U': (2, 3), 'G': (2, 4), 'Z': (2, 4), 'O': (8, 1), 
           'H': (1, 5), 'E': (11, 1), 'J': (4, 1), 'Č': (1, 5), 'N': (7, 1), 'A': (10, 1), 'L': (4, 1), 'Ž': (1, 10), 'M': (2, 3), 'Š': (1, 6), 'C': (1, 8), 'S': (6, 1)},
                 
                 
    'sv': {'*': (2, 0), 'B': (2, 4), 'V': (2, 3), 'Ä': (2, 3), 'Y': (1, 7), 'K': (3, 2), 'F': (2, 3), 'R': (8, 1), 'P': (2, 4), 'D': (5, 1), 'I': (5, 1), 'U': (3, 4), 'G': (3, 2), 'Z': (1, 10), 
           'O': (5, 2), 'H': (2, 2), 'E': (7, 1), 'X': (1, 8), 'T': (8, 1), 'Ö': (2, 4), 'J': (1, 7), 'Å': (2, 4), 'N': (6, 1), 'A': (8, 1), 'L': (5, 1), 'M': (3, 2), 'C': (1, 8), 'S': (8, 1)},
                 
                 
    'tn': {'*': (2, 0), 'B': (3, 4), 'U': (1, 8), 'T': (6, 1), 'Y': (1, 8), 'K': (4, 3), 'F': (1, 8), 'R': (3, 5), 'P': (1, 8), 'D': (2, 5), 'I': (5, 2), 'G': (6, 1), 'O': (11, 1), 'H': (3, 5), 
           'E': (12, 1), 'J': (1, 10), 'N': (6, 1), 'A': (16, 1), 'W': (2, 5), 'L': (9, 1), 'M': (4, 3), 'S': (5, 1)},
                 
                 
    'tr': {'*': (2, 0), 'B': (2, 3), 'U': (3, 2), 'T': (5, 1), 'Y': (2, 3), 'K': (7, 1), 'F': (1, 7), 'R': (6, 1), 'P': (1, 5), 'Ş': (2, 4), 'D': (2, 3), 'I': (4, 2), 'V': (1, 7), 'İ': (7, 1), 
           'G': (1, 5), 'Z': (2, 4), 'O': (3, 2), 'H': (1, 5), 'E': (8, 1), 'Ğ': (1, 8), 'Ö': (1, 7), 'J': (1, 10), 'N': (5, 1), 'Ü': (2, 3), 'A': (12, 1), 'L': (7, 1), 'M': (4, 2), 'Ç': (2, 4), 'C': (2, 4), 'S': (3, 2)},
                 
                 
    'uk': {'*': (2, 0), 'М': (4, 2), 'Д': (3, 2), 'Г': (2, 4), 'Ц': (1, 6), 'Ш': (1, 6), 'Х': (1, 5), 'К': (4, 2), 'Я': (2, 4), 'Ж': (1, 6), 'Л': (3, 2), 'Щ': (1, 8), 'Ч': (1, 5), 'Е': (5, 1), 
           'Є': (1, 8), 'О': (10, 1), 'З': (2, 4), 'У': (3, 3), 'Р': (5, 1), 'П': (3, 2), 'Ю': (1, 7), 'Ї': (1, 6), 'В': (4, 1), 'Ґ': (1, 10), 'А': (8, 1), 'Б': (2, 4), "'": (1, 10), 'Т': (5, 1), 
           'Ь': (1, 5), 'Ф': (1, 8), 'Н': (7, 1), 'И': (7, 1), 'І': (5, 1), 'С': (4, 2), 'Й': (1, 5)},
                 
                 
    'cy': {'*': (2, 0), '1': (4, 1), 'U': (3, 2), 'T': (2, 3), 'B': (2, 3), 'F': (3, 2), 'R': (7, 1), 'P': (1, 5), 'D': (6, 1), 'I': (7, 1), '6': (1, 10), 'G': (3, 2), 'O': (6, 1), 'H': (2, 4), 
           '7': (1, 10), 'E': (8, 1), '5': (1, 5), 'Y': (7, 1), 'J': (1, 8), 'N': (8, 1), '2': (2, 4), '4': (1, 5), 'A': (10, 1), 'W': (5, 1), 'L': (3, 2), 'M': (2, 3), '3': (2, 4), 'C': (2, 4), 'S': (3, 3)},
                 
                 
    'bopo': {'*': (2, 0), 'ㄠ': (4, 5), 'ㄑ': (1, 8), 'ㄡ': (2, 7), 'ㄏ': (3, 6), 'ㄩ': (2, 6), 'ㄣ': (3, 5), 'ㄜ': (5, 4), 'ㄢ': (5, 4), 'ㄓ': (2, 6), 'ㄇ': (1, 8), 'ㄊ': (3, 6), 'ㄐ': (4, 5), 
             'ㄥ': (5, 4), 'ㄧ': (13, 1), 'ㄝ': (1, 8), 'ㄒ': (2, 6), 'ㄨ': (10, 1), 'ㄚ': (4, 5), 'ㄌ': (3, 6), 'ㄞ': (1, 7), 'ㄗ': (1, 8), 'ㄟ': (2, 6), 'ㄛ': (2, 7), 'ㄍ': (2, 7), 'ㄖ': (1, 8), 
             'ㄅ': (2, 6), 'ㄤ': (2, 6), 'ㄋ': (1, 8), 'ㄕ': (3, 6), 'ㄉ': (8, 4)},
                 
                 
    'ms': {'*': (2, 0), 'B': (3, 3), 'U': (6, 1), 'T': (5, 1), 'Y': (1, 5), 'K': (6, 1), 'F': (1, 10), 'R': (5, 1), 'P': (2, 4), 'D': (3, 3), 'I': (7, 1), 'G': (4, 3), 'Z': (1, 10), 'O': (2, 4), 
           'H': (2, 4), 'E': (7, 1), 'J': (1, 5), 'N': (8, 1), 'A': (19, 1), 'W': (1, 8), 'L': (4, 2), 'M': (5, 1), 'C': (1, 8), 'S': (4, 2)},

#     'en': {"*": (2,0), 'A': (1,1), "B": (1,3), "C": (1,3), "D": (1,2), "E": (1,1), "F": (1,4), "G": (1,2), "H": (1,4), "I": (1,1), "K": (1,5),
#            "L": (1,1), "M": (1,3), "N": (1,1), "O": (1,1), "P": (1,3), "R": (1,1), "S": (1,1), "T": (1,1), "U": (1,1), "V": (1,4),
#            "W": (1,4), "Y": (1,4)}
    }