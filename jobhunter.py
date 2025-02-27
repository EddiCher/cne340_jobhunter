CREATE TABLE student_grades (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  number_grade INTEGER,
  fraction_completed REAL);
INSERT INTO student_grades (name, number_grade, fraction_completed)
  VALUES ("Winston", 85, 0.805);
INSERT INTO student_grades (name, number_grade, fraction_completed)
  VALUES ("Winnefer", 95, 0.901);
INSERT INTO student_grades (name, number_grade, fraction_completed)
  VALUES ("Winsteen", 85, 0.906);
INSERT INTO student_grades (name, number_grade, fraction_completed)
  VALUES ("Wincifer", 66, 0.7054);
INSERT INTO student_grades (name, number_grade, fraction_completed)
  VALUES ("Winster", 76, 0.5013);
INSERT INTO student_grades (name, number_grade, fraction_completed)
  VALUES ("Winstonia", 82, 0.9045);
SELECT name, number_grade, ROUND(fraction_completed * 100) AS percent_completed
 FROM student_grades;
 SELECT COUNT(*),
  CASE
    WHEN number_grade > 95 THEN "A"
    WHEN number_grade > 85 THEN "B"
    WHEN number_grade > 75 THEN "C"
    ELSE "F"
  END AS "letter_grade"
FROM student_grades
GROUP BY letter_grade
