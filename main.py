def add_note():
    title = input("Введите заголовок заметки: ")
    text = input("Введите текст заметки: ")
    
    try:
        with open("notes.txt", "a", encoding="utf-8") as file:
            file.write(f"=== Заголовок: {title} ===\n")
            file.write(f"{text}\n")
            file.write("-" * 20 + "\n\n")
        print("Заметка сохранена!")
    except PermissionError:
        print("Ошибка: нет прав для записи в файл.")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")


while True:
    print("\n1. Добавить заметку")
    print("2. Показать все заметки")
    print("3. Выйти")
    choice = input("Выберите действие: ")
    if choice == "1":
        add_note()
    elif choice == "2":
        show_notes()
    elif choice == "3":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")
