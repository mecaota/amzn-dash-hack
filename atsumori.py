import wave
import pyaudio
import time
import os
from PIL import Image
# チャンク数を指定
CHUNK = 1024


def playAtsumori():
    img = Image.open('src/atsumori.png')

    wf = wave.open("src/atsumori.wav", "rb")
    p = pyaudio.PyAudio()
    # 画像表示

    img.show()

    # Streamを生成(3)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # Streamをつかって再生開始 (4)
    # 1024個読み取り
    data = wf.readframes(CHUNK)
    while data != "b''":
        stream.write(data)
        data = wf.readframes(CHUNK)
        print(data)
    # 再生が終わると、ストリームを停止・解放 (6)
    stream.stop_stream()
    stream.close()
    wf.close()

    p.terminate()
    img.close()


if __name__ == "__main__":
    playAtsumori()
