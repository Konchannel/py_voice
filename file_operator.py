def operate_file():
    # 文字列から制御命令をサーチし、ファイルや文章を操作する
        # 文字列からファイル名をサーチし、取り出す。それをfile_nameとして渡す
    ...


def update_file(file_name, edited_message):
    with open(".\{}.py".format(file_name), mode='w') as file:
        file.write(edited_message)
