import os

# MAIN MENU FUNCTION
def ana_menu():
    print("\n*** Basit Not Defteri Uygulaması ***")
    print("1. Yeni Metin Dosyası Oluştur")
    print("2. Metin Dosyasını Düzenle")
    print("3. Metin Dosyasını Sil")
    print("4. Mevcut Metin Dosyalarını Listele")
    print("5. Çıkış")
    secim = input("Bir seçenek girin (1-5): ")
    return secim

# FILE CREATOR FUNCTION
def dosya_olustur():
    dosya_adi = input("Oluşturmak istediğiniz dosyanın adını girin (uzantı olmadan): ") + ".txt"
    try:
        if os.path.exists(dosya_adi):
            print("Bu adla zaten bir dosya var.")
        else:
            with open(dosya_adi, 'w') as dosya:
                dosya.write(input("Dosyaya yazmak istediğiniz metni girin: "))
            print(f"{dosya_adi} oluşturuldu.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

# FILE EDITOR FUNCTION
def dosya_duzenle():
    dosya_adi = input("Düzenlemek istediğiniz dosyanın adını girin (uzantı olmadan): ") + ".txt"
    try:
        if os.path.exists(dosya_adi):
            with open(dosya_adi, 'a') as dosya:
                dosya.write("\n" + input("Dosyaya eklemek istediğiniz metni girin: "))
            print(f"{dosya_adi} düzenlendi.")
        else:
            print("Bu adla bir dosya bulunamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

# DELETE FILE FUNCTION
def dosya_sil():
    dosya_adi = input("Silmek istediğiniz dosyanın adını girin (uzantı olmadan): ") + ".txt"
    try:
        if os.path.exists(dosya_adi):
            os.remove(dosya_adi)
            print(f"{dosya_adi} silindi.")
        else:
            print("Bu adla bir dosya bulunamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

# FILE LIST FUNCTION
def dosya_listele():
    dosyalar = [f for f in os.listdir() if f.endswith('.txt')]
    if dosyalar:
        print("\nMevcut metin dosyaları:")
        for dosya in dosyalar:
            print(dosya)
    else:
        print("Hiçbir metin dosyası bulunamadı.")


def main():
    while True:
        secim = ana_menu()

        if secim == '1':
            dosya_olustur()
        elif secim == '2':
            dosya_duzenle()
        elif secim == '3':
            dosya_sil()
        elif secim == '4':
            dosya_listele()
        elif secim == '5':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen 1-5 arasında bir değer girin.")


if __name__ == "__main__":
    main()
