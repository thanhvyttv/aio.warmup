import cv2


def test_camera(index):
    cap = cv2.VideoCapture(index)
    if cap.isOpened():
        print(f"Camera {index} mở thành công.")
        cap.release()
        return True
    else:
        print(f"Không thể mở camera {index}.")
        return False


for i in range(10):  # Thử các chỉ số từ 0 đến 9
    test_camera(i)
