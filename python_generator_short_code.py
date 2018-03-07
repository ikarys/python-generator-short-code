from random import choice, random
from string import digits, letters, punctuation

def generator_short_code(length=6, _digits=True, _letters=True, _punctuation=False):
    """
    Generate short string code.
    @param length, String, default=6
    @param _digits, Boolean, default=True
    @param _letters, Boolean, default=True
    @param _punctuation, Boolean, default=False
    @return String
    """
    code = ''
    possibilities = ''.join([
        digits if _digits else '',
        letters if _letters else '',
        punctuation if _punctuation else ''
    ])
    for i in range(length):
        code += choice(possibilities)
    return code
