# main.py

from notes_manager import NotesManager

def print_menu():
    print("-------------------------")
    print("1. Создать новую заметку")
    print("2. Редактировать заметку")
    print("3. Удалить заметку")
    print("4. Сохранить заметки в файл")
    print("5. Загрузить заметки из файла")
    print("6. Вывести заметку по ID")
    print("7. Вывести все заметки")
    print("8. Выйти")
    print("-------------------------")

def main():
    notes_manager = NotesManager()

    while True:
        print_menu()
        choice = input("Выберите действие (1-8): ")

        if choice == '1':
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            notes_manager.create_note(title, body)
            print("Заметка создана!")

        elif choice == '2':
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            if notes_manager.edit_note(note_id, title, body):
                print("Заметка отредактирована!")
            else:
                print("Заметка с указанным ID не найдена.")

        elif choice == '3':
            note_id = int(input("Введите ID заметки для удаления: "))
            if notes_manager.delete_note(note_id):
                print("Заметка удалена!")
            else:
                print("Заметка с указанным ID не найдена.")

        elif choice == '4':
            filename = input("Введите имя файла для сохранения заметок: ")
            notes_manager.save_notes_to_file(filename)
            print("Заметки сохранены в файле.")

        elif choice == '5':
            filename = input("Введите имя файла для загрузки заметок: ")
            notes_manager.load_notes_from_file(filename)
            print("Заметки загружены из файла.")

        elif choice == '6':
            note_id = int(input("Введите ID заметки для вывода: "))
            notes_manager.print_single_note(note_id)

        elif choice == '7':
            notes_manager.print_all_notes()

        elif choice == '8':
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, выберите от 1 до 8.")

if __name__ == "__main__":
    main()