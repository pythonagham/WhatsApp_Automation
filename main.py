import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import pywhatkit
from datetime import datetime
import time

def send_message():
    phone_number = phone_entry.get()
    group_id = group_entry.get()
    message = message_entry.get()
    selected_date = cal.get_date()
    selected_time = time_entry.get()
    # Parse the selected date and time
    datetime_obj = datetime.strptime(f"{selected_date} {selected_time}", "%Y-%m-%d %I:%M %p")

    # Set the target date and time
    target_date = datetime(datetime_obj.year, datetime_obj.month, datetime_obj.day, datetime_obj.hour, datetime_obj.minute)
    # Calculate the time difference between now and the target date
    time_difference = target_date - datetime.now()
    print (time_difference)
    # Convert the time difference to seconds
    delay_seconds = time_difference.total_seconds()
    if phone_number:
        # Check if the target date is in the future
        if delay_seconds > 100:
            messagebox.showinfo("Message Scheduled",
                        f"Message scheduled for {datetime_obj.strftime('%Y-%m-%d %I:%M %p')},after{delay_seconds}")
            print(delay_seconds)
            time.sleep(delay_seconds-60)
            # Wait until the target date and time
            pywhatkit.sendwhatmsg(phone_number, message, target_date.hour, target_date.minute, 30, True, 5)
        elif delay_seconds>0 and delay_seconds <100:
            messagebox.showinfo("Message Scheduled",
                                f"Message scheduled for {datetime_obj.strftime('%Y-%m-%d %I:%M %p')}")
            pywhatkit.sendwhatmsg(phone_number, message, target_date.hour, target_date.minute, 30, True, 5)
        else:
            messagebox.showinfo("Warning","Target date and time have already passed.")

    elif group_id:
        messagebox.showinfo("Message Scheduled",
                            f"Message scheduled for {datetime_obj.strftime('%Y-%m-%d %I:%M %p')}")
        pywhatkit.sendwhatmsg_to_group(group_id, message, datetime_obj.hour, datetime_obj.minute, 30, True, 5)

    else:
        messagebox.showinfo("Warning", "Please enter phone number or group ID.")

# Create the main Tkinter window
root = tk.Tk()
root.title("WhatsApp Message Sender")
root.geometry('600x645')
root.config(bg='#128c7e')
root.resizable(False, False)


logo = tk.PhotoImage(file='first.png')
tk.Label(root, image=logo, bg='#128c7e') \
    .place(x=220, y=5)
tk.Label(root, text='Whatsapp Bot', font="Calibri 35 bold",
         fg='white', bg='#128c7e').place(x=150, y=162)


# Create entry fields
phone_label = tk.Label(root, text="Enter Phone Number:",
                    font='Calibri 15 bold',bg='#128c7e',
                    fg="#ece5dd")
phone_label.place(x=55, y=255)

phone_entry = tk.Entry(root,font='Calibri 15 bold')
phone_entry.place(x=55, y=290)

tk.Label(root, text="Or",
        font='Calibri 15 bold',
        bg='#128c7e',fg="#ece5dd").place(x=285, y=290)

group_label = tk.Label(root, text="Enter Group ID:",
                       font='Calibri 15 bold',
                       bg='#128c7e',fg="#ece5dd")
group_label.place(x=340, y=255)

group_entry = tk.Entry(root,font='Calibri 15 bold')
group_entry.place(x=340, y=290)

date_label = tk.Label(root, text="Select Date:", font='Calibri 15 bold',
                      bg='#128c7e', fg="#ece5dd")
date_label.place(x=115, y=350)

# Create DateEntry widget
cal = DateEntry(root, width=12, background='darkblue',font='Calibri 15 bold',
                foreground='white', borderwidth=2, year=2023, month=12, day=19)
cal.place(x=115, y=385)

# Create time entry
time_label = tk.Label(root, text="Select Time:", font='Calibri 15 bold',
                      bg='#128c7e', fg="#ece5dd")
time_label.place(x=340, y=350)

time_entry = tk.Entry(root, font='Calibri 15 bold',width=13)
time_entry.place(x=340, y=385)

message_label = tk.Label(root, text="Enter message:",
                         font='Calibri 15 bold',
                         bg='#128c7e',fg="#ece5dd")
message_label.place(x=235, y=445)

message_entry = tk.Entry(root,font='Calibri 20 bold',width=15)
message_entry.place(x=190, y=480)

# Create Send Message button
send_button = tk.Button(root, text="Send Message", height='1',width=15,
           bg='#25d366',fg='white',font='Calibri 15 bold',bd=0,
           command=send_message)
send_button.place(x=218, y=542)

# Start the Tkinter event loop
root.mainloop()
