import speech_to_text as st
import gui


def main():
    response_str = st.main()
    gui.TestApp().run()
    # gui.TestApp().build(response_str)  # 画面表示が残るようにしなければ
    print(response_str)


if __name__ == '__main__':
    main()