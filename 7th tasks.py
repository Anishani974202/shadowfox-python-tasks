StudentID,Name,Maths,Science,English
1,Aditya,78,89,90
2,Sneha,88,76,95


import csv

with open("student_marks.csv", mode="r") as infile:
    reader = csv.DictReader(infile)
    students_data = []

    
    for row in reader:
        maths = int(row['Maths'])
        science = int(row['Science'])
        english = int(row['English'])

        total = maths + science + english
        average = total / 3

        row['Total_Marks'] = total
        row['Average'] = round(average, 2)

        students_data.append(row)

with open("student_marks_with_totals.csv", mode="w", newline='') as outfile:
    fieldnames = list(students_data[0].keys())
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students_data)