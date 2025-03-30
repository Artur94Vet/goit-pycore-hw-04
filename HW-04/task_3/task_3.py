#!/usr/bin/env python3
import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama
init(autoreset=True)

def print_directory_tree(path: Path, indent: int = 0):
    """Рекурсивна функція для виведення структури директорії."""
    prefix = " " * indent
    if path.is_dir():
        print(prefix + Fore.BLUE + f"📂 {path.name}" + Style.RESET_ALL)
        for item in sorted(path.iterdir(), key=lambda x: x.name):
            print_directory_tree(item, indent + 4)
    else:
        print(prefix + Fore.GREEN + f"📜 {path.name}" + Style.RESET_ALL)

if __name__ == "__main__":
    # Отримуємо директорію, де знаходиться скрипт
    base_dir = Path(__file__).parent

    # Якщо аргумент не передано, використовуємо папку "picture" в тій же директорії
    if len(sys.argv) < 2:
        target_dir = base_dir / "picture"
    else:
        target_dir = Path(sys.argv[1])
    
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Помилка: {target_dir} не існує або не є директорією.")
        sys.exit(1)
    
    print("Структура директорії:")
    print_directory_tree(target_dir)
