import cv2
#1. Mở camera
cap = cv2.VideoCapture(0)
#Load Haar Cascade để phát hiện khuôn mặt
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    #2.1 Chuyển sang grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #2.2 Phát hiện cạnh (canny)
    edges = cv2.Canny(gray, 100, 200)

    #2.3 Phát hiện khuôn mặt và vẽ hình chữ nhật
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y), (x+w, y+h), (255,0,0), 2)
    
    #Hiển thị kết quả
    cv2.imshow('Original', frame)
    cv2.imshow('Edges', edges)

    #Thoát khi nhấn 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows
