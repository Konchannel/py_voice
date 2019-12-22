import edit_message
import speech_to_text as st
import gui


def main():
    response_message = st.main()
    gui.TestApp().set_message(response_message)
    gui.TestApp().run()
    print(response_message)


if __name__ == '__main__':
    main()