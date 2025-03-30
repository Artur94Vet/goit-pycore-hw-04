import os

def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Пропускаємо порожні рядки
                parts = line.split(',')
                if len(parts) != 3:
                    print(f"Невірний формат рядка: {line}")
                    continue  # Пропускаємо рядки з некоректним форматом
                cat = {
                    "id": parts[0],
                    "name": parts[1],
                    "age": parts[2]
                }
                cats.append(cat)
    except FileNotFoundError:
        print("Файл не знайдено!")
    except Exception as e:
        print(f"Виникла помилка: {e}")
    return cats

if __name__ == '__main__':
    # Отримуємо абсолютний шлях до директорії, де знаходиться цей скрипт (тобто папка task_2)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Оскільки файл cats_file.txt знаходиться в тій же директорії, просто використовуємо його ім'я
    file_path = os.path.join(base_dir, "cats_file.txt")
    
print("Шлях до файлу:", file_path)
cats_info = get_cats_info(file_path)
print("Фінальний результат:")
for cat in cats_info:
    print(f"{cat['id']},{cat['name']},{cat['age']}")
