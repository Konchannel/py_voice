import re

def edit_py_format(message):
    trans_table = str({'だんだ': '__', 'だんだん': '__', 'イニット': 'init', 'かっこ': '(', '括弧': '(',
                       'かっことじる': ')', '括弧とじる': ')','括弧閉じる': ')',
                       '角括弧': '[', '角カッコ': '[', '中括弧': '{', '中カッコ': '{',
                       'プリント': 'print', 'クォーテーション': "'", 'ダブルクォーテーション': '"'})
    message.translate(trans_table)
    return message
