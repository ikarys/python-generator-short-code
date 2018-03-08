from sys import version_info
from random import choice, random
from string import digits, punctuation

# Detect Python version
# letters was splitted in Python 3.x
if version_info[0] < 3:
    from string import letters
else:
    from string import ascii_uppercase as letters_upper
    from string import ascii_lowercase as letters_lower
    letters = letters_upper + letters_lower

def generator_short_code(length=6, _digits=True, _letters=True, _punctuation=False, case='both'):
    """
    Generate short string code.
    @param length, String, default=6
    @param _digits, Boolean, default=True
    @param _letters, Boolean, default=True
    @param _punctuation, Boolean, default=False
    @param case, String, default='both'
    @return String
    """
    case_states = ['both', 'lower', 'upper']

    if case.lower() not in case_states:
        return ("Error : Case value is invalid, "
                "it must take one of the following state : %s" % ", ".join(case_states))

    possibilities = ''.join([
        digits if _digits else '',
        letters if _letters else '',
        punctuation if _punctuation else ''
    ])

    code = "".join(choice(possibilities) for i in range(length))

    if case == 'lower':
        code = code.lower()
    elif case == 'upper':
        code = code.upper()

    return code

