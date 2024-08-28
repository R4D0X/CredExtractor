import re
import os
import colorama
from colorama import Fore, Style

colorama.init()

def extract_credentials(input_file, output_file):

    pattern = r"URL:\shttps?://(.*?)(/|\r)\nUsername:\s(.*?)[|\r]\nPassword:\s(.*?)[|\r]\n"
    
    with open(input_file, 'r') as file:
        content = file.read()
        matches = re.findall(pattern, content, re.IGNORECASE)
        
    with open(output_file, 'w') as outfile:
        for match in matches:
            url, _, username, password = match
            outfile.write(f"{url},{username},{password}\n")
    
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX)
    print(f"İşlem tamamlandı. Sonuçlar {output_file} dosyasına kaydedildi.")

def main():
    os.system("apt install figlet -y")
    os.system("clear")
    print(Style.BRIGHT + Fore.MAGENTA)
    os.system("figlet -f mono12 R4D0X")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Bir dosya giriniz: ", end="")
    input_file = input(Fore.LIGHTBLUE_EX + Style.NORMAL)
    output_file = "Combined.csv"
    
    if not os.path.isfile(input_file):
        print(Style.BRIGHT + Fore.LIGHTRED_EX)
        print(f"Hata: {input_file} bulunamadı.")
        return
    
    extract_credentials(input_file, output_file)

if __name__ == "__main__":
    main()
