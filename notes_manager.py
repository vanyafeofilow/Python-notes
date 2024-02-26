# notes_manager.py

import json
from datetime import datetime
from note import Note

class NotesManager:
    def __init__(self):
        self.notes = []

    def create_note(self, title, body):
        note_id = len(self.notes) + 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_note = Note(note_id, title, body, timestamp)
        self.notes.append(new_note)
        return new_note
    
    def edit_note(self, note_id, title, body):
        for note in self.notes:
            if note.note_id == note_id:
                note.title = title
                note.body = body
                note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                return True
        return False

    def delete_note(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                self.notes.remove(note)
                return True
        return False

    def save_notes_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                notes_data = []
                for note in self.notes:
                    notes_data.append({
                        'note_id': note.note_id,
                        'title': note.title,
                        'body': note.body,
                        'timestamp': note.timestamp
                    })
                json.dump(notes_data, file)
            print("Заметки успешно сохранены в файле.")
        except Exception as e:
            print(f"Произошла ошибка при сохранении заметок в файл: {e}")

    def load_notes_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                notes_data = json.load(file)
                self.notes = []
                for data in notes_data:
                    self.notes.append(Note(data['note_id'], data['title'], data['body'], data['timestamp']))
        except FileNotFoundError:
            # Если файл не существует, создаем пустой список заметок
            self.notes = []

    def print_single_note(self, note_id):
        found_note = next((note for note in self.notes if note.note_id == note_id), None)
        if found_note:
            print(f"ID: {found_note.note_id}, Время: {found_note.timestamp}, Заголовок: {found_note.title}, Текст: {found_note.body}")
        else:
            print("Заметка с указанным ID не найдена.")

    def print_all_notes(self):
        if not self.notes:
            print("Нет доступных заметок.")
        else:
            sorted_notes = sorted(self.notes, key=lambda x: x.timestamp)
            print("Список всех заметок:")
            for note in sorted_notes:
                print(f"ID: {note.note_id}, Время: {note.timestamp}, Заголовок: {note.title}, Текст: {note.body}")