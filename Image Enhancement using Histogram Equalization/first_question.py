import cv2


def myHistEq(img):
    width, height, depth = img.shape
    total = width * height
    begin = [[0 for col in range(width)] for row in range(height)]
    cnt = [0] * 256
    for i in range(width):
        for j in range(height):
            cnt[img[i][j]] += 1
    for i in range(1, 256):
        cnt[i] += cnt[i-1]
    cnt = cnt * 255 / total
    target = begin
    for i in range(width):
        for j in range(height):
            target[i][j] = cnt[img[i][j]]
    return target


img_bgr = cv2.imread("mp2.jpg", cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
mydst = myHistEq(img_gray)
cvdst = cv2.equalizeHist(img_gray)
cv2.imwrite("mp2cvdst.jpg", cvdst)
cv2.imwrite("mp2mydst.jpg", mydst)
