import mysql.connector
import xml.etree.ElementTree as ET
import time

def query(): 
    # Input
    print("Nhập database: ", end = ""); your_database = input()
    print("Nhập truong: ", end = ""); truong = input()
    print("Nhập hoc: ", end = ""); namhoc = input()  #(2018, 2024)
    print("Nhập xep loai: ", end = ""); xeploai = input() #Xuat sac, Gioi, Kha, Trung binh, Yeu

    # Kết nối tới cơ sở dữ liệu MySQL
    connection = mysql.connector.connect(
        host = localhost,
        user = your_username,
        password = your_password,
        database = your_database
    )
    # Tạo đối tượng cursor
    cursor = connection.cursor()

    # Tạo câu truy vấn để lấy danh sách học sinh
    query = f"""
    SELECT HS.HO, HS.TEN, HS.NTNS, H.DIEMTB, H.XEPLOAI, H.KQUA
    FROM HS
    INNER JOIN HOC H ON HS.MAHS = H.MAHS
    WHERE H.MATR = '{truong}' AND H.NAMHOC = {namhoc} AND H.XEPLOAI = '{xeploai}';
    """
    # Thực thi câu truy vấn và đo thời gian truy vấn
    start_time = time.time()
    cursor.execute(query)
    end_time = time.time()
    execution_time = end_time - start_time

    # Lấy kết quả truy vấn
    results = cursor.fetchall()

    # Tạo danh sách học sinh dưới dạng cây XML
    root = ET.Element("HocSinhList")
    for result in results:
        ho, ten, ntns, diemtb, xeploai, kqua = result
        hoc_sinh = ET.SubElement(root, "HocSinh")
        ET.SubElement(hoc_sinh, "Ho").text = ho
        ET.SubElement(hoc_sinh, "Ten").text = ten
        ET.SubElement(hoc_sinh, "NTNS").text = str(ntns)
        ET.SubElement(hoc_sinh, "DiemTB").text = str(diemtb)
        ET.SubElement(hoc_sinh, "XepLoai").text = xeploai
        ET.SubElement(hoc_sinh, "KetQua").text = kqua

    # Tạo tên file XML dựa trên thông tin đầu vào
    file_name = f"XML\{your_database}-{truong}-{namhoc}-{xeploai}.xml"
    
    # Ghi danh sách học sinh vào file XML
    tree = ET.ElementTree(root)
    tree.write(file_name)
    
    #In ra màn hình thời gian chạy truy vấn 
    print(f"Thời gian thực hiện truy vấn: {execution_time} seconds")
    
    # Đóng kết nối
    cursor.close()
    connection.close()

#Nhập các thông tin để connect vào cơ sở dữ liệu 
print("Nhập localhost: ", end=""); localhost = input() 
print("Nhập user: ", end=""); your_username = input() 
print("Nhập password: ", end=""); your_password = input() 

while True: 
    query() 
    print(
f"""
------------------------------------------------------------------------
Ban co muon tiep tuc truy van khong? 
nhap 'n' de thoat chuong trinh 
nhap bat ki ki tu khac de tiep tuc"""
) 
    signal = input() 
    if signal == 'n' : 
        print("Ket thuc!") 
        break
