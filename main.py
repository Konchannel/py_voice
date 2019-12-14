from . import speech_to_text as st
from . import gui


def main():
    speech_text = st.main()
    print(speech_text)


if __name__ == '__main__':
    main()