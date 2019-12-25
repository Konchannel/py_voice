import re


def edit_py_format(message):
    message = re.sub('かくかっことじる|角括弧とじる|角括弧閉じる', ']', message)
    message = re.sub('角括弧|角カッコ', '[', message)
    message = re.sub('中学校とじる|中学校閉じる|中括弧とじる|中括弧閉じる', '}', message)
    message = re.sub('中学校|中括弧|中カッコ', '{', message)
    message = re.sub('かっことじる|括弧とじる|括弧閉じる', ')', message)
    message = re.sub('かっこ|括弧', '(', message)
    message = re.sub('プリント', 'print', message)
    message = re.sub('ダブルクォーテーション', '"', message)
    message = re.sub('クォーテーション', "'", message)
    # bool
    message = re.sub('', "False", message)
    message = re.sub('', "None", message)
    message = re.sub('', "True", message)
    message = re.sub('', "or", message)
    message = re.sub('', "and", message)
    message = re.sub('', "not", message)

    # Comparison
    message = re.sub('', "<=", message)
    message = re.sub('', ">=", message)
    message = re.sub('', "==", message)
    message = re.sub('', "!=", message)
    message = re.sub('', "<", message)
    message = re.sub('', ">", message)

    message = re.sub('', "as", message)
    message = re.sub('', "assert", message)
    message = re.sub('', "async", message)
    message = re.sub('', "await", message)
    message = re.sub('', "break", message)
    message = re.sub('', "class", message)
    message = re.sub('', "continue", message)
    message = re.sub('', "def", message)
    message = re.sub('', "del", message)
    message = re.sub('', "elif", message)
    message = re.sub('', "else", message)
    message = re.sub('', "except", message)
    message = re.sub('', "finally", message)
    message = re.sub('', "for", message)
    message = re.sub('', "from", message)
    message = re.sub('', "global", message)
    message = re.sub('', "if", message)
    message = re.sub('', "import", message)
    message = re.sub('', "in", message)
    message = re.sub('', "is", message)
    message = re.sub('', "lambda", message)
    message = re.sub('', "nonlocal", message)
    message = re.sub('', "pass", message)
    message = re.sub('', "raise", message)
    message = re.sub('', "return", message)
    message = re.sub('', "try", message)
    message = re.sub('', "while", message)
    message = re.sub('', "with", message)
    message = re.sub('', "yield", message)

    '''
      '(', ')', '{', '}', '[', ']'
      'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
      'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
      'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
      'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
    '''

    return message
