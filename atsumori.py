import wave
import pyaudio
import time
import cv2
import urllib
import numpy as np
import matplotlib.pyplot as plt
# チャンク数を指定
CHUNK = 1024


def downloadImage(url):
    img_read = urllib.request.urlopen(url).read()  # URLよりバイナリストリームで画像取得
    img_arr = np.fromstring(img_read, np.uint8)  # ストリームをnumpy arrayに変換
    image = cv2.imdecode(img_arr, -1)
    if image is None:
        raise ValueError("'" + url + "'" +
                         "はこのプログラムでは扱えないファイルです。このファイルはパスされます。")
        return None
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


def playAtsumori():
    wf = wave.open("src/atsumori.wav", "rb")
    p = pyaudio.PyAudio()
    # Streamを生成(3)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # Streamをつかって再生開始 (4)
    # 1024個読み取り
    data = wf.readframes(CHUNK)
    img = downloadImage("https://pbs.twimg.com/media/C-VUJ58VYAAtZnV.jpg")
    plt.imshow(img)
    plt.show()
    plt.close()
    while "''" not in str(data):
        stream.write(data)
        data = wf.readframes(CHUNK)
        print(data)
    # 再生が終わると、ストリームを停止・解放 (6)
    stream.stop_stream()
    stream.close()
    wf.close()
    p.terminate()


if __name__ == "__main__":
    playAtsumori()
