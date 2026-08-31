"""
Undo/Redo Problem Statement

Think of a text editor like MS Word or google docs

When you type, delete or format text, the editor saves a "snapshot" of what the document looks like
after each action.

This way when you press CTRL+Z (undo), the editor can bring back the previous version of your document

######### Below structure can be defined as #############

Originator: This is the main object whose data you want to save and bring back later.
Think of it as the TextEditor that holds your content

Memento: This act like a snapshot or save point that captures the originator's data at a specific moment. TextMemento class

Caretaker: This is the manager that keeps all the snapshots safe and organized. It does not change the snapshots, just store them and gives them back when you need them. Think of it as the History class

"""
from typing import List

class TextMemento:
    def __init__(self,text):
        self.__saved_text = text

    def get_saved_text(self):
        return self.__saved_text
    
class TextEditor:
    def __init__(self):
        self.__text = ""

    def write(self,new_text):
        self.__text += new_text

    def get_text(self)-> str:
        return self.__text

    def save(self) -> TextMemento:
        return TextMemento(self.__text)

    def restore(self,tm:TextMemento):
        self.__text = tm.get_saved_text()

class History:
    def __init__(self):
        self.__history: List[TextMemento] = []

    def save_state(self,tm: TextMemento):
        self.__history.append(tm)

    def undo(self):
        if self.__history:
            self.__history.pop()
            if self.__history:
                return self.__history[-1]
            else:
                return TextMemento("")
        else:
            return TextMemento("")

    def get_history(self):
        for i in range(len(self.__history)):
            print(f"{i} = {self.__history[i].get_saved_text()}")

    




# creating object
text_editor = TextEditor()
history = History()
text_editor.write("Hello")
text_editor.write(" World")
history.save_state(text_editor.save())
text_editor.write(" Good")
text_editor.write(" Bye")
history.save_state(text_editor.save())
history.get_history()
print("------------")
text_editor.restore(history.undo())
history.get_history()
print(text_editor.get_text())