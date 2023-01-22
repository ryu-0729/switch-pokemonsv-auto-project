import time
import cv2 as cv
import numpy as np
from nxbt import Buttons
from nxbt import Sticks


class CustomCommon():
    def __init__(self, nx, cIndex):
        self.nx = nx
        self.cIndex = cIndex


    def game_start(self):
        """ NOTE: コントローラーの持ち方/順番を変える画面からゲームを起動するまで """

        for _ in range(2):
            self.nx.press_buttons(self.cIndex, [Buttons.B], down=1.0)
            time.sleep(2)

        for _ in range(4):
            self.nx.tilt_stick(self.cIndex, Sticks.LEFT_STICK, -100, 0, 0.25, 0.25)

        self.nx.tilt_stick(self.cIndex, Sticks.LEFT_STICK, 0, 100, 0.25, 0.25)
        for _ in range(2):
            self.nx.press_buttons(self.cIndex, [Buttons.A], down=1.0)


    def get_capture(self):
        """ NOTE: キャプチャの取得と画像の返却 """

        cap = cv.VideoCapture(0)

        for _ in range(60):
            ret, frame = cap.read()

        return frame


    def check_report(self, cap_img):
        """ NOTE: キャプチャ画像と学校最強大会エントリー画面の「学校最強大会」の画像と一致するか判定 """

        # NOTE: キャプチャ画像のトリミングと2値化処理
        trimming_cap_img = cap_img[125 : 175, 400 : 525]
        gray_cap_img = cv.cvtColor(trimming_cap_img, cv.COLOR_RGB2GRAY)
        _, thresh_cap_img = cv.threshold(gray_cap_img, 0, 255, cv.THRESH_OTSU)

        # NOTE: エントリー画像の読み込みと2値化処理
        img = cv.imread('./img/trimming.jpg')
        gray_img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
        _, thresh_img = cv.threshold(gray_img, 0, 255, cv.THRESH_OTSU)

        # NOTE: 一致する要素数を取得し、既定値を超えているか判定
        ret = np.count_nonzero(thresh_cap_img == thresh_img)
        print('画像比較中')
        print(f'比較結果：{ret}')
        return ret >= 5500


    def report(self):
        """ NOTE: レポートを書く """

        self.nx.press_buttons(self.cIndex, [Buttons.X], down=1.0)
        self.nx.press_buttons(self.cIndex, [Buttons.R], down=1.0)
        time.sleep(5)
        self.nx.press_buttons(self.cIndex, [Buttons.A], down=1.0)
        time.sleep(10)
        self.nx.press_buttons(self.cIndex, [Buttons.B], down=1.0)
        self.nx.press_buttons(self.cIndex, [Buttons.B], down=1.0)


    def streak_button(self):
        """ NOTE: RボタンとAボタンの連打 """

        self.nx.press_buttons(self.cIndex, [Buttons.R])
        self.nx.press_buttons(self.cIndex, [Buttons.A])
