from sys import exit
from funcion import *
from os import system
from time import sleep


def Man_Hinh_Chinh():
    global var
    print('''
##  ##   #   #   #   ##### ##### #   # #   #
# ## #  # #   # #      #     #   ##  # #   #
#    # #   #   #       #     #   # # # #####
#    # #####   #       #     #   #  ## #   #
#    # #   #   #       #   ##### #   # #   #

Chuc Nang
1.Tinh Toan Thong Thuong
2.Phuong Trinh
3.Sap Xep
4.Dung Sai
5.VecTor
6.Thong Ke
7.Ghi Chu
8.Huong Dan
9.Thoat
''')
    var = input('==>')


while True:
    try:
        var = None
        while True:
            system('cls')
            Man_Hinh_Chinh()
            while var == '1':
                i = input('Nhap Phep Tinh: ')
                if i == 'thoat':
                    break
                print(math(i))
            while var == '2':
                system('cls')
                print('''
1.Phuong Trinh Bac Nhat
2.Phuong Trinh Bac Hai
3.Phuong Trinh Bac Ba
4.Phuong Trinh Bac Bon
5.Phuong Trinh Bac Nam(Ket Qua Co The Khong Chinh Xac)
6.Thoat
***Phuong Trinh Bac Nhat Va Hai Khong In Ra So Phuc***''')
                chose = input('==>')
                while chose == '1':
                    system('cls')
                    a = float(input('Nhap a: '))
                    b = float(input('Nhap b: '))
                    print(phuongtrinhbacnhat(a, b))
                    check = input('Tiep Tuc? y/n')
                    if 'n' in check.lower():
                        break

                while chose == '2':
                    system('cls')
                    a = float(input('Nhap a: '))
                    b = float(input('Nhap b: '))
                    c = float(input('Nhap c: '))
                    print(phuongtrinhbachai(a, b, c))
                    check = input('Tiep Tuc? y/n')
                    if 'n' in check.lower():
                        break
                while chose == '3':
                    system('cls')
                    a = float(input('Nhap a: '))
                    b = float(input('Nhap b: '))
                    c = float(input('Nhap c: '))
                    d = float(input('Nhap d: '))
                    print(phuongtrinhbacba(a, b, c, d))
                    check = input('Tiep Tuc? y/n')
                    if 'n' in check.lower():
                        break
                while chose == '4':
                    system('cls')
                    a = float(input('Nhap a: '))
                    b = float(input('Nhap b: '))
                    c = float(input('Nhap c: '))
                    d = float(input('Nhap d: '))
                    e = float(input('Nhap e: '))
                    print(phuongtrinhbacbon(a, b, c, d, e))
                    check = input('Tiep Tuc? y/n')
                    if 'n' in check.lower():
                        break
                while chose == '5':
                    system('cls')
                    a = float(input('Nhap a: '))
                    b = float(input('Nhap b: '))
                    c = float(input('Nhap c: '))
                    d = float(input('Nhap d: '))
                    e = float(input('Nhap e: '))
                    f = float(input('Nhap f: '))
                    print(phuongtrinhbacnam(a, b, c,d, e, f))
                    check = input('Tiep Tuc? y/n')
                    if 'n' in check.lower():
                        break
                if chose.lower() == 'thoat' or chose == '6':
                    break
            while var == '3':
                system('cls')
                a = input(
                    'Nhap Cac Gia Tri Can Sap Xep Cach Nhau Boi Dau Cach: ').split()
                print(sapxep(a))
                check = input('Tiep Tuc? y/n')
                if 'n' in check.lower():
                    break
            while var == '4':
                a = input('Nhap Gia Tri So Sanh(vd: 1<2): ')
                if a == 'thoat':
                    break
                print(dungsai(a))
            Vector_2_Chieu_list = [[None, None] for i in range(8)]
            Vector_3_Chieu_list = [[None, None, None] for i in range(8)]
            while var == '5':
                l = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                              'E': 4, 'F': 5, 'G': 6, 'H': 7}
                chose = input(('''
1.Hien Cac Bien Vector Da Co
2.Tao VecTor
3.Tich Toan VecTor
4.Tich Vo Huong
5.Goc Giua Hai VecTor
6.Thoat
'''))
                while chose == '1':
                    chose1 = input('''
1.Vector 2 chieu
2.Vector 3 chieu
3.Thoat
==>''')
                    if chose1 == '1':
                        print(Vector_2_Chieu_list)
                    elif chose1 == '2':
                        print(Vector_3_Chieu_list)
                    elif chose1 == '3':
                        break
                    else:
                        print('Vui Long Nhap Lai')
                while chose == '2':
                    chose2_1 = input('''
1.Vector 2 chieu
2.Vector 3 chieu
3.Thoat
==>''')
                    if chose2_1 == '1':
                        chose2 = input('''
Tao:A,B,C,D,E,F,G,H
    ''').upper()

                        while chose2 in l:
                            print(Vector_2_Chieu_list[l[f'{chose2}']])
                            a = float(input('Nhap Hang 1: '))
                            Vector_2_Chieu_list[l[f'{chose2}']][0] = round(a, 6)
                            print(Vector_2_Chieu_list[l[f'{chose2}']])
                            b = float(input('Nhap Hang 2: '))
                            Vector_2_Chieu_list[l[f'{chose2}']][1] = round(b, 6)
                            print(Vector_2_Chieu_list[l[f'{chose2}']])
                            sleep(1)
                            break
                        if chose2 == 'thoat':
                            break
                    if chose2_1 == '2':
                        chose2 = input('''
                    Tao: A, B, C, D, E,F, G, H
                        ''').upper()
                        while chose2 in l:
                            print(Vector_3_Chieu_list[l[f'{chose2}']])
                            a = float(input('Nhap Hang 1: '))
                            Vector_3_Chieu_list[l[f'{chose2}']][0] = round(a, 6)
                            print(Vector_3_Chieu_list[l[f'{chose2}']])
                            b = float(input('Nhap Hang 2: '))
                            Vector_3_Chieu_list[l[f'{chose2}']][1] = round(b, 6)
                            print(Vector_3_Chieu_list[l[f'{chose2}']])
                            c = float(input('Nhap Hang 3: '))
                            Vector_3_Chieu_list[l[f'{chose2}']][2] = round(c, 6)
                            print(Vector_3_Chieu_list[l[f'{chose2}']])
                            sleep(1)
                            break

                    if chose2_1 == '3':
                        break
                while chose == '3':
                    chose3 = input('''
1. Vector 2 chieu
2. Vector 3 chieu
3. Thoat
==> ''')

                    if chose3 == '1':
                        try:
                            a = input('Nhap VecTor Thu Nhat: ').upper()
                            Vector1 = Vector_2_Chieu(Vector_2_Chieu_list[l[f'{a}']][0], Vector_2_Chieu_list[l[f'{a}']][1])
                            c = input('Nhap Phep Tinh: ')
                            b = input('Nhap VecTor Thu Hai: ').upper()
                            Vector2 = Vector_2_Chieu(Vector_2_Chieu_list[l[f'{b}']][0], Vector_2_Chieu_list[l[f'{b}']][1])
                            if c == '+':
                                print(Vector1.cong(Vector2))
                            elif c == '-':
                                print(Vector1.tru(Vector2))
                            elif c == '*':
                                print(Vector1.nhan(Vector2))
                            elif c == '/':
                                print(Vector1.chia(Vector2))
                        except Exception as ex:
                            print('Loi', ex)

                    elif chose3 == '2':
                        try:
                            a = input('Nhap VecTor Thu Nhat: ').upper()
                            Vector1 = Vector_3_Chieu(Vector_3_Chieu_list[l[f'{a}']][0], Vector_3_Chieu_list[l[f'{a}']][1], Vector_3_Chieu_list[l[f'{a}']][2])
                            c = input('Nhap Phep Tinh: ')
                            b = input('Nhap VecTor Thu Hai: ').upper()
                            Vector2 = Vector_3_Chieu(Vector_3_Chieu_list[l[f'{b}']][0], Vector_3_Chieu_list[l[f'{b}']][1], Vector_3_Chieu_list[l[f'{b}']][2])
                            if c == '+':
                                print(Vector1.cong(Vector2))
                            elif c == '-':
                                print(Vector1.tru(Vector2))
                            elif c == '*':
                                print(Vector1.nhan(Vector2))
                            elif c == '/':
                                print(Vector1.chia(Vector2))
                        except Exception as ex:
                            print('Loi', ex)

                    elif chose3 == '3' or chose3.lower() == 'thoat':
                        break
                while chose == '4':
                    chose4 = input('''
1. Vector 2 chieu
2. Vector 3 chieu
3. Thoat
==> ''')
                    if chose4 == '1':  # 2 chieu
                        a = input(
                            'Nhap Hai Gia Tri Cach Nhau Boi Dau Cach').upper().split()
                        Vector1 = Vector_2_Chieu(Vector_2_Chieu_list[l[f'{a[0]}']][0], Vector_2_Chieu_list[l[f'{a[0]}']][1])
                        Vector2 = Vector_2_Chieu(Vector_2_Chieu_list[l[f'{a[1]}']][0], Vector_2_Chieu_list[l[f'{a[1]}']][1])
                        print(Vector1.tichvohuong(Vector2))
                    elif chose4 == '2':
                        a = input(
                            'Nhap Hai Gia Tri Cach Nhau Boi Dau Cach: ').upper().split()
                        Vector1 = Vector_3_Chieu(Vector_3_Chieu_list[l[f'{a[0]}']][0], Vector_3_Chieu_list[l[f'{a[0]}']][1], Vector_3_Chieu_list[l[f'{a[0]}']][2])
                        Vector2 = Vector_3_Chieu(Vector_3_Chieu_list[l[f'{a[1]}']][0], Vector_3_Chieu_list[l[f'{a[1]}']][1], Vector_3_Chieu_list[l[f'{a[1]}']][2])
                        print(Vector1.tichvohuong(Vector2))
                    elif chose4 == '3':
                        break
                while chose == '5':
                    chose5 = input('''
1. Vector 2 chieu
2. Vector 3 chieu
3. Thoat
==> ''')
                    if chose5 == '1':
                        chon5 = input(
                            'Nhap Hai Gia Tri Cach Nhau Boi Dau Cach: ').upper().split()
                        print(chon5)
                        Vector1 = Vector_2_Chieu(Vector_2_Chieu_list[l[f'{chon5[0]}']][0], Vector_2_Chieu_list[l[f'{chon5[0]}']][1])
                        Vector2 = Vector_2_Chieu(Vector_2_Chieu_list[l[f'{chon5[1]}']][0], Vector_2_Chieu_list[l[f'{chon5[1]}']][1])
                        print(Vector1.x,Vector1.y)
                        print(Vector2.x,Vector2.y)
                        print(Vector1.gocgiuahaiduongthang(Vector2))
                    elif chose5 =='2':
                        a = input(
'Nhap Hai Gia Tri Cach Nhau Boi Dau Cach: ').upper().split()
                        Vector1 = Vector_3_Chieu(Vector_3_Chieu_list[l[f'{a[0]}']][0], Vector_3_Chieu_list[l[f'{a[0]}']][1], Vector_3_Chieu_list[l[f'{a[0]}']][2])
                        Vector2 = Vector_3_Chieu(Vector_3_Chieu_list[l[f'{a[1]}']][0], Vector_3_Chieu_list[l[f'{a[1]}']][1], Vector_3_Chieu_list[l[f'{a[1]}']][2])
                        print(Vector1.gocgiuahaiduongthang((Vector2)))
                    elif chose5 == '3':break
                if chose =='6':break
            while var == '6':
                chose6 = input('Nhap So Lieu Cach Nhau Boi Dau Cach: ').split()
                if chose6 == ['thoat']:break
                chose6 = [int(i) for i in chose6]
                khanh = thongke(chose6)
                print(f'''
Gia Tri Lon Nhat: {khanh.max()}
Gia Tri Nho Nhat: {khanh.min()}
So Phan Tu: {khanh.sophantu()}
Tu Phan Vi: {khanh.quartiles()}
Trung Binh Cong: {khanh.trungbinh()}
Trung Vi: {khanh.trungvi()}          
''')
                
                        
            if var == '7':
                from subprocess import run
                file = "note.txt"
                try:
                    run(["notepad.exe", file], check=True)
                except FileNotFoundError:
                    with open(file, "w") as f:
                        pass
                    run(["notepad.exe", file], check=True)
            elif var =='8':
                system('cls')
                print('''
~~~~~~~~~~~~~~~~~~~Phan Mem May Tinh~~~~~~~~~~~~~~~~~~~

Phan Mem Nay Do Bui Duy Khanh Lam Trong Vong 4 Ngay
T Chi Mong Moi Nguoi Su Dung No Thoi
Huong Dan:    Nhap Cac Chu So Theo Yeu Cau Thoi
              Neu Muon Thoat 1 Cho Hay Nhap Chu 'thoat'

Love Me: https://www.facebook.com/profile.php?id=100089931995830
GitHub: https://github.com/BuiKhanh2007?fbclid=IwAR1ZFlHWC5Tfqr5BvzC6XPxbb3elkOduOXB8q0R1zPVq4e1lX10GZaw0hio
''')
                a = input('Thoat <=>')
                break
            if var == '9':
                exit()
    except Exception as ex:
        print('Loi: ', ex)
        print('Ve Man Hinh Chinh!')
        sleep(2)
