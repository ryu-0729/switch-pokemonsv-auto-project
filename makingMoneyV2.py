import time
from random import randint
import datetime
import nxbt
from nxbt import Buttons
from nxbt import Sticks
import cv2
import numpy as np


def random_colour():

    return [
        randint(0, 255),
        randint(0, 255),
        randint(0, 255),
    ]

def start_game(nx, cIndex):
    for _ in range(2):
        nx.press_buttons(cIndex, [Buttons.B], down=1.0)
        time.sleep(2)
    
    for _ in range(4):
        nx.tilt_stick(cIndex, Sticks.LEFT_STICK, -100, 0, 0.25, 0.25)

    nx.tilt_stick(cIndex, Sticks.LEFT_STICK, 0, 100, 0.25, 0.25)
    for _ in range(2):
        nx.press_buttons(cIndex, [Buttons.A], down=1.0)

def capture():
    cap = cv2.VideoCapture(0)

    for _ in range(60):
        ret, frame = cap.read()

    # NOTE: キャプチャ画面を返却
    return frame

# TODO: レポートするかの判定は画像比較を行う
def check_report():
    cap_img = capture()
    # NOTE: キャプチャ画像のトリミングと2値化処理
    trimming_cap_img = cap_img[125 : 175, 400 : 525]
    gray_cap_img = cv2.cvtColor(trimming_cap_img, cv2.COLOR_RGB2GRAY)
    _, thresh_cap_img = cv2.threshold(gray_cap_img, 0, 255, cv2.THRESH_OTSU)

    # NOTE: エントリー画像の読み込みと2値化処理
    img = cv2.imread('./img/trimming.jpg')
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, thresh_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_OTSU)

    ret = np.count_nonzero(thresh_cap_img == thresh_img)
    print('画像比較')
    print(ret)
    return ret >= 5500

def report(nx, cIndex):
    nx.press_buttons(cIndex, [Buttons.X], down=1.0)
    nx.press_buttons(cIndex, [Buttons.R], down=1.0)
    time.sleep(5)
    nx.press_buttons(cIndex, [Buttons.A], down=1.0)
    time.sleep(10)
    nx.press_buttons(cIndex, [Buttons.B], down=1.0)
    nx.press_buttons(cIndex, [Buttons.B], down=1.0)

def main():
    # Init NXBT
    nx = nxbt.Nxbt()

    # Get a list of all available Bluetooth adapters
    adapters = nx.get_available_adapters()
    # Prepare a list to store the indexes of the
    # created controllers.
    controller_index = []
    # Loop over all Bluetooth adapters and create
    # Switch Pro Controllers
    for i in range(0, len(adapters)):
        index = nx.create_controller(
            nxbt.PRO_CONTROLLER,
            adapter_path=adapters[i],
            colour_body=random_colour(),
            colour_buttons=random_colour())
        controller_index.append(index)

    # Select the last controller for input
    controller_index = controller_index[-1]
    print('接続中...')

    # Wait for the switch to connect to the controller
    nx.wait_for_connection(controller_index)

    # NOTE: ゲームの起動
    start_game(nx, controller_index)
    time.sleep(25)

    now = datetime.datetime.now()
    # NOTE: 任意の時間を設定
    after_hour = datetime.timedelta(hours=0, minutes=10)

    # TODO: 設定金額を設けて金額に達したら処理を終了したい
    while True:
        if check_report():
            # NOTE: レポート実行
            report(nx, controller_index)
            # NOTE: 設定時間を経過しているかつレポートが終わったタイミングで処理終了
            if not datetime.datetime.now() < now + after_hour:
                break
        nx.press_buttons(controller_index, [Buttons.R])
        nx.press_buttons(controller_index, [Buttons.A])

    print('処理終了...')


if __name__ == "__main__":
    main()
