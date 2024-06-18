from tkinter import *
import customtkinter as s
from CTkListbox import CTkListbox
from tkinter import messagebox

# Create new task
def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Delete selected task
def deleteTaskAlternative():
    try:
        lb.delete(lb.curselection())
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Set the color theme
s.set_appearance_mode("dark")
s.set_default_color_theme("dark-blue")        

form = s.CTk()
form.geometry('350x320')
form.title('To-do-list')
form.resizable(False, False)

# Font for all objects
font = s.CTkFont(family="Bahnschrift", size=14)

# Listbox frame
frame = s.CTkFrame(form, width=300, height=200)
frame.place(relx=0.5, rely=0.34, anchor=CENTER)

# Tasks listbox
lb = CTkListbox(frame, width=260, height=170, font=font,highlight_color="#383838",hover_color="#292929",button_color="#252525")
lb.place(relx=0.5, rely=0.5, anchor=CENTER)

# Tasks entry
my_entry = s.CTkEntry(form,font=font,width=200,fg_color="#212121",border_color="#383838")
my_entry.place(relx=0.5, rely=0.72, anchor=CENTER)

# Buttons frame
frame2 = s.CTkFrame(form,width=280,height=40,corner_radius=20)
frame2.place(relx=0.5, rely=0.85, anchor=CENTER)

# Delete task button
addbtn = s.CTkButton(frame2, text='Add Task', font=font,width=130,border_color="#383838",border_width=2,fg_color="#282828",hover_color="#383838",corner_radius=20, command=newTask)
addbtn.place(relx=0.25, rely=0.5, anchor=CENTER)

# Add task button
delete_btn = s.CTkButton(frame2, text='Delete Task', font=font,width=130,border_color="#383838",border_width=2,fg_color="#282828",hover_color="#383838",corner_radius=20, command=deleteTaskAlternative)
delete_btn.place(relx=0.75, rely=0.5, anchor=CENTER)

form.mainloop()