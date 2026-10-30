accepted = 0
rejected = 0
has_digit = False
while True:
    job_title = str(input("enter the job title/done:"))
    if job_title == "done":
        break
    job_title = job_title[0]. upper() + job_title[1:].lower()   
    for c in job_title:
        if c.isdigit():
            has_digit = True
            break
    if has_digit == True or len(job_title) < 3:
        rejected += 1
    else:
        accepted += 1
print(f"jobs accepted:{accepted} vs jobs rejected:{rejected}")
