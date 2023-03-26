import cv2 as cv
import numpy as np


def main():
    img = cv.imread('./img/reentry_trimming.jpg')
    gray_img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    ret, thresh_img = cv.threshold(gray_img, 0, 255, cv.THRESH_OTSU)
    cv.imwrite('./img/thresh_reentry.jpg', thresh_img)
    print(ret)

    # NOTE: 比較する際にはトリミングは必須。warningになる
    test = np.count_nonzero(thresh_img == thresh_img)
    print(test) # NOTE: 6250で判定

if __name__ == '__main__':
    main()
