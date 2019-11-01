import tkinter as tk
from tkinter import messagebox as msg
from tkinter.ttk import Notebook

import requests

#clase
class TranslateBook(tk.Tk):

    #funcion inicial
    def __init__(self):
        super().__init__()

        #titulo y tamaño de la ventana
        self.title("Translation Book v1")
        self.geometry("500x300")

        #metodo Notebook son fichas, coleccion de paginas
        #dentro de una variabe, en un tiempo no definido
        self.notebook = Notebook(self)

        #creacion de las pestañas English_Frame e Italian_Fram
        #metodos que se les da a las fichas
        english_tab = tk.Frame(self.notebook)
        italian_tab = tk.Frame(self.notebook)

        #creacion del boton de traducir en English_Frame,
        #ejecuta el metodo traslate
        self.translate_button = tk.Button(english_tab, text="Translate", command=self.translate)
        self.translate_button.pack(side=tk.BOTTOM, fill=tk.X)

        #caja de texto en el English_Frame
        self.english_entry = tk.Text(english_tab, bg="white", fg="black")
        self.english_entry.pack(side=tk.TOP, expand=1)

        #boton de copiar en el Italian_Frame con el metodo copy_to_clipboard
        #hacer referencia al metodo copy_to_clipboard
        self.italian_copy_button = tk.Button(italian_tab, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.italian_copy_button.pack(side=tk.BOTTOM, fill=tk.X)

        #impresion de la traducccion
        #re recibe texto entonces debe ser una variable tipo String
        self.italian_translation = tk.StringVar(italian_tab)
        self.italian_translation.set("")

        self.italian_label = tk.Label(italian_tab, textvar=self.italian_translation, bg="lightgrey", fg="black")
        self.italian_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        #nombre de las pestañas o frames
        self.notebook.add(english_tab, text="Ingles")
        self.notebook.add(italian_tab, text="Italiano")

        self.notebook.pack(fill=tk.BOTH, expand=1)

    #funcion traslate
    def translate(self, target_language="it", text=None):
        if not text:
            text = self.english_entry.get(1.0, tk.END)

        url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl={}&tl={}&dt=t&q={}".format("en", target_language, text)

        try:
            r = requests.get(url)
            #raise_for_status es para saber que ha pasado con la url(r)
            r.raise_for_status()
            translation = r.json()[0][0][0]
            self.italian_translation.set(translation)
            msg.showinfo("Translation Successful", "Text successfully translated")
        except Exception as e:
            msg.showerror("Translation Failed", str(e))

    def copy_to_clipboard(self, text=None):
        if not text:
            text = self.italian_translation.get()

        self.clipboard_clear()
        self.clipboard_append(text)
        msg.showinfo("Copied Successfully", "Text copied to clipboard")


if __name__ == "__main__":
    translatebook = TranslateBook()
    translatebook.mainloop()
