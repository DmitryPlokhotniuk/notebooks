import json
from datetime import datetime


def save_note(notes, file_path):
    with open(file_path, 'w') as file:
        json.dump(notes, file, indent=4)


def load_note(file_path):
    with open(file_path, 'r') as file:
        notes = json.load(file)
        return notes


def add_note(notes, new_note):
    max_id = max(note['id'] for note in notes) if notes else 0
    new_note['id'] = max_id + 1
    notes.append(new_note)
    print(f"Добавлена новая заметка с ID: {new_note['id']}")
    print()


def edit_note(notes, note_id, new_title=None, new_body=None, new_datatime=None):
    for note in notes:
        if note['id'] == note_id:
            if new_title:
                note['title'] = new_title
            if new_body:
                note['body'] = new_body
            if new_datatime:
                note['datetime'] = new_datatime
            print(f"Заметка с ID: {note_id} была изменена \n")
            break


def delete_note(notes, note_id):
    notes[:] = [note for note in notes if note['id'] != note_id]
    print(f"Заметка с ID: {note_id} удалена.")
    print()


def main():
    file_path = 'notes.txt'
    notes = load_note(file_path)

    while True:
        print('1. Вывести все заметки')
        print('2. Добавить заметку')
        print('3. Редактировать заметку')
        print('4. Удалить заметку')
        print('5. Выйти')

        choice = input('Выберите действие: ')

        if choice == '1':
            print('Заметки: \n')
            notes = sorted(notes,
                           key=lambda x: datetime.strptime(x['datetime'], '%Y-%m-%d %H:%M:%S'), reverse=False)
            for note in notes:
                print(f"ID: {note['id']}")
                print(f"Заголовок: {note['title']}")
                print(f"Текст: {note['body']}")
                print(f"Дата/время: {note['datetime']}")
                print()
        elif choice == '2':
            title = input('Введите заголовок заметки: ')
            body = input('Введите текст заметки: ')
            # datetime = input('Введите дату/время заметки (в формате "гггг-мм-дд чч:мм:сс")')
            date_time: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            new_note = {
                'title': title,
                'body': body,
                'datetime': date_time
            }

            add_note(notes, new_note)
            save_note(notes, file_path)

        elif choice == '3':
            note_id = int(input('Введите ID заметки для редактирования: '))
            new_title = input('Введите новый заголовок заметки (или оставьте пустым): ')
            new_body = input('Ведите новый текст заметки (или оставьте пустым): ')
            # new_datatime = input('Введите новую дату/время заметки (или оставьте пустым): ')
            new_date_time: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            edit_note(notes, note_id, new_title, new_body, new_date_time)
            save_note(notes, file_path)
        elif choice == '4':
            note_id = int(input('Введите Id заметки для удаления: '))

            delete_note(notes, note_id)
            save_note(notes, file_path)
        elif choice == '5':
            break
        else:
            print('Неверный выбор. Попробуйте еще раз.')


if __name__ == '__main__':
    main()
