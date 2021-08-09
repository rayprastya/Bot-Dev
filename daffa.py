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

# text = input('Coba ketik sesuatu :')

greeting = "Halloo, selamat datang di Mie Ayam Bangka Cianjur ! gunakan keyword 'menu 13k' atau 'menu 15k', untuk liat-liat menu kami yaa;D"

menu13 = [
    "Dipilih menu serba 13k nya yaa;D :",
    "1. Mie Ayam Bangka Polos",
    "2. Mie Yamin Bangka Polos",
    "3. Kwetiaw Bangka Polos",
    "4. Kwetiaw Yamin Bangka Polos",
]
menu15 = [
    "Dipilih menu serba 15k nya yaa;D :",
    "1. Mie Ayam Bangka + Bakso + Pangsit Goreng",
    "2. Mie Yamin Bangka + Bakso + Pangsit Goreng",
    "3. Kwetiaw Bangka + Bakso + Pangsit Goreng",
    "4. Kwetiaw Yamin Bangka + Bakso + Pangsit Goreng",
]

text = ""
while text != "keluar":
    text = input("Coba ketik sesuatu : ")
    if text in ["halo", "Halo", "Hallo", "hallo"]:
        print(greeting)
    elif text in ["menu 13k", "Menu 13k"]:
        print(*menu13, sep="\n")
    elif text in ["menu 15k", "Menu 15k"]:
        print(*menu15, sep="\n")
    else:
        # break
        print("Kamu bilang apa, aku ga ngertii...aku belum bisa banget bahasa indonesia soalnya:(")
