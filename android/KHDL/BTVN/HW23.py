so_sinh_vien= int(input("Nhap so sinh vien: "))
mon_hoc= int(input("Nhập số lượng môn học: "))
diem= []

for i in range(0,so_sinh_vien):
    diem_temp = []
    for j in range (0, mon_hoc):
        diem_mon = float(input(f"Nhập điểm môn học thứ {j+1} của sinh viên thứ {i+1}: "))
        diem_temp.append(diem_mon)
    diem.append(diem_temp)
diem_tb=[]
for i in range(0, so_sinh_vien):
    diem_tb_sv = sum(diem[i])/mon_hoc
    diem_tb.append(diem_tb_sv)

for i in range(0, so_sinh_vien):
    print(f"Điểm trung bình của sinh viên thứ {i+1}là: {diem_tb}")



