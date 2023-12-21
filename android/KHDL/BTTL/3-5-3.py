drink={
    'tra chanh' : 10000,
    'tra dao' : 20000,
    'tra tac': 10000
}
number_of_new_drink= int(input("Nhap so luong do uong moi: "))
for i in range(0, number_of_new_drink):
    add_drink=int(input(f"Nhap do uong ban muon them vao menu: "))
    drink[add_drink] = int(input(f'Nhap gia do uong vao {add_drink}'))

print('--Menu--')