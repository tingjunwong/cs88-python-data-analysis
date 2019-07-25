.read data.sql

-- Q2
CREATE TABLE obedience as
  -- REPLACE THIS LINE
  SELECT seven, gerald from students;


-- Q3
CREATE TABLE blue_dog as
  -- REPLACE THIS LINE
  SELECT color,pet from students where color = "blue" and pet = "dog";


-- Q4
CREATE TABLE smallest_int as
  -- REPLACE THIS LINE
  SELECT time, smallest from students
where smallest > 3 order by smallest limit 20;


-- Q5
CREATE TABLE sevens as
  -- REPLACE THIS LINE
  SELECT a.seven from students as a, checkboxes as b
    where a.time = b.time and a.number = 7 and b.'7' = 'True';


-- Q6
CREATE TABLE matchmaker as
  -- REPLACE THIS LINE
  SELECT a.pet, a.song, a.color, b.color from students as a, students as b
    where a.pet = b.pet and a.song = b.song and a.time < b.time;


-- Q7
CREATE TABLE smallest_int_count as
  -- REPLACE THIS LINE
  -- SELECT smallest, COUNT(*) FROM students where smallest > 0 GROUP BY smallest;

select smallest,count(*) from students group by smallest;