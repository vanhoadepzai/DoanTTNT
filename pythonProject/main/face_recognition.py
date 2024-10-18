import cv2
import os


def nhan_dien_khuon_mat():
    # Kiểm tra file haarcascade có tồn tại hay không
    haarcascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    if not os.path.exists(haarcascade_path):
        print("Không tìm thấy file haarcascade_frontalface_default.xml")
        return

    # Load file haarcascade dùng để nhận diện khuôn mặt
    face_cascade = cv2.CascadeClassifier(haarcascade_path)

    cam = cv2.VideoCapture(0)

    # Kiểm tra nếu camera không mở được
    if not cam.isOpened():
        print("Không thể mở camera")
        return

    cv2.namedWindow("Nhận Diện Khuôn Mặt")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Không thể lấy hình ảnh từ camera")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Chuyển đổi sang ảnh xám để nhận diện
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Vẽ hình chữ nhật xung quanh khuôn mặt
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow("Nhận Diện Khuôn Mặt", frame)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            # ESC để thoát
            print("Thoát!")
            break

    cam.release()
    cv2.destroyAllWindows()
