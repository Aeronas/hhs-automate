# HHS Automation Program

## To pull inputs from data boxes
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
