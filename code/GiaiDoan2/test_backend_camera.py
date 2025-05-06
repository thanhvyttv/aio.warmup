import cv2

# Thử với backend DSHOW (thường dùng trên Windows)
cap_dshow = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if cap_dshow.isOpened():
    print("Camera 0 mở thành công với CAP_DSHOW.")
    cap_dshow.release()
else:
    print("Không thể mở camera 0 với CAP_DSHOW.")

# Thử với backend V4L2 (thường dùng trên Linux)
cap_v4l = cv2.VideoCapture(0, cv2.CAP_V4L2)
if cap_v4l.isOpened():
    print("Camera 0 mở thành công với CAP_V4L2.")
    cap_v4l.release()
else:
    print("Không thể mở camera 0 với CAP_V4L2.")

# Thử với camera 1 và các backend
cap_dshow_1 = cv2.VideoCapture(1, cv2.CAP_DSHOW)
if cap_dshow_1.isOpened():
    print("Camera 1 mở thành công với CAP_DSHOW.")
    cap_dshow_1.release()
else:
    print("Không thể mở camera 1 với CAP_DSHOW.")

cap_v4l_1 = cv2.VideoCapture(1, cv2.CAP_V4L2)
if cap_v4l_1.isOpened():
    print("Camera 1 mở thành công với CAP_V4L2.")
    cap_v4l_1.release()
else:
    print("Không thể mở camera 1 với CAP_V4L2.")
