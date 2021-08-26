# catatan :
# serba 13k :
# "Mie Ayam bangka polos",
# "Mie Yamin bangka polos",
# "kwetiaw bangka polos",
# "kwetiaw yamin bangka polos"

# serba 15k :
# "Mie Ayam bangka + bakso + pangsit goreng",
# "Mie yamin bangka + bakso + pangsit goreng",
# "kwetiaw bangka + bakso + pangsit goreng",
# "kwetiaw yamin bangka + bakso + pangsit goreng"

# var
menu1 = "Mie Ayam Bangka Polos"
menu2 = "Mie Yamin Bangka Polos"
menu3 = "Kwetiaw Bangka Polos"
menu4 = "Kwetiaw Yamin Bangka Polos"
menu5 = "Mie Ayam Bangka + Bakso + Pangsit Goreng"
menu6 = "Mie Yamin Bangka + Bakso + Pangsit Goreng"
menu7 = "Kwetiaw Bangka + Bakso + Pangsit Goreng"
menu8 = "Kwetiaw Yamin Bangka + Bakso + Pangsit Goreng"

menu13 = [
    menu1,
    menu2,
    menu3,
    menu4,
]

menu15 = [
    menu5,
    menu6,
    menu7,
    menu8,
]

mainmenu = [menu13, menu15]
choosenmainmenu = ""
# end var

# func pilihmenu
def choosemenu():
    print(
        "Halloo, selamat datang di Mie Ayam Bangka Cianjur ! Silahkan kamu pilih menu berdasarkan harga  : \n1. Menu serba 13K\n2. Menu serba 15K"
    )
    choosenmenu = input("Kamu mau menu yang mana : ")
    if choosenmenu == "1":
        for m13 in range(len(menu13)):
            print(str(m13 + 1) + ". " + menu13[m13])
        choose = int(input("Silahkan pilih menu yang kamu mau :"))
        choosenmainmenu = str(menu13[choose - 1])
    elif choosenmenu == "2":
        for m15 in range(len(menu15)):
            print(str(m15 + 1) + ". " + menu15[m15])
        choose = int(input("Silahkan pilih menu yang kamu mau :"))
        choosenmainmenu = str(menu15[choose - 1])
    return choosenmainmenu


# end pilihmenu


# play
choosenmainmenu = choosemenu()
print("")
print("okee, aku konfirmasi kalau menu yang kamu pilih adalah " + choosenmainmenu)
