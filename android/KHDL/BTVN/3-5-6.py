sinhvien = int(input("Nhập số lượng sinh viên: "))
monhoc = int(input("Nhập số lượng môn học: "))


danh_sach_sinh_vien = {}


for i in range(sinhvien):
    ten_sv = input(f"Nhập tên sinh viên {i+1}: ")
    diem_sv = []
    for j in range(monhoc):
        diem = float(input(f"Nhập điểm môn học {j+1} của sinh viên {ten_sv}: "))
        diem_sv.append(diem)
    danh_sach_sinh_vien[ten_sv] = diem_sv


print("Điểm trung bình của mỗi sinh viên:")
for ten_sv, diem_sv in danh_sach_sinh_vien.items():
    diem_trung_binh = sum(diem_sv) / len(diem_sv)
    print(f"Sinh viên {ten_sv}: {diem_trung_binh}")