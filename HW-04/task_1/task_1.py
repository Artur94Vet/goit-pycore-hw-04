import os

def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Видаляємо пробільні символи та символи нового рядка
                line = line.strip()
                if not line:
                    continue  # Пропускаємо порожні рядки
                parts = line.split(',')
                if len(parts) != 2:
                    continue  # Пропускаємо рядки з некоректним форматом
                try:
                    salary = float(parts[1])
                except ValueError:
                    continue  # Якщо зарплату неможливо конвертувати в число, пропускаємо рядок
                total += salary
                count += 1
    except FileNotFoundError:
        print("Файл не знайдено!")
        return (0, 0)
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return (0, 0)
    
    average = total / count if count else 0
    return (total, average)

if __name__ == '__main__':
    # Отримуємо абсолютний шлях до директорії, де знаходиться цей скрипт
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Якщо файл знаходиться в тій же папці, просто вкажіть його ім'я
    file_name = "salary_file.txt"
    # Якщо файл у підпапці (наприклад, "task_1"), можна написати:
    # file_name = os.path.join("task_1", "salary_file.txt")
    file_path = os.path.join(base_dir, file_name)
    
    total, average = total_salary(file_path)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
