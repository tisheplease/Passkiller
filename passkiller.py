import hashlib
import secrets
import string
import bcrypt
import os
import pyfiglet
from termcolor import colored

def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_art = pyfiglet.figlet_format("PASSKILLER", font="doom")
    print(colored("===========================================================", "red"))
    print(colored(ascii_art, "red"))
    print(colored("       Password Security Toolkit by @tisheplease", "red"))
    print(colored("===========================================================", "red"))
    print(colored("1. Генератор паролей       | 4. Подбор пароля к хэшу", "red"))
    print(colored("2. Проверка пароля         | 5. База утечек", "red"))
    print(colored("3. Хэширование пароля      | 6. Выход", "red"))
    print(colored("===========================================================", "red"))

def generate_password():
    length = int(input("Введите длину пароля: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    print(colored(f"Сгенерированный пароль: {password}", "green"))

def check_password():
    password = input("Введите пароль для проверки: ")
    score = 0
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    if len(password) >= 12:
        score += 1
    levels = ["Очень слабый", "Слабый", "Средний", "Сильный", "Очень сильный"]
    print(colored(f"Сложность пароля: {levels[score]}", "green" if score > 2 else "red"))

def hash_password():
    password = input("Введите пароль для хэширования: ")
    method = input("Выберите алгоритм (md5, sha256, bcrypt): ").lower()
    if method == "md5":
        print(colored(f"MD5: {hashlib.md5(password.encode()).hexdigest()}", "green"))
    elif method == "sha256":
        print(colored(f"SHA-256: {hashlib.sha256(password.encode()).hexdigest()}", "green"))
    elif method == "bcrypt":
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        print(colored(f"Bcrypt: {hashed.decode()}", "green"))
    else:
        print(colored("Некорректный алгоритм!", "red"))

def brute_force():
    hash_to_crack = input("Введите хэш (MD5) для подбора: ")
    dict_file = input("Введите путь к словарю: ")
    try:
        with open(dict_file, "r", encoding="utf-8") as f:
            for line in f:
                password = line.strip()
                if hashlib.md5(password.encode()).hexdigest() == hash_to_crack:
                    print(colored(f"Пароль найден: {password}", "green"))
                    return
        print(colored("Пароль не найден в словаре.", "red"))
    except FileNotFoundError:
        print(colored("Файл словаря не найден!", "red"))

def main():
    while True:
        show_menu()
        choice = input("Выберите опцию: ")
        if choice == "1":
            generate_password()
        elif choice == "2":
            check_password()
        elif choice == "3":
            hash_password()
        elif choice == "4":
            brute_force()
        elif choice == "5":
            print(colored("Функция проверки базы утечек в разработке...", "yellow"))
        elif choice == "6":
            print(colored("Выход из программы...", "yellow"))
            break
        else:
            print(colored("Неверный выбор, попробуйте снова.", "red"))
        input("Нажмите Enter, чтобы вернуться в меню...")

if __name__ == "__main__":
    main()
