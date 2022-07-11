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


img_bgr = cv2.imread("mp2a.jpg", cv2.IMREAD_COLOR)
(B, G, R) = cv2.split(img_bgr)
mydst = myHistEq(G)
cvdst = cv2.equalizeHist(G)
merged1 = cv2.merge([B, mydst,  R])
merged2 = cv2.merge([B, cvdst, R])
cv2.imwrite("mp2aGcvdst.jpg", merged2)
cv2.imwrite("mp2aGmydst.jpg", merged1)
