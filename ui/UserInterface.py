import sqlite3

import customtkinter
from ui.handleUserInput import handleUserInput
from ui.UserInputs import UserInputs
from time import time
from tkinter import messagebox
import pandas as pd
import tkinter as tk
from functions.handleFiles import copyfile
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class UserInterface(customtkinter.CTk):
    WIDTH = 640
    HEIGHT = 320

    def __init__(self):
        super().__init__()
        self.timer = 0
        self.title("SQLite and MongoDb comparison ZTB")
        self.geometry(f"{UserInterface.WIDTH}x{UserInterface.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        #self.photo_image_sqlite = tk.PhotoImage(file='./img/sqlite.png')
        #self.photo_image_mongodb = tk.PhotoImage(file='./img/mongodb.png')

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Restore SQLite",
                                                command=self.restore_backup)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=25, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x11)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=2)
        self.frame_right.rowconfigure(10, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        # ============ frame_info ============

        # ============ frame_right ============

        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="Choose Options:")
        self.label_radio_group.grid(row=0, column=0, columnspan=2, pady=15, padx=15, sticky="")

        self.combobox_selected_db = customtkinter.CTkComboBox(master=self.frame_right,
                                                              values=["SQLite", "MongoDb"])
        self.combobox_selected_db.grid(row=1, column=0, columnspan=2, pady=15, padx=15, sticky="we")

        self.combobox_crud_method = customtkinter.CTkComboBox(master=self.frame_right,
                                                              values=["CREATE", "READ", "UPDATE", "DELETE"])
        self.combobox_crud_method.grid(row=2, column=0, columnspan=2, pady=15, padx=15, sticky="we")

        self.entry_records_ammount = customtkinter.CTkEntry(master=self.frame_right,
                                                            width=120,
                                                            placeholder_text="Records amount")
        self.entry_records_ammount.grid(row=0, column=0, columnspan=2, pady=15, padx=15, sticky="we")

        self.button_start = customtkinter.CTkButton(master=self.frame_right,
                                                    border_width=2,  # <- custom border_width
                                                    fg_color="grey",  # <- no fg_color
                                                    command=self.button_start,
                                                    text="Start")
        self.button_start.grid(row=10, column=0, columnspan=3, pady=15, padx=15, sticky="swe")

        # set default values
        self.combobox_selected_db.set("Select Database")
        self.combobox_crud_method.set("CRUD Operation")

    def button_start(self):
        x = self.get_user_inputs()
        # Na początku stworzyć backup
        time_start = time()
        handleUserInput(x)
        time_end = time()
        time_diff = time_end - time_start
        result = "Execution in sec: " + str(round(time_diff, 5))
        messagebox.showinfo("output",  result)
        if x.selected_database == "MongoDb":
            df = pd.read_csv("MongoDb.csv")
            new_row = {'Iterations': x.records_amount, 'Time': time_diff, 'Method': x.crud_method}
            df = df.append(new_row, ignore_index=True)
            df.to_csv('MongoDb.csv', index=False)
        else:
            df = pd.read_csv("SQLite.csv")
            new_row = {'Iterations': x.records_amount, 'Time': time_diff, 'Method': x.crud_method}
            df = df.append(new_row, ignore_index=True)
            df.to_csv('SQLite.csv', index=False)

    def restore_backup(self):
        copyfile("Backup/database.sqlite", "Reviews/database.sqlite", "Backup restored.")

    @staticmethod
    def change_appearance_mode(new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

    def get_user_inputs(self):
        return UserInputs(
            int(self.entry_records_ammount.get()),
            self.combobox_selected_db.get(),
            self.combobox_crud_method.get()
        )
