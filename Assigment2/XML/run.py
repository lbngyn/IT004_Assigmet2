import xml.etree.ElementTree as ET
import os
import pandas as pd
import numpy as np

def query_students_by_score(xml_file, min_score, max_score):
    # Đọc tệp tin XML 
    tree = ET.parse(f'{xml_file}')
    root = tree.getroot()

    # Xpath truy vấn danh sách học sinh có điểm trung bình nằm trong ngưỡng điểm
    xpath_query = f"//student[diem >= {min_score} and diem <= {max_score}]"
    students = root.findall(xpath_query)

    # In danh sách học sinh
    for student in students:
        ho = student.find("ho").text
        ten = student.find("ten").text
        diem = student.find("diem").text
        print(f"Họ tên: {ho} {ten}")
        print(f"Điểm trung bình: {diem}")
        print("---")


# Đường dẫn tuyệt đối của tệp tin đang thực thi
current_file_path = os.path.abspath(__file__)
#Lấy đường dẫn thư mục hiện tại
folder_path = os.path.dirname(current_file_path).replace(" ", "_")
# Lấy lấy file XML đầu tiên trong thư mục 
XML_file = os.path.join(folder_path,[f for f in os.listdir(folder_path) if f.endswith('.xml')][0])

# Nhập min và max 
min_score = input("Nhap so diem thap: ")
max_score = input("Nhap so diem cao: ")

# Thực hiện truy vấn danh sách học sinh từ tệp tin XML đã xuất ra từ câu 4
query_students_by_score(XML_file, min_score, max_score)
