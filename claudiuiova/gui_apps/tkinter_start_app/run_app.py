import tkinter as tk
import functools
from claudiuiova.gui_apps.utils.get_words import Words
from tkinter.messagebox import showerror


class WordMakerInterface(object):

    def __init__(self, root, geometry="480x200", resizable=False):
        self.grid_params = ['column', 'row', 'columnspan', 'rowspan']
        self.root = root
        self.root.geometry(geometry)

        if not resizable:
            self.root.resizable()
        else:
            self.root.resizable(resizable)

    def create_frame_and_pack(self, side=tk.TOP, **kwargs):
        frame = tk.Frame(self.root, **kwargs)
        frame.pack(side=side)
        return frame

    def create_label_and_pack(self, window, text='', **kwargs):
        label = tk.Label(window, text=text)
        if any(x in kwargs for x in self.grid_params):
            label.grid(**kwargs)
        else:
            label.pack()

    def create_entry_and_pack(self, window, **kwargs):
        entry = tk.Entry(window)
        if any(x in kwargs for x in self.grid_params):
            entry.grid(**kwargs)
        else:
            entry.pack()

        return entry

    def create_button_and_pack(self, window, command, text='', **kwargs):
        button = tk.Button(window, text=text, command=command)
        if any(x in kwargs for x in self.grid_params):
            button.grid(**kwargs)
        else:
            button.pack()


def get_entry_value(entry):
    return entry.get()


def get_all_entry_values(*args):
    return tuple([get_entry_value(x) for x in args])


def destroy_frame_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def show_words(frame, text_input, length_input):
    random_string, word_length = get_all_entry_values(text_input, length_input)

    # delete current results
    destroy_frame_widgets(frame)

    result_label = tk.Label(frame, text="Results")
    result_label.grid(row=0, column=0, columnspan=3)

    try:
        randomly_constructed_words = Words(random_string, int(word_length))
        english_words = randomly_constructed_words.get_english_words_with_multiprocessing()
        max_lines = 3
        lines_index = list(range(1, max_lines + 1)) if max_lines > len(english_words) else \
            list(range(1, max_lines + 1)) * \
            (len(english_words) // max_lines) + list(range(1, (len(english_words) % max_lines) + 1))

        columns_index = [x for y in range(len(english_words) // max_lines + 1) for x in [y] * max_lines]

        for line_index, word in enumerate(english_words):
            result = tk.Label(frame, text=word, borderwidth=2, relief="groove", anchor=tk.W, justify=tk.LEFT)
            result.grid(row=lines_index[line_index], column=columns_index[line_index])
    except ValueError:
        showerror("Integer Required", "Please insert a number as length! Ty bro!")


if __name__ == "__main__":
    my_root = tk.Tk()
    app = WordMakerInterface(my_root)
    widgets_frame = app.create_frame_and_pack()

    separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)
    separator.pack(fill=tk.X, padx=5, pady=5)

    result_frame = app.create_frame_and_pack(height=437, width=480)
    app.create_label_and_pack(widgets_frame, text="Insert the random string", column=0, row=0)
    random_string_input = app.create_entry_and_pack(widgets_frame, column=1, row=0)

    app.create_label_and_pack(widgets_frame, text="Insert the word length", column=0, row=1)
    word_length_input = app.create_entry_and_pack(widgets_frame, column=1, row=1)

    app.create_button_and_pack(widgets_frame, text="Create", column=2, row=0, columnspan=2, rowspan=2, sticky='NSEW',
                               command=functools.partial(show_words, *[result_frame,
                                                                       random_string_input, word_length_input]))

    my_root.mainloop()
