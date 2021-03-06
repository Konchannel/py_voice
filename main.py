from edit_message import edit_py_format as edit_py
import speech_to_text
import gui
import file_operator


def main():
    # text print by kivy.
    edited_message = get_message()
    gui.print_gui(edited_message)

    # save text.
    file_name = file_operator.edit_file_name()
    file_operator.update_file(file_name, edited_message)


# Get Japanese text converted to python format, from Google Speech-to-Text API & edit_py.
def get_message():
    message_voice = speech_to_text.main()
    edited_message = edit_py(message_voice)
    return edited_message


if __name__ == '__main__':
    main()


# 同期処理。音声取得　→　ファイル操作
    #                　→　コード生成　→　gui表示

    # ファイルを新規作成するか読み込むかを選択
        # 新規作成or読み込みの最初が違うだけ。ファイル表示するのは変わらないので
    # 音声入力は操作のためだけ。guiにファイルの現状が出る
        # guiのリアルタイム表示をさせたい
        # guiで制御命令を受け付けたい（ポインタ移動、文字削除(文字数指定)、コピー、ペースト、ひとつ戻す、行削除、複数行をまとめてインデント増減・コピー・カット・ペースト、変数名一括変更など）
        # guiで行番号表示したい