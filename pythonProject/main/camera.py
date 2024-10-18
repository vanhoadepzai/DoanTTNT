import cv2
import os
import tkinter as tk
from tkinter import messagebox

# Biến toàn cục để lưu camera
cam = None

def chup_anh():
    global cam
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Chụp Ảnh")

    # Đường dẫn để lưu ảnh
    base_save_path = r"D:\tai lieu\DOANATTT\pythonProject\save\inputface"

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Không thể mở camera")
            break
        cv2.imshow("Chụp Ảnh", frame)

        k = cv2.waitKey(1) & 0xFF  # Thêm & 0xFF để lấy mã phím đúng
        if k == 27:
            # ESC để thoát
            print("Thoát!")
            break
        elif k == 32:
            # Phím space để chụp ảnh
            nhap_thong_tin(base_save_path, frame)  # Gọi hàm nhập thông tin sau khi chụp ảnh

    cam.release()
    cv2.destroyAllWindows()

def nhap_thong_tin(base_save_path, frame):
    # Tạo một cửa sổ mới
    root = tk.Tk()
    root.title("Nhập Thông Tin")
    root.geometry("300x200")  # Kích thước của cửa sổ

    # Cài đặt màu nền
    root.configure(bg="#f0f0f0")  # Màu nền xám nhạt

    # Tạo label và entry cho họ tên
    lbl_ho_ten = tk.Label(root, text="Họ tên:", font=("Arial", 12, "bold"), bg="#f0f0f0")
    lbl_ho_ten.pack(pady=5)  # Thêm khoảng cách trên dưới
    entry_ho_ten = tk.Entry(root, font=("Arial", 12), width=25)
    entry_ho_ten.pack(pady=5)

    # Tạo label và entry cho số tuổi
    lbl_tuoi = tk.Label(root, text="Số tuổi:", font=("Arial", 12, "bold"), bg="#f0f0f0")
    lbl_tuoi.pack(pady=5)
    entry_tuoi = tk.Entry(root, font=("Arial", 12), width=25)
    entry_tuoi.pack(pady=5)

    # Hàm kiểm tra thông tin đã tồn tại
    def kiem_tra_thong_tin(ho_ten, tuoi):
        user_folder = os.path.join(base_save_path, ho_ten)
        info_path = os.path.join(user_folder, "info.txt")

        if os.path.exists(info_path):
            with open(info_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if f"Họ tên: {ho_ten}, Số tuổi: {tuoi}" in line:
                        return True  # Thông tin đã tồn tại
        return False  # Thông tin chưa tồn tại

    # Hàm xử lý khi nhấn nút "Lưu"
    def luu_thong_tin():
        ho_ten = entry_ho_ten.get().strip()
        tuoi = entry_tuoi.get()

        # Kiểm tra nếu họ tên hoặc tuổi trống
        if ho_ten == "" or tuoi == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập đủ thông tin!")
            return

        # Kiểm tra nếu tuổi không phải là số
        if not tuoi.isdigit():
            messagebox.showerror("Lỗi", "Số tuổi phải là một số hợp lệ!")
            return

        # Tạo thư mục mới dựa trên họ tên
        user_folder = os.path.join(base_save_path, ho_ten)  # Tạo đường dẫn thư mục mới
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)  # Tạo thư mục nếu chưa tồn tại

        # Đếm số ảnh đã có trong thư mục
        existing_images = [f for f in os.listdir(user_folder) if f.endswith('.png')]
        img_counter = len(existing_images)  # Chỉ số ảnh bắt đầu từ số lượng ảnh đã có

        # Tạo đường dẫn mới để lưu ảnh
        img_name = f"{ho_ten}_image_{img_counter + 1}.png"  # Sử dụng tên cơ bản và chỉ số mới
        img_full_path = os.path.join(user_folder, img_name)

        # Lưu ảnh vào thư mục mới
        cv2.imwrite(img_full_path, frame)  # Lưu ảnh đã chụp thẳng vào thư mục người dùng
        print(f"Đã lưu ảnh vào {img_full_path}!")

        # Kiểm tra nếu thông tin đã tồn tại
        if kiem_tra_thong_tin(ho_ten, tuoi):
            messagebox.showinfo("Thông báo", "Thông tin này đã tồn tại! Chỉ lưu ảnh mới.")
        else:
            # Đường dẫn tệp để lưu thông tin
            info_path = os.path.join(user_folder, "info.txt")  # Cập nhật đường dẫn tệp thông tin

            # Lưu thông tin vào tệp với mã hóa UTF-8
            with open(info_path, 'a', encoding='utf-8') as f:  # Mở tệp ở chế độ thêm với mã hóa UTF-8
                f.write(f"Họ tên: {ho_ten}, Số tuổi: {tuoi}, Đường dẫn ảnh: {img_full_path}\n")

        # Hiển thị thông tin đã nhập
        messagebox.showinfo("Thông tin đã nhập", f"Họ tên: {ho_ten}\nSố tuổi: {tuoi}\nĐã lưu ảnh tại: {img_full_path}")
        root.destroy()  # Đóng cửa sổ nhập liệu

    # Tạo nút "Lưu"
    btn_luu = tk.Button(root, text="Lưu", command=luu_thong_tin, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
    btn_luu.pack(pady=20)

    root.protocol("WM_DELETE_WINDOW", lambda: (cam.release(), root.destroy()))  # Giải phóng camera khi đóng cửa sổ

    root.mainloop()

# Gọi hàm chụp ảnh
chup_anh()
