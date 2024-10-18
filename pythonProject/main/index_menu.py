import tkinter as tk
from camera import chup_anh
from face_recognition import nhan_dien_khuon_mat

# Giao diện chính
def main_menu():
    window = tk.Tk()
    window.title("Menu Chính")
    window.geometry("300x250")  # Đã tăng chiều cao để thêm nút thoát

    lbl_title = tk.Label(window, text="Chọn chức năng", font=("Arial", 16))
    lbl_title.pack(pady=10)

    btn_chup_anh = tk.Button(window, text="Chụp Ảnh", command=chup_anh, width=20, height=2)
    btn_chup_anh.pack(pady=10)

    btn_nhan_dien = tk.Button(window, text="Nhận Diện Khuôn Mặt", command=nhan_dien_khuon_mat, width=20, height=2)
    btn_nhan_dien.pack(pady=10)

    # Thêm nút "Thoát"
    btn_exit = tk.Button(window, text="Thoát", command=window.quit, width=20, height=2, bg='red')
    btn_exit.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main_menu()
