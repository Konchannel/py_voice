from . import speech_to_text as st
from . import gui


def main():
    speechtext = st.main()
    print(speechtext)


if __name__ == '__main__':
    main()