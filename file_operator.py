from datetime import datetime


def operate_file():
    # 文字列から制御命令をサーチし、ファイルや文章を操作する
        # 文字列からファイル名をサーチし、取り出す。それをfile_nameとして渡す
    ...


def update_file(file_name, edited_message):
    with open(".\{}.py".format(file_name), mode='x') as file:
        file.write(edited_message)


# ひとまず,現在日時をファイル名とする(ファイル名も入力してもらうのが理想形)
def edit_file_name():
    dt = datetime.now().strftime("%Y%m%d_%H%M%S")
    return 'py_voice' + dt
