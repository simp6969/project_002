import cv2

face_cascade = cv2.CascadeClassifier(
    "C:\Python311\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml"
)

img = cv2.imread("C:/workspace/workspace/project_002/20230207_122812.jpg")
while True:
    frame = img
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    print(*faces)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow("camera_main", frame)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
frame.release()
