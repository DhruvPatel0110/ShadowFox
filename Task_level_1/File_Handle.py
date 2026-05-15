# Reading student_marks.csv file and adding Total & Average columns
import csv

students = []

with open("student_marks.csv", "r") as file:

    csv_reader = csv.DictReader(file)

    for row in csv_reader:

        # Replacing empty values with 0 as the dataset has empty values
        maths = int(row["Maths"] or 0)
        physics = int(row["Physics"] or 0)
        chemistry = int(row["Chemistry"] or 0)
        english = int(row["English"] or 0)
        biology = int(row["Biology"] or 0)
        economics = int(row["Economics"] or 0)
        history = int(row["History"] or 0)
        civics = int(row["Civics"] or 0)

        # Calculating total and average
        total_marks = (
            maths + physics + chemistry + english +
            biology + economics + history + civics
        )

        average_marks = total_marks / 8

        # Adding new columns
        row["Total_Marks"] = total_marks
        row["Average_Marks"] = average_marks

        students.append(row)


# # Writing updated data into a new CSV file
with open("updated_student_marks.csv", "w", newline="") as new_file:

    fieldnames = students[0].keys()

    writer = csv.DictWriter(new_file, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerows(students)

print("New CSV file created successfully")