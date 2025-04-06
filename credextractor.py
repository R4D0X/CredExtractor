import re
import os
from colorama import Fore, Style, init
from tkinter import Tk, filedialog

init(autoreset=True)

def print_ascii_art():
    ascii_art = """
       /$$                      /$$ /$$
      | $$                     |__/| $$   
  /$$$$$$$  /$$$$$$  /$$    /$$ /$$| $$ /$$$$$$$$
 /$$__  $$ /$$__  $$|  $$  /$$/| $$| $$|____ /$$/ 
| $$  | $$| $$$$$$$$ \\  $$/$$/ | $$| $$   /$$$$/
| $$  | $$| $$_____/  \\  $$$/  | $$| $$  /$$__/
|  $$$$$$$|  $$$$$$$   \\  $/   | $$| $$ /$$$$$$$$
 \\_______/ \\_______/    \\_/    |__/|__/|________/

# spyhackerz.org special thanks my best friend radoxin 
    """
    print(ascii_art)

def extract_credentials(input_file, output_file):
    pattern = r"https?://([^\s:]+):2083:([^\s:]+):([^\s]+)"
    
    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as file:
            with open(output_file, 'w', encoding='utf-8') as outfile:
                found = False
                for line in file:
                    matches = re.findall(pattern, line)
                    if matches:
                        found = True
                        for match in matches:
                            url, username, password = match
                            outfile.write(f"{url},{username},{password}\n")
                
                if not found:
                    print(Style.BRIGHT + Fore.LIGHTRED_EX)
                    print(f"Hata: Dosyada eşleşen veri bulunamadı.")
                    print("Devilz-Spyhackerz.org")

        if found:
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX)
            print(f"İşlem tamamlandı. Sonuçlar {output_file} dosyasına kaydedildi.")
            print("Devilz-Spyhackerz.org")

    except Exception as e:
        print(Style.BRIGHT + Fore.LIGHTRED_EX)
        print(f"Hata: {str(e)}")
        print("Devilz-Spyhackerz.org")

def select_input_file():
    """GUI kullanarak dosya seçimi yapılacak fonksiyon"""
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Bir dosya seçin", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    return file_path

def main():
    print_ascii_art()

    print(Style.BRIGHT + Fore.MAGENTA)
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Dosya seçiliyor...")

    input_file = select_input_file()
    if not input_file:
        print(Style.BRIGHT + Fore.LIGHTRED_EX)
        print("Hata: Dosya seçilmedi.")
        print("Devilz-Spyhackerz.org")
        return
    
    output_file = "Combined.txt"
    if not os.path.isfile(input_file):
        print(Style.BRIGHT + Fore.LIGHTRED_EX)
        print(f"Hata: {input_file} bulunamadı.")
        print("Devilz-Spyhackerz.org")
        return
    extract_credentials(input_file, output_file)

if __name__ == "__main__":
    main()
