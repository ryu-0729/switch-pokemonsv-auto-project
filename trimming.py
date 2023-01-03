import cv2 as cv


def main():
    img = cv.imread('./school-test.jpg')
    trimming_img = img[125 : 175, 400 : 525]
    cv.imwrite('./img/trimming.jpg', trimming_img)


if __name__ == '__main__':
    main()
