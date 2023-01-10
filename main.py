import bitlyshortener
from tkinter import *
from dotenv import load_dotenv
import os

load_dotenv()


def url_shortener():
    '''
    Main function, that goes to bilty.com API, and converts long URL to short URL.
    '''
    url = entry_long_url.get()  # Gets long URL from user
    access_tokens = [os.getenv('API_KEY')]  # Your API_KEY from .env file
    shortener = bitlyshortener.Shortener(tokens=access_tokens)
    short_url = shortener._shorten_url(url)  # Makes short URL
    label2.configure(text=f'{short_url}')  # Displays short URL in label2
    label2.clipboard_append(short_url)  # Places short URL on the clipboard


def delete():
    '''
    Clears entry (with long link) label 
    and label with generated short link
    '''
    entry_long_url.delete(0, END)
    label2.config(text='.....')
    label2.clipboard_clear()


window = Tk()  # main window of URL-shortener
window.title('URL SHORTENER')
window.geometry('710x101')
window.resizable(False, False)

label_1 = Label(window, text='Enter your long URL')
label_1.place(x=10, y=4)

long_url_window = StringVar()
entry_long_url = Entry(window, width=54, textvariable=long_url_window)
entry_long_url.pack()
entry_long_url.place(x=10, y=30)

print_short_url = '.....'
label2 = Label(text=print_short_url, font=('Roboto', 15))
label2.place(x=12, y=65)

button_convert = Button(window, text='Convert and copy URL',
                        width=17, command=url_shortener)
button_convert.place(x=513, y=28)

exit_button = Button(window, text="Exit", width=17, command=window.destroy)
exit_button.place(x=513, y=63)


clear_laber = Button(window, text="Clear all", width=10, command=delete)
clear_laber.place(x=382, y=63)


if __name__ == '__main__':

    window.mainloop()
