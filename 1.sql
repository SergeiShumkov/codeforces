-- https://sql-academy.org

-- SELECT [константы, агрегатные_функции, поля_группировки]
-- FROM имя_таблицы
-- WHERE условия_на_ограничения_строк
-- GROUP BY поля_группировки
-- HAVING условие_на_ограничение_строк_после_группировки
-- ORDER BY условие_сортировки

-- SELECT поля_таблиц
-- FROM таблица_1
-- [INNER] | [[LEFT | RIGHT | FULL][OUTER]] JOIN таблица_2
--     ON условие_соединения
-- [INNER] | [[LEFT | RIGHT | FULL][OUTER]] JOIN таблица_n
--     ON условие_соединения]



SELECT room_id, AVG(Reviews.rating) AS avg_score  
FROM Reservations
JOIN Reviews
ON Reservations.id  = Reviews.reservation_id 
GROUP BY room_id ;

SELECT good_name  
FROM Payments
JOIN FamilyMembers
ON Payments.family_member  = FamilyMembers.member_id 
JOIN Goods
ON Payments.good = Goods.good_id
WHERE FamilyMembers.status = "son";

SELECT Class.name , Student.first_name 
FROM Class
JOIN Student_in_class
ON Class.id = Student_in_class.class
JOIN student
ON Student_in_class.student = Student.id;

SELECT Class.name , Student_in_class.student 
FROM Class
JOIN Student_in_class
ON Class.id = Student_in_class.class ;

SELECT home_type,  MAX(price)-MIN(price) AS difference
FROM Rooms
GROUP BY home_type
HAVING COUNT(*) >= 2;

SELECT plane , AVG(TIMESTAMPDIFF(second, time_out, time_in))  AS time 
FROM Trip
GROUP BY plane ;

SELECT status , MIN(birthday) AS birthday   
FROM FamilyMembers
GROUP BY status ;

SELECT class, COUNT(*) AS count
FROM Student_in_class
GROUP BY class
ORDER BY count DESC;

SELECT *  
FROM FamilyMembers
WHERE member_name LIKE "% Quincey"
ORDER BY status , member_name ;

SELECT good , amount * unit_price AS sum  
FROM Payments
ORDER BY sum DESC;

SELECT member_name 
FROM FamilyMembers
WHERE member_name LIKE "% Quincey";

SELECT *    
FROM Student
WHERE YEAR(birthday) IN (2000, 2002, 2004);

SELECT room_id, start_date, end_date    
FROM Reservations
WHERE total BETWEEN 500 AND 1200;

SELECT first_name, last_name   
FROM Student
WHERE middle_name IS NULL;

SELECT *
FROM Rooms
WHERE has_kitchen AND has_internet;

SELECT member_name, birthday  
FROM FamilyMembers
WHERE status = "father" OR status = "mother";

SELECT member_name 
FROM FamilyMembers
WHERE status = "father";

SELECT good
FROM Payments
WHERE unit_price > 2000;

SELECT DISTINCT teacher, subject 
FROM Schedule;

SELECT member_name,
	LENGTH(member_name) - INSTR(member_name, " ") AS lastname_length
FROM FamilyMembers;

SELECT member_name,
	YEAR(birthday ) AS year_of_birth
FROM FamilyMembers;

