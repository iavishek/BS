CREATE TABLE course (
    course_id   INT  PRIMARY KEY,
    course_name TEXT NOT NULL
);

CREATE TABLE student (
    student_id   INT  PRIMARY KEY,
    student_name TEXT NOT NULL,
    course_id    INT ,
    FOREIGN KEY (course_id) REFERENCES course (course_id)
);