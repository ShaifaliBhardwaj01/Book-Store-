from tkinter import *
import backend

global selected_tuple


def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        if index:
            selected_tuple = list1.get(index)
            # print(selected_tuple)
        # return selected_tuple
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)


def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


window = Tk()

window.wm_title("Book Store")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, text=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, text=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, text=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, text=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview())

# bind a method to a list
list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)
b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)
b3 = Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=4, column=3)
b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)
b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)
b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
