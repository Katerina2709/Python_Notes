from datetime import datetime

class Note:
    def __init__(self, id, title, text, date_time):
        self.id =  id 
        self.title = title
        self.text = text
        self.date_time = date_time
      
    def get_id(note):
        return note.id

    def get_title(note):
        return note.title

    def get_text(note):
        return note.text

    def get_date(note):
        return note.datetime

    def set_title(note, title):
        note.title = title

    def set_text(note, text):
        note.text = text

    def set_date(note):
        note.date_time = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

   

    