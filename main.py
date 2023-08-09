from note import Note
from datetime import datetime
import json
import uuid


file_path = 'notes.json'
try:
    notes = []
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)  
        for item in data:
            note = Note(id=item["id"], title=item["title"], text=item["text"], date_time=item["date"])  
            notes.append(note)
except json.decoder.JSONDecodeError as e:
        notes = []

def write_notes(array):
    data = []
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in array:
            note =  {"id": item.id, "title": item.title, "text": item.text, "date": item.date_time}
            data.append(note)
        json.dump(data, file, ensure_ascii=False, indent=4)
    file.close           

def note_all(array):
    for note in array:
        print(f"\n{note.id}. {note.title} ({note.date_time}):\n\t {note.text}")
    
def note_add(array):

    title = input("\nВведите заголовок заметки: ")
    text = input("Введите текст заметки: ")    
    date_time = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    id = str(uuid.uuid1())[0:3]
    note = Note(id, title, text, date_time)
    array.append(note)
    write_notes(array)
    print("\nВаша заметка успешно добавлена!")

def note_edit(array):
    id = input("\nВведите идентификатор заметки, которую хотите редактировать: ")
    flag = False
    for note in array:
        if Note.get_id(note) == id:
            flag = True
            print(f"Редактирование заметки: {note.title}")
            title = input("\nВведите новый заголовок заметки (или оставьте поле пустым, если не хотите менять): ")
            text = input("Введите новый текст заметки (или оставьте поле пустым, если не хотите менять): ")
            if title:
                note.title = title
            if text:
                note.text = text
            if (title  or text):
                note.date_time = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))   
            write_notes(array)
            print("\nВаша заметка успешно отредактирована!")
    if not flag:
        print('Такой заметки нет')

def note_delete(array):
    id = input("\nВведите идентификатор заметки, которую хотите удалить: ")
    flag = False
    for note in array:
        if Note.get_id(note) == id:
            flag = True
            print(f"Удаление заметки: {note.title}")
            notes.remove(note)   
            write_notes(array)
            print("\nВаша заметка успешно удалена!")
    if not flag:
        print('Заметка не найдена')

def note_list(array):
    date = input("\nВведите дату в формате дд.мм.гггг для выбора заметок: ")
    filter = datetime.strptime(date, "%d.%m.%Y")
    flag = False
    for note in notes:
        if datetime.strptime(note.date_time, "%d.%m.%Y %H:%M:%S").date() == filter.date():
            print(f"\n{note.id}. {note.title} ({note.date_time}):\n\t {note.text}")
            flag = True
    if not flag: 
        print('Нет заметок для отображения')

print("   Главное меню:\n")
print("1. Вывод всех заметок")
print("2. Добавление новой заметки")
print("3. Редактирование заметки")
print("4. Удаление заметки")
print("5. Выборка заметок по дате")
print("6. Выход")
choice = int(input("Выберите действие: "))

match choice:
    case 1:
        note_all(notes)
        print()
    case 2:
        note_add(notes)
        print() 
    case 3:
        note_edit(notes)
        print()
    case 4:
        note_delete(notes)
        print()
    case 5:
        note_list(notes)
        print()
    case 6:
        print()             
                    
    case _:
        print("Ошибка ввода")

