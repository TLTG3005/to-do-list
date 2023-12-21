chuyen_nganh = ['CNTT', 18, 'CNTT chat luong cao', 22, 'KHDL', 18, 'Dia chat', 17, 'Moi truong', 15]
Toan=int(input("Nhap diem toan cua ban: "))
Ly=int(input("Nhap diem ly cua ban: "))
Hoa=int(input("Nhap diem hoa cua ban: "))

tongdiem=Toan + Ly + Hoa 
check = 0
for i in range(1, len(chuyen_nganh), 2 ):
    if(tongdiem >= chuyen_nganh[i]):
        print(f"ban da trung tuyen {chuyen_nganh[i-1]}")
        check = 1
if(check == 0):
    print("Xin loi ban khong trung chuyen nganh nao")