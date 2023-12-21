#tính số phần tử của 1 danh sách
def tinh_so_phan_tu(danh_sach):
    dem = 0 
    for phan_tu in danh_sach:
        dem = dem+1
    return dem
danh_sach_phan_tu=[0,1,2,3,4,5]
print(tinh_so_phan_tu(danh_sach_phan_tu))
#kiểm tra giá trị nhập 
def kiem_tra_gia_tri_trong_khoang(gia_tri_dau_tien, gia_tri_cuoi,gia_tri):
    if (gia_tri_dau_tien <= gia_tri <= gia_tri_cuoi ):
        return True
    else:
        return False
kiem_tra =  kiem_tra_gia_tri_trong_khoang(int(input("Nhập số đầu tiên trong khoảng : ")), int(input("Nhập số cuối cùng trong khoảng : ")),int(input("Nhập số muốn kiểm tra trong khoảng : ")))
print(kiem_tra)
#sắp xếp phần tử
