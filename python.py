import os,time, sys
from colorama import Fore, Back,Style
from PIL import Image
from strConst import *


def webp_converter(choice: chr, files: list, source: str,  des: str):
    
    
    if choice in ['a', 'A']:
        for file in files:
            try:
                name = file.split(".")[0]
                img = Image.open(source + "/" + file).convert(RGB)
                img.save(des + "/" + name + '.png', 'png')
                print(Fore.GREEN + f"[OK] {name}.png")
                print(Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"[ERROR] {file}")
                print(Style.RESET_ALL)
        sys.exit(0)
            
            
    if choice in ['b', 'B']:
        for file in files:
            try:
                name = file.split(".")[0]
                img = Image.open(source + "/" + file).convert(RGB)
                img.save(des + "/" + name + '.jpg', 'jpeg')
                print(Fore.GREEN + f"[OK] {name}.jpg")
                print(Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"[ERROR] {file}")
                print(Style.RESET_ALL)
        sys.exit(0)
   
            
def png_converter(choice: chr, files: list, source: str,  des: str):
    if choice in ['a', 'A']:
        for file in files:
            try:
                name = file.split(".")[0]
                img = Image.open(source + "/" + file).convert(RGB)
                img.save(des + "/" + name + '.jpg', 'jpeg')
                print(Fore.GREEN + f"[OK] {name}.jpg")
                print(Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"[ERROR] {file}")
                print(Style.RESET_ALL)
        sys.exit(0)
            
            
    if choice in ['b', 'B']:
        for file in files:
            try:
                name = file.split(".")[0]
                img = Image.open(source + "/" + file).convert(RGB)
                img.save(des + "/" + name + '.webp', 'webp')
                print(Fore.GREEN + f"[OK] {name}.webp")
                print(Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"[ERROR] {file}")
                print(Style.RESET_ALL)
        sys.exit(0)
                
                
def jpg_converter(choice: chr, files: list, source: str,  des: str):
    
    if choice in ['a', 'A']:
        for file in files:
            try:
                name = file.split(".")[0]
                img = Image.open(source + "/" + file).convert(RGB)
                img.save(des + "/" + name + '.png', 'png')
                print(Fore.GREEN + f"[OK] {name}.png")
                print(Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"[ERROR] {file}")
                print(Style.RESET_ALL)
        sys.exit(0)
            
            
    if choice in ['b', 'B']:
        for file in files:
            try:
                name = file.split(".")[0]
                img = Image.open(source + "/" +file).convert(RGB)
                img.save(des + "/" + name + '.webp', 'webp')
                print(Fore.GREEN + f"[OK] {name}.webp")
                print(Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"[ERROR] {file}")
                print(Style.RESET_ALL)
        sys.exit(0)


def crawl_on_files(source: str) :
    # Crawl on files
    files  = os.listdir(source)
    if not files:
        print(Fore.LIGHTRED_EX + ERROR_404_FILES)
        print(Style.RESET_ALL)
        sys.exit(0)
        
    # Show files
    for i in files:
        print(Fore.CYAN + i)
        print(Style.RESET_ALL)
        
        
    print(PLEASE_WAIT)
    time.sleep(5)
    os.system('cls')
    
    return files


def main():
    
    print(Fore.LIGHTBLUE_EX)
    source: str = input(SOURCE)
    destination: str = input(DESTINATION)
    print(Style.RESET_ALL)
    
    
    files = crawl_on_files(source)
    type_of_file = files[0].split(".")[1] # Find type of file
    
    
    if type_of_file == PNG:
        print(Fore.LIGHTMAGENTA_EX)
        print(PNG_TEXT)
        print(Style.RESET_ALL)
        choice = input(CHOICE)
        
        if choice not in ['a', 'A', 'b', 'B']:
            print(Fore.RED + ERROR_CORRECT_CHOICE)
            print(Style.RESET_ALL)
            sys.exit(0)
        else:
            png_converter(choice, files, source, destination)
    
    if type_of_file == JPG:
        print(Fore.LIGHTMAGENTA_EX)
        print(JPG_TEXT)
        print(Style.RESET_ALL)
        choice = input(CHOICE)
        
        if choice not in ['a', 'A', 'b', 'B']:
            print(Fore.RED + ERROR_CORRECT_CHOICE)
            print(Style.RESET_ALL)
            sys.exit(0)
        else:
            jpg_converter(choice, files, source, destination)
    
    if type_of_file == WEBP:
        print(Fore.LIGHTMAGENTA_EX)
        print(WEBP_TEXT)
        print(Style.RESET_ALL)
        choice = input(CHOICE)
        
        if choice not in ['a', 'A', 'b', 'B']:
            print(Fore.RED + ERROR_CORRECT_CHOICE)
            print(Style.RESET_ALL)
            sys.exit(0)
        else:
            webp_converter(choice, files, source, destination)
    

if __name__ == "__main__":
    main()