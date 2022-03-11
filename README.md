# HHS Automation Program

## Instructions:

1. Download and install Python from [Here](https://www.python.org/downloads/)
2. Download the ZIP file for the hhs-automate repository and unpack
4. Navigate into the folder containing the file "TrackerGUI_1.0.py" in CMD
5. Type the commands:
    'pip install pyinstaller'
    'pyinstaller --onefile -w "TrackerGUI_1.0"'
6. Delete the following files and folders:
    1. ``__pycache__``
    2. build
    3. TrackerGUI_1.0.spec

You now have an excicutable file for the production tracker inside the new folder named "disc".


### To pull inputs from data boxes

**HHS Project Number**
`hhs_num = hhs_num_box.get()`
**Customer Project ID**
`cus_job = cus_job_box.get()`
**Location Information**
`loc = loc_box.get()`
**Date**
`day = day_box.get()`
`month = month_box.get()`


## File names standards

**Daily Input**
`{hhs_num}_{cus_job}_{month}-{day}.xlsx`
**Proj Tracker**
`{hhs_num}_{cus_job}_Production-Tracker.xlsx`


### TODO
- Create master project tracker and add to functionality
- Add master tracking sheet and seperate month sheets to projects
- Create sheet copier with font/boarders as well to other workbooks
- Add function to open already created daily wb if exists already
- Add employee list to tracker and input
- Add completion % tracker to workbooks
