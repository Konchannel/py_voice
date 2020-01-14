# coding:utf-8
import re


def edit_py_format(message):

    # basic
    message = re.sub('かくかっことじる|角括弧とじる|角括弧閉じる', ']', message)
    message = re.sub('角括弧|角カッコ', '[', message)
    message = re.sub('中学校とじる|中学校閉じる|中括弧とじる|中括弧閉じる', '}', message)
    message = re.sub('中学校|中括弧|中カッコ', '{', message)
    message = re.sub('かっことじる|かっこ閉じる|括弧とじる|括弧閉じる', ')', message)
    message = re.sub('かっこ|括弧', '(', message)
    message = re.sub('Print|プリント', 'print', message)
    message = re.sub('ダブルクォーテーション|ダブルコーテーション', '"', message)
    message = re.sub('クォーテーション', "'", message)
    message = re.sub('コロン|コロ', ":", message)
    message = re.sub('インデント', "  ", message)
    message = re.sub('アンダースコア', "_", message)
    message = re.sub('ダンダー', "__init__", message)

    # bool
    message = re.sub('フォルス|ホルス', "False", message)
    message = re.sub('TRUEルー|TRUE', "True", message)
    message = re.sub('BoA|おあ|とは|ゴア', " or ", message)
    message = re.sub('アンド|&|安藤', " and ", message)
    message = re.sub('マット', " not ", message)
    message = re.sub('ノー|ローン|のん', "None", message)

    # Comparison
    message = re.sub('小なりイコール', " <= ", message)
    message = re.sub('大なりイコール', " >= ", message)
    message = re.sub('==', " == ", message)
    message = re.sub('ノットイコール', " != ", message)
    message = re.sub('小なり', " < ", message)
    message = re.sub('大なり', " > ", message)
    message = re.sub('伊豆', " is ", message)
    message = re.sub('イン', "in", message)

    # NewLine
    message = re.sub('\n', "", message)
    message = re.sub('改行', "\n", message)

    # Type
    message = re.sub('意味と|インド', "int", message)
    message = re.sub('フロート', "float", message)
    message = re.sub('string|STR', "str", message)

    # Operator
    message = re.sub('たす|足す|グラス|フラップ|ブラスト', "+", message)
    message = re.sub('ひく|引く|マイナス', "-", message)
    message = re.sub('かける|アスタリスク', "*", message)
    message = re.sub('ダブルバックスラッシュ|DOUBLE backslash|DOUBLE backslashシュ', "\\\\", message)
    message = re.sub('ダブルスラッシュ', "//", message)
    message = re.sub('わる|スラッシュ', "/", message)
    message = re.sub('パーセント', "%", message)

    # Import
    message = re.sub('from', "from", message)
    message = re.sub('import', "import", message)
    message = re.sub('アズ|アブ|あず|ある', "as", message)

    # Def
    message = re.sub('グラス|クラス|フラッシュ', "class ", message)
    message = re.sub('DEF|ジェフ|レフ', "def", message)

    # Conditional branch
    message = re.sub('IF|いふ|岐阜|皮膚', "if", message)
    message = re.sub('LE 5|Le 4|LE|LF|LEC|エリック', "elif", message)
    message = re.sub('ELse', "else", message)

    # Loop
    message = re.sub('4|フォー', "for", message)
    message = re.sub('はいる', "while", message)
    message = re.sub('ラムダ', "lambda", message)
    message = re.sub('グレープ|ブレーク|ブレイク', "break", message)
    message = re.sub('コンティニュー|コンビニ', "continue", message)
    message = re.sub('パス|バス|明日', "pass", message)
    message = re.sub('リターン', "return", message)

    # Other
    message = re.sub('レンジ', "range", message)
    message = re.sub('トライ', "try", message)
    message = re.sub('ウィズ', "with", message)
    message = re.sub('エクセプト|accept', "except", message)
    message = re.sub('Finallyル', "finally", message)

    return message

