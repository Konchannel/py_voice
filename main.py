import speech_to_text as st
import gui


def main():
    response_str = st.main()
    gui.TestApp().get_message(response_str)
    gui.TestApp().run()
    print(response_str)


if __name__ == '__main__':
    main()