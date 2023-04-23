# Bernabe, Aleckxis Kate V.
# BSCpE 1-4

# Open the input file.
with open('students.txt', 'r') as f:
    # Set up variables to determine which student has the highest GWA.
    highest_gwa = 1
    student_name = ''
    # Read the file line by line.
    for line in f:
        # Separate the student name from the GWA in the line.
        name, gwa = line.strip().split(',')
        # Convert the GWA into a float.
        gwa = float(gwa)
        # Check if the student has a higher GWA than the current highest GWA
        if gwa < highest_gwa:
            # Update the highest GWA and the student's name with the highest GWA.
            highest_gwa = gwa
            student_name = name
# Print the name and GWA of the pupil with the highest GWA.
print(f"The student with the highest GWA is", student_name, "with the GWA of", highest_gwa, ".")