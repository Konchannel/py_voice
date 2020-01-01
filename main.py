from edit_message import edit_py_format as edit_py
import speech_to_text as st
import gui


def main():
    message_str = st.main()
    edited_str = edit_py(message_str)
    gui.print_gui(edited_str)
    print(message_str)
    print("-----")
    print(edited_str)


if __name__ == '__main__':
    main()