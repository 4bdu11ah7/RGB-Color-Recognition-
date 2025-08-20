import cv2

def mouse_click(event, x, y, flags, param):
    global clicked, r, g, b, xpos, ypos
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked = True
        xpos, ypos = x, y
        b, g, r = img[y, x]
        b, g, r = int(b), int(g), int(r)

clicked = False
r = g = b = xpos = ypos = 0

img = cv2.imread('image.jpg')

width = 800
height = int(img.shape[0] * (width / img.shape[1]))
img = cv2.resize(img, (width, height))

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouse_click)

while True:
    temp_img = img.copy()

    if clicked:
        cv2.rectangle(temp_img, (20, 20), (600, 60), (b, g, r), -1)
        text = f"R={r} G={g} B={b}"
        cv2.putText(temp_img, text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.imshow('Image', temp_img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
