import os
import requests

def download_images_from_file(file_path, output_folder):
    # Kiểm tra xem thư mục output có tồn tại chưa, nếu chưa thì tạo mới
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Đọc các liên kết từ tệp văn bản
    with open(file_path, 'r') as file:
        image_links = file.readlines()

    # Lặp qua từng liên kết và tải về ảnh
    for idx, link in enumerate(image_links):
        link = link.strip()  # Loại bỏ khoảng trắng và dấu xuống dòng
        try:
            response = requests.get(link)
            if response.status_code == 200:
                # Lấy tên tệp từ URL và kết hợp với thư mục đầu ra
                file_name = os.path.join(output_folder, f"image_{idx + 1}.png")
                with open(file_name, 'wb') as img_file:
                    img_file.write(response.content)
                print(f"Đã tải xuống: {file_name}")
            else:
                print(f"Lỗi khi tải xuống ảnh từ {link}")
        except Exception as e:
            print(f"Lỗi khi xử lý ảnh từ {link}: {e}")

# Gọi hàm để tải về ảnh
file_path = 'room15.txt'
output_folder = 'input'
download_images_from_file(file_path, output_folder)