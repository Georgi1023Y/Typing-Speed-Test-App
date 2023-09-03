import tkinter as tk
import random
import time

# Importing text data from the 'texts' module
from texts import short_texts

# Sets starting time with no value and empty string for random text
random_text = ""
start_time = None


# Function that gets random text from texts.py file. Texts are saved as Python list
def get_random_text():
    global random_text
    random_text = random.choice(short_texts)
    text_label.config(text=random_text)


# Functionality and logic
# Function that starts the typing test.
def start_typing_test():
    global start_time
    start_time = time.time()
    input_text.config(state=tk.NORMAL)
    input_text.delete(1.0, tk.END)
    input_text.focus_set()
    start_button.config(state=tk.DISABLED)
    submit_button.config(state=tk.DISABLED)  # Disable the Submit button when the test starts
    return get_random_text()


# Function that calculates typing speed of the user
def calculate_typing_speed():
    global start_time
    end_time = time.time()
    entered_text = input_text.get(1.0, tk.END)
    words = entered_text.split()
    num_words = len(words)
    elapsed_time = end_time - start_time

    # Calculates words per minute (WPM)
    words_per_minute = int((num_words / elapsed_time) * 60)

    result_label.config(text=f"Your typing speed is: {words_per_minute} words per minute")
    input_text.config(state=tk.DISABLED)
    submit_button.config(state=tk.DISABLED)  # Disables the Submit button after displaying the result
    start_button.config(state=tk.NORMAL)  # Enables the start button after displaying the result


# Function to check if text has been entered and enable/disable the Submit button accordingly
def check_text_entry(event):
    text = input_text.get(1.0, tk.END)
    text = text.strip()  # Remove leading and trailing whitespace
    if text:
        submit_button.config(state=tk.NORMAL)
    else:
        submit_button.config(state=tk.DISABLED)


# Creates the main window of Typing Speed Test App
root = tk.Tk()
root.title("Typing Speed Test")

# Creates all other elements of the application
# Shows instructions, so the user can understand what to do
instruction_label = tk.Label(root, text="Please type the following text as fast as you can:")
instruction_label.pack()

# Shows the randomly chosen text that the user will need to type
text_label = tk.Label(root, text=random_text)
text_label.pack()

# User will type here
input_text = tk.Text(root, height=5, width=40)
input_text.pack()
input_text.config(state=tk.DISABLED)

# Starts the typing test
start_button = tk.Button(root, text="Start Typing Test", command=start_typing_test)
start_button.pack()

# Shows result to the user
result_label = tk.Label(root, text="")
result_label.pack()

# Calculates the typing speed of the user
submit_button = tk.Button(root, text="Submit", command=calculate_typing_speed)
submit_button.pack()
submit_button.config(state=tk.DISABLED)

# Bind the text entry field to the check_text_entry function
input_text.bind('<KeyRelease>', check_text_entry)

# Starts the GUI event loop
root.mainloop()
