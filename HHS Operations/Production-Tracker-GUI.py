# !Python3                                              A3R0NA$
import os
from tkinter import *
from tkinter import messagebox, messagebox
from PIL import ImageTk, Image
'''
{hhs_num}_{cus_job}_{month}-{day}.xlsx
{hhs_num}_{cus_job}_Production-Tracker.xlsx
'''

# Create main window
root = Tk()
root.title('Main Window')
root.geometry('275x175')


# Core functions
def VerifyProjInfo(num, m, d):
    '''
    Verifies project number, day and month are entered correctly
    Returns 1 if they are and 0 if they are not
    '''
    if len(num) == 8:
        if int(m) > 0 and int(m) < 13:
            if int(d) > 0 and int(d) < 32:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0


def NewInputWB():
    '''Create new entry workbook'''
    global hhs_num
    global cus_job
    global day
    global month
    # Verify inputs are in correct format
    if VerifyProjInfo(hhs_num, month, day):
        # New excel input file name
        new_entry_name = f'{hhs_num}_{cus_job}_{month}-{day}.xlsx'
        existing_reports = os.listdir('./Reports/History/')
        # Verify todays entry does not exist
        if new_entry_name in existing_reports:
            messagebox.showerror('This date input file already exists!')
            break
        else:
            # Load entry template
            new_wb = op.load_workbook(
                'Templates/Template_DailyInput.xlsx.xlsx')
            # Save new copy in reports
            new_wb.Save(f'Reports/History/{new_entry_name}.xlsx')
            # Open the new input copy
            open_now = messagebox.askyesno(
                'Daily entry file created, open now?')
            if open_now:
                os.system(
                    f'start EXCEL.EXE Reports/History/{new_entry_name}.xlsx')
            else:
                break
    else:
        messagebox.showerror('Incorrect project info formats!')
        break


def EnterDaysInput():
    '''Enter the new days data'''
    global hhs_num
    global cus_job
    global day
    global month
    # Load projects input file (completed)
    entry_wb = op.load_workbook(
        f'Reports/History/{hhs_num}_{cus_job}_{month}-{day}.xlsx')
    # Load existing project tracker
    proj_tracker = op.load_workbook(
        f'Reports/{hhs_num}_{cus_job}_Production-Tracker.xlsx')
    # TODO Verify date column does not already exist (ask to copy over)
    # TODO Enter input wb data into new column
    # TODO Save project tracker changes, Close input wb


def CreateNewProject():
    '''Create new project tracker'''
    global hhs_num
    global cus_job
    global day
    global month
    # Verify project format and does not already exist
    if VerifyProjInfo(hhs_num, month, day):
        new_proj_name = f'{hhs_num}_{cus_job}_Production-Tracker.xlsx'
        existing_projects = os.listdir('./Reports/')
        if new_proj_name not in existing_projects:
            proj_template = op.load_workbook(
                'Templates/Template_ProjectTracker.xlsx')
            # TODO Enter project information into new project wb
            proj_template.save(new_proj_name)
            messagebox.showinfo(
                f'Project Tracker {new_proj_name} has been created.')
        else:
            messagebox.showerror('Project already exists!')
            break
    else:
        messagebox.showerror('Verify project info formats!')


# Input names and boxes
hhs_num_label = Label(root, text='HHS Project Number:')
hhs_num_label.grid(row=0, column=0, columnspan=2)
hhs_num_entry = Entry(root, width=23)
hhs_num_entry.grid(row=0, column=2, columnspan=2)
hhs_num = hhs_num_entry.get()  # TODO Verify proper format info

cus_job_label = Label(root, text='Customer Job Number:')
cus_job_label.grid(row=1, column=0, columnspan=2)
cus_job_entry = Entry(root, width=23)
cus_job_entry.grid(row=1, column=2, columnspan=2)
cus_job = cus_job_entry.get()  # TODO Verify proper format info

loc_label = Label(root, text='Location:')  # TODO Make a dropdown menu?
loc_label.grid(row=2, column=0, columnspan=2)
loc_entry = Entry(root, width=23)
loc_entry.grid(row=2, column=2, columnspan=2)
loc = loc_entry.get()  # TODO Verify proper format info

date_label = Label(root, text='Date: [Day] [Month]')
date_label.grid(row=3, column=0, columnspan=2)
day_entry = Entry(root, width=11)  # TODO Make a dropdown menu?
day_entry.grid(row=3, column=2, pady=6)
month_entry = Entry(root, width=11)  # TODO Make a dropdown menu?
month_entry.grid(row=3, column=3, pady=6)
day = day_entry.get()  # TODO Verify proper format info
month = month_entry.get()  # TODO Verify proper format info


# Action Buttons
make_wb_button = Button(root, text='Create New Report', command=NewInputWB)
make_wb_button.grid(row=4, column=0, columnspan=2)

enter_data_button = Button(
    root, text='Enter Daily Report', command=EnterDaysInput)
enter_data_button.grid(row=4, column=2, columnspan=2)

new_proj_button = Button(root, text='Create Project', command=CreateNewProject)
new_proj_button.grid(row=5, column=1, columnspan=2, pady=20)


# Run main logic (Open root window)
root.mainloop()
