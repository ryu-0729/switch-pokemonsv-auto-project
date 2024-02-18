import time
from random import randint

import cv2 as cv
import numpy as np
from nxbt import PRO_CONTROLLER, Buttons, Nxbt, Sticks


class CustomCommon:
    def __init__(self):
        self.nx = Nxbt
        self.controller_index = []

    def setup_controller(self):
        adapters = self.nx.get_available_adapters()
        controller_index = []

        for i in range(0, len(adapters)):
            index = self.nx.create_controller(
                PRO_CONTROLLER,
                adapter_path=adapters[i],
                colour_body=self.random_colour(),
                colour_buttons=self.random_colour(),
            )
            controller_index.append(index)

        self.controller_index = controller_index[-1]

    def random_colour(self):
        return [
            randint(0, 255),
            randint(0, 255),
            randint(0, 255),
        ]

    def game_start(self):
        """NOTE: コントローラーの持ち方/順番を変える画面からゲームを起動するまで"""

        for _ in range(2):
            self.nx.press_buttons(self.controller_index, [Buttons.B], down=1.0)
            time.sleep(2)

        for _ in range(4):
            self.nx.tilt_stick(
                self.controller_index, Sticks.LEFT_STICK, -100, 0, 0.25, 0.25
            )

        self.nx.tilt_stick(self.controller_index, Sticks.LEFT_STICK, 0, 100, 0.25, 0.25)
        for _ in range(2):
            self.nx.press_buttons(self.controller_index, [Buttons.A], down=1.0)

    def get_capture(self):
        """NOTE: キャプチャの取得と画像の返却"""

        cap = cv.VideoCapture(0)

        for _ in range(60):
            _, frame = cap.read()

        return frame

    def image_comparison(self, img, trimming_cap_img):
        """NOTE: 画像の比較結果を返す"""

        # NOTE: キャプチャ画像のトリミングと2値化処理
        gray_cap_img = cv.cvtColor(trimming_cap_img, cv.COLOR_RGB2GRAY)
        _, thresh_cap_img = cv.threshold(gray_cap_img, 0, 255, cv.THRESH_OTSU)

        # NOTE: 比較元の画像の読み込みと2値化処理
        gray_img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
        _, thresh_img = cv.threshold(gray_img, 0, 255, cv.THRESH_OTSU)

        # NOTE: 一致する要素数を取得し、既定値を超えているか判定
        ret = np.count_nonzero(thresh_cap_img == thresh_img)
        return ret

    def check_report(self, cap_img):
        """NOTE: キャプチャ画像と学校最強大会エントリー画面の「学校最強大会」の画像と一致するか判定"""

        trimming_cap_img = cap_img[125:175, 400:525]
        img = cv.imread("./img/trimming.jpg")
        ret = self.image_comparison(img, trimming_cap_img)

        print(f"レポート比較結果：{ret}")
        return ret >= 5500

    def check_re_entry(self, cap_img):
        """NOTE: キャプチャ画像とリエントリー判定用画像と一致するか判定"""

        trimming_cap_img = cap_img[275:400, 25:200]
        img = cv.imread("./img/reentry_trimming.jpg")
        ret = self.image_comparison(img, trimming_cap_img)

        print(f"リエントリー比較結果：{ret}")
        return ret >= 17000

    def report(self):
        """NOTE: レポートを書く"""

        self.nx.press_buttons(self.controller_index, [Buttons.X], down=1.0)
        self.nx.press_buttons(self.controller_index, [Buttons.R], down=1.0)
        time.sleep(5)
        self.nx.press_buttons(self.controller_index, [Buttons.A], down=1.0)
        time.sleep(10)
        self.nx.press_buttons(self.controller_index, [Buttons.B], down=1.0)
        self.nx.press_buttons(self.controller_index, [Buttons.B], down=1.0)

    def streak_button(self):
        """NOTE: RボタンとAボタンの連打"""

        self.nx.press_buttons(self.controller_index, [Buttons.R])
        self.nx.press_buttons(self.controller_index, [Buttons.A])

    def restart(self):
        """NOTE: ゲームを終了して再起動"""

        time.sleep(5)
        self.nx.press_buttons(self.controller_index, [Buttons.HOME], down=0.3)
        time.sleep(2)
        self.nx.press_buttons(self.controller_index, [Buttons.X], down=1.0)
        time.sleep(2)
        self.nx.press_buttons(self.controller_index, [Buttons.A], down=1.0)
        time.sleep(5)
        self.nx.press_buttons(self.controller_index, [Buttons.A], down=1.0)
        time.sleep(2)
        self.nx.press_buttons(self.controller_index, [Buttons.A], down=1.0)
