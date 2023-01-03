import cv2 as cv


def main():
    x = 25
    y = 25

    img = cv.imread('./school-test.jpg')

    img_y, img_x = img.shape[:2]

    img[y : img_y : y, : , :] = 255
    img[:, x : img_x : x, :] = 255

    cv.imwrite('./img/grid.jpg', img)


if __name__ == '__main__':
    main()
