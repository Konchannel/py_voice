import re


def edit_py_format(message):
    '''
    trans_table = str({'だんだ': '__', 'だんだん': '__', 'イニット': 'init',
                        '中括弧': '{', '中カッコ': '{',)
    '''

    message = re.sub('かくかっことじる|角括弧とじる|角括弧閉じる', ']', message)
    message = re.sub('角括弧|角カッコ', '[', message)
    message = re.sub('中学校とじる|中学校閉じる|中括弧とじる|中括弧閉じる', '}', message)
    message = re.sub('中学校|中括弧|中カッコ', '{', message)
    message = re.sub('かっことじる|括弧とじる|括弧閉じる', ')', message)
    message = re.sub('かっこ|括弧', '(', message)
    message = re.sub('プリント', 'print', message)
    message = re.sub('ダブルクォーテーション', '"', message)
    message = re.sub('クォーテーション', "'", message)

    return message
