# English
## What is py_voice?
py_voice provides programming with Japanese voice input (voice coding).

## How to use
1. ```set GOOGLE_APPLICATION_CREDENTIALS=[credentials file pass]```
2. Run ```python main.py``` in console.
3. Speak in Japanese into the microphone .
4. If you say syuuro(終了) or owari(終わり), speech recognition will end.

  
# 日本語
## py_voiceとは？
py_voiceは日本語の音声入力でのプログラミング（ボイスコーディング）を提供します

## 使い方
1.```set GOOGLE_APPLICATION_CREDENTIALS=[credentials file pass]```

2.コンソールで```python py_voice```を実行します

3.マイクに向かって日本語で喋りかけます

4.終了、または終わりと言ったら音声認識を終了します

## GUIライブラリ(Kivy)を使用するためにインストールするもの
pip install --upgraade pip wheel setuptools

pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew

pip install kivy.deps.gstreamer

pip install kivy.deps.angle

pip install --upgrade kivy