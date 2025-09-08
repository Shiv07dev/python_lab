cursor.execute('''CREATE TABLE IF NOT EXISTS student_subjects (
                    Id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    Mark INTEGER NOT NULL,
                    FOREIGN KEY (student_id) REFERENCES student_record (Enrollment)
                )''')


student_subjects = [
    ("PWP", 95, 92301733016),
    ("DSA", 80, 92301733016),
    ("OS", 85, 92301733016),
    ("MIS", 90, 92301733016),
]

cursor.executemany('''INSERT INTO student_subjects (name, Mark, student_id) 
                      VALUES (?, ?, ?)''', student_subjects)

conn.commit()


cursor.execute('''SELECT name, Mark FROM student_subjects 
                  WHERE student_id = 92301733016''')
subjects = cursor.fetchall()

for subject in subjects:
    print(f"Subject: {subject[0]}, Mark: {subject[1]}")