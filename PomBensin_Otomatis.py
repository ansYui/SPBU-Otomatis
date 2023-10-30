from random import *
from time import *
from math import *

text1 = ["⎸              Masuk sebagai:               ⎹", 
         "⎸                 Login as:                 ⎹"]
text2 = ["⎸                1. Pembeli                 ⎹", 
         "⎸                1. Customer                ⎹"]
text3 = ["⎸       Masukkan angka 0 untuk keluar       ⎹", 
         "⎸              Enter 0 to exit              ⎹"]
text4 = ["⎸                Menu Utama                 ⎹", 
         "⎸                Main Menu                  ⎹"]
text5 = ["⎸      Silakan pilih jenis bahan bakar      ⎹", 
         "⎸      Please select the type of fuel       ⎹"]
text6 = ["⎸  1. Pertamax Turbo 98     Rp16.600/liter  ⎹", 
         "⎸  1. Pertamax Turbo 98     Rp16.600/litre  ⎹"]
text7 = ["⎸  2. Pertamax 92           Rp14.000/liter  ⎹", 
         "⎸  2. Pertamax 92           Rp14.000/litre  ⎹"]
text8 = ["⎸  3. Pertalite             Rp10.000/liter  ⎹", 
         "⎸  3. Pertalite             Rp10.000/litre  ⎹"]
text9 = ["⎸  4. Pertamina Dex         Rp17.900/liter  ⎹", 
         "⎸  4. Pertamina Dex         Rp17.900/litre  ⎹"]
text10 = ["⎸  5. Dexlite               Rp17.200/liter  ⎹", 
          "⎸  5. Dexlite               Rp17.200/litre  ⎹"]
text11 = ["⎸  6. Bio Solar             Rp6.800/liter   ⎹", 
          "⎸  6. Bio Solar             Rp6.800/litre   ⎹"]
text12 = ["Masukkan kata sandi: ", "Enter password: "]
text13 = ["Kata sandi yang Anda masukkan salah.", 
          "The password you entered is incorrect."]
text14 = ["Coba lagi? (Y/N): ", "Try again? (Y/N): "]
text15 = ["⎸            Halaman Utama Admin            ⎹", 
          "⎸              Admin Home Page              ⎹"]
text16 = ["⎸           Silakan pilih halaman           ⎹", 
          "⎸             Please select the             ⎹"]
text17 = ["⎸            yang hendak dituju             ⎹", 
          "⎸               desired page                ⎹"]
text18 = ["⎸            1. Cek Stok                    ⎹", 
          "⎸           1. Stock Checking               ⎹"]
text19 = ["⎸            2. Tambah Stok                 ⎹", 
          "⎸           2. Restock                      ⎹"]
text20 = ["⎸            3. Riwayat Transaksi           ⎹", 
          "⎸           3. Transaction History          ⎹"]
text21 = ["⎸          Masukkan nominal sesuai          ⎹", 
          "⎸             Enter the nominal             ⎹"]
text22 = ["⎸           dengan kebutuhan Anda           ⎹", 
          "⎸           cost of fuel required           ⎹"]
text23 = ["⎸   Masukkan huruf F untuk isi full tank    ⎹", 
          "⎸          Enter F for a full tank          ⎹"]
text24 = ["⎸          Masukkan angka 0 untuk           ⎹", 
          "⎸            Enter 0 to get back            ⎹"]
text25 = ["⎸           kembali ke menu utama           ⎹", 
          "⎸               to main menu                ⎹"]
text26 = ["Minimal dari nilai nominal isi bensin adalah Rp10.000", 
          "The minimum nominal for fuel filling is Rp10.000"]
text27 = ["⎸    Kendaraan anda sedang diisi dengan     ⎹", 
          "⎸   Your vehicle is being filled up with    ⎹"]
text28 = ["⎸              Harap tunggu...              ⎹", 
          "⎸              Please wait...               ⎹"]
text29 = ["Proses mengisi: ", "Filling progress: "]
text30 = ["⎸          Pengisian telah selesai          ⎹", 
          "⎸      Fuel filling has been completed      ⎹"]
text31 = ["⎸            Terima kasih telah             ⎹", 
          "⎸               Thank you for               ⎹"]
text32 = ["⎸         menggunakan layanan kami          ⎹", 
          "⎸             using our service             ⎹"]
text33 = ["⎸      Selamat melanjutkan perjalanan       ⎹", 
          "⎸             Have a nice trip              ⎹"]
text34 = ["⎸        Anda dan hati-hati di jalan        ⎹", 
          "⎸              and be careful               ⎹"]
text35 = ["⎸               Stok Tersedia               ⎹",
          "⎸              Available Stock              ⎹"]
text36 = ["liter tersedia", "litre available"]
text37 = ["⎸            Pilih jenis bensin             ⎹", 
          "⎸          Select the type of fuel          ⎹"]
text38 = ["⎸            yang ingin ditambah            ⎹", 
          "⎸              you want to add              ⎹"]
text39 = ["Masukkan kuantitas (liter) yang ingin ditambah ke persediaan: ",
          "Input the desired quantity (litre) to add to the inventory: "]
text40 = ["⎸             Histori Transaksi             ⎹", 
          "⎸            Transaction History            ⎹"]
text41 = ["⎸ No.  Jenis Bensin  Q (liter) Uang Dibayar ⎹", 
          "⎸ No.  Type of Fuel  Q (litre)    Amount    ⎹"]
text42 = ["⎸                            Berikutnya (2) ⎹", 
          "⎸                                 Next (2)  ⎹"]
text43 = ["⎸ Sebelumnya (1)             Berikutnya (2) ⎹", 
          "⎸  Previous (1)                   Next (2)  ⎹"]
text44 = ["⎸ Sebelumnya (1)                            ⎹", 
          "⎸  Previous (1)                             ⎹"]

def welcome():
    print("_______________________________________________")
    print("⎸                                             ⎹")
    print("⎸                                             ⎹")
    print("⎸           Selamat Datang di SPBU!           ⎹")
    print("⎸ Kami siap melayani kebutuhan BBM masyarakat ⎹")
    print("⎸                                             ⎹")
    print("⎸          Silakan masukkan angka 1           ⎹")
    print("⎸           untuk menggunakan mesin           ⎹")
    print("⎸                                             ⎹")
    print("⎸---------------------------------------------⎹")
    print("⎸                                             ⎹")
    print("⎸           Welcome to Gas Station!           ⎹")
    print("⎸ We are ready to serve public needs for fuel ⎹")
    print("⎸                                             ⎹")
    print("⎸           Please enter 1 to start           ⎹")
    print("⎸              using the machine              ⎹")
    print("⎸                                             ⎹")
    print("⎸                                             ⎹")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    return

def selectLang():
    print("_______________________________________________")
    print("⎸                                             ⎹")
    print("⎸                                             ⎹")
    print("⎸                 Pilih Bahasa                ⎹")
    print("⎸                ---------------              ⎹")
    print("⎸                Select Language              ⎹")
    print("⎸                                             ⎹")
    print("⎸                                             ⎹")
    print("⎸                                             ⎹")
    print("⎸              1. Bahasa Indonesia            ⎹")
    print("⎸                  2. English                 ⎹")
    print("⎸                                             ⎹")
    print("⎸                                             ⎹")
    print("⎸                                             ⎹")
    print("⎸      Masukkan angka 0 untuk pembatalan      ⎹")
    print("⎸      ---------------------------------      ⎹")
    print("⎸              Enter 0 to cancel              ⎹")
    print("⎸                                             ⎹")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    return

def loginScreen():
    print("_____________________________________________")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print(text1[lang])
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print(text2[lang])
    print("⎸                 2. Admin                  ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print(text3[lang])
    print("⎸                                           ⎹")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    return

def customerMenu():
    print("_____________________________________________")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print(text4[lang])
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print(text5[lang])
    print("⎸                                           ⎹")
    print(text6[lang])
    print(text7[lang])
    print(text8[lang])
    print(text9[lang])
    print(text10[lang])
    print(text11[lang])
    print("⎸                                           ⎹")
    print(text3[lang])
    print("⎸                                           ⎹")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    return

def adminHome():
    print("_____________________________________________")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print(text15[lang])
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print(text16[lang])
    print(text17[lang])
    print("⎸                                           ⎹")
    print(text18[lang])
    print(text19[lang])
    print(text20[lang])
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print(text3[lang])
    print("⎸                                           ⎹")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    return

def purchaseScreen():
    print("_____________________________________________")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print(text21[lang])
    print(text22[lang])
    print("⎸                                           ⎹")
    print(text23[lang])
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print(text24[lang])
    print(text25[lang])
    print("⎸                                           ⎹")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    return

def fuelFilling():
    if lang == 0:
        space = (34 - len(str(volume) + type[option]))
    else:
        space = (31 - len(str(volume) + type[option]))
    print("_____________________________________________")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print(text27[lang])
    print("⎸" + (space//2)*' ', volume, unit[lang], type[option], (space - space//2)*' ' + "⎹")
    print("⎸                                           ⎹")
    print(text28[lang])
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    return

def fuelFilled():
    print("_____________________________________________")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print(text30[lang])
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print(text31[lang])
    print(text32[lang])
    print("⎸                                           ⎹")
    print(text33[lang])
    print(text34[lang])
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    return

def stockChecking():
    if lang == 0:
        space = 8
    else:
        space = 7
    print("_____________________________________________")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print(text35[lang])
    print("⎸                                           ⎹")
    print(f"⎸ Pertamax Turbo 98 {stok[0]:>{space}} {text36[lang]} ⎹")
    print(f"⎸ Pertamax 92       {stok[1]:>{space}} {text36[lang]} ⎹")
    print(f"⎸ Pertalite         {stok[2]:>{space}} {text36[lang]} ⎹")
    print(f"⎸ Pertamina Dex     {stok[3]:>{space}} {text36[lang]} ⎹")
    print(f"⎸ Dexlite           {stok[4]:>{space}} {text36[lang]} ⎹")
    print(f"⎸ Bio Solar         {stok[5]:>{space}} {text36[lang]} ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print(text24[lang])
    print(text25[lang])
    print("⎸                                           ⎹")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    return

def restock():
    print("_____________________________________________")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print(text37[lang])
    print(text38[lang])
    print("⎸                                           ⎹")
    print("⎸           1. Pertamax Turbo 98            ⎹")
    print("⎸           2. Pertamax 92                  ⎹")
    print("⎸           3. Pertalite                    ⎹")
    print("⎸           4. Pertamina Dex                ⎹")
    print("⎸           5. Dexlite                      ⎹")
    print("⎸           6. Bio Solar                    ⎹")
    print("⎸                                           ⎹")
    print(text24[lang])
    print(text25[lang])
    print("⎸                                           ⎹")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    return

def transactionHistory(x):
    print("_____________________________________________")
    print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    print(text40[lang])
    print("⎸                                           ⎹")
    print(text41[lang])
    if x < pagination:
        for i in range(5*(x - 1), 5*x):
            print(transaction[i])
    else:
        for i in range(5*(x - 1), len(transaction)):
            print(transaction[i])
        for i in range(len(transaction), 5*x):
            print("⎸                                           ⎹")
    print("⎸                                           ⎹")
    if pagination == 1 or len(transaction) == 0:
        print("⎸                                           ⎹")
    else:
        if x == 1:
            print(text42[lang])
        elif x < pagination:
            print(text43[lang])
        else:
            print(text44[lang])
    print("⎸                                           ⎹")
    print(text24[lang])
    print(text25[lang])
    print("⎸                                           ⎹")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    return

def volumeConversion(x):
    if x == 'F':
        vehicleType = randint(1, 20)
        if vehicleType < 14:
            fillUp = round(uniform(2, 10), 2)
        elif vehicleType < 20:
            fillUp = round(uniform(10, 60), 2)
        else:
            fillUp = round(uniform(60, 200), 2)
    else:
        fillUp = round(int(x)/cost[option], 2)
    if fillUp == int(fillUp):
        return round(fillUp)
    return fillUp

def debitAdjustment(x):
    if x <= 10:
        return 0.5
    elif x <= 60:
        return 3
    else:
        return 8

def transactionRecording(x, y):
    rowNumber = str(transactionIndex + 1) + '.'
    pay = str(int(x*y))
    if len(pay) > 6:
        pay = pay[:len(pay) - 6] + '.' + pay[len(pay) - 6:len(pay) - 3] + '.' + pay[len(pay) - 3:]
    else:
        pay = pay[:len(pay) - 3] + '.' + pay[len(pay) - 3:]
    Activity = f"⎸ {rowNumber:<3} {type[option]:<14} {str(x):^9} {'+Rp' + pay:>12} ⎹"
    return Activity

def progress_percent(progress, total):
    print(f"{text29[lang]}{100*(progress/float(total)):.2f}%", end="\r")
    if progress == total:
        print("")

enter = '0'
type = ["Pertamax Turbo", "Pertamax", "Pertalite", 
        "Pertamina Dex", "Dexlite", "Bio Solar"]
cost = [16600, 14000, 10000, 17900, 17200, 6800]
stok = [1000, 1000, 1000, 1000, 1000, 1000]
unit = ["liter", "litre of"]
transaction = []
transactionIndex = 0

while True:
    while enter == '0':
        welcome()
        if input() == '1':
            selectLang()
            enter = input()
            if enter != '0':
                lang = int(enter) - 1
                while True:
                    loginScreen()
                    enter = input()
                    if enter != '2':
                        break
                    else:
                        while input(text12[lang]) != "123":
                            print(text13[lang])
                            if input(text14[lang]) == 'N':
                                break
                        else:
                            break
    if enter == '1':
        while True:
            customerMenu()
            enter = input()
            if enter == '0':
                break
            option = int(enter) - 1
            purchaseScreen()
            enter = input()
            while enter.isnumeric():
                if enter == '0' or int(enter) >= 10000:
                    break
                if int(enter) < 10000:
                    print(text26[lang])
                enter = input()
            if enter != '0':
                volume = volumeConversion(enter)
                debit = debitAdjustment(volume)
                transaction.append(transactionRecording(volume, cost[option]))
                transactionIndex += 1
                stok[option] = round(stok[option] - volume, 2)
                if stok[option] == int(stok[option]):
                    stok[option] = round(stok[option])
                fuelFilling()
                numbers = [x for x in range(round(20000*volume/debit))]
                for i, x in enumerate(numbers):
                    progress_percent(i + 1, len(numbers))
                fuelFilled()
                sleep(3)
                enter = '0'
                break
    elif enter == '2':
        while True:
            adminHome()
            enter = input()
            if enter == '0':
                break
            elif enter == '1':
                stockChecking()
                enter = input()
            elif enter == '2':
                restock()
                enter = input()
                if enter != '0':
                    stok[int(enter) - 1] += int(input(text39[lang]))
            elif enter == '3':
                pagination, pageNumber = ceil(len(transaction)/5), 1
                while True:
                    transactionHistory(pageNumber)
                    enter = input()
                    if enter == '0':
                        break
                    elif enter == '1':
                        pageNumber -= 1
                    elif enter == '2':
                        pageNumber += 1
