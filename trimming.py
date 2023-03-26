import cv2 as cv


def main():
    img = cv.imread('./img/reentry.jpg')
    # NOTE: img[top : bottom, left : right]
    trimming_img = img[275 : 400, 25 : 200]
    cv.imwrite('./img/reentry_trimming.jpg', trimming_img)


if __name__ == '__main__':
    main()
