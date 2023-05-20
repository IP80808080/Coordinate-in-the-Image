import cv2

input = cv2.imread("input.jpg")

height, width, _ = input.shape

max_width = 800
max_height = 600

if width > max_width or height > max_height:
    ratio = min(max_width / width, max_height / height)
    new_width = int(width * ratio)
    new_height = int(height * ratio)
else:
    new_width = width
    new_height = height

cv2.namedWindow("input", cv2.WINDOW_NORMAL)
cv2.resizeWindow("input", new_width, new_height)


cv2.imshow("input", input)

def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        print(f"Coordinates (x, y) : ({x}, {y})")

cv2.setMouseCallback("input", get_coordinates)

cv2.waitKey(0)
cv2.destroyAllWindows()
