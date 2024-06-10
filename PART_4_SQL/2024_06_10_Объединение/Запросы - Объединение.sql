SELECT FirstName, LastName, BirthDate, Email
FROM Students
WHERE EXISTS (SELECT * 
 FROM achievements
 WHERE achievements.StudentId = Students.Id
 )


 -- ANY/SOME - ��������� ���� � ���� �������� - 
 -- �������� ���������� ��������� ������� ���������,
 -- ������� ������������ �����������

SELECT FirstName, LastName, BirthDate, Email
FROM Students
WHERE Id = ANY (SELECT StudentID
				FROM achievements		
				WHERE Assesment = '10'
				);


SELECT FirstName, LastName, BirthDate, Email
FROM Students
WHERE Id IN (SELECT StudentID
				FROM achievements		
				WHERE Assesment = '10'
				);

SELECT COUNT(*) AS [Count] -- COUNT - �������-������� ���������� 
FROM Students
WHERE BirthDate < ANY (Select BirthDate from Teachers)


-- ALL - ������������ ��� ��������� ����������� ����������, ����� ������� ����� ������� ������� ��� ����������, ��������������� ������ ��������� ��� ����������.


SELECT FirstName, LastName, Assesment 
FROM Students AS S, achievements as A
WHERE StudentId = S.ID AND
Assesment > ALL (
		SELECT AVG(Assesment) -- AVG - ��������������������
		FROM achievements
		-- GROUP BY StudentId
);


SELECT FirstName, + ' ' + LastName as FullName, BirthDate
FROM Students
WHERE MONTH (BirthDate) > 5
AND MONTH(BirthDate) < 9
UNION -- ����������� ��������
SELECT FirstName, + ' ' + LastName as FullName, BirthDate
FROM Teachers
WHERE MONTH (BirthDate) > 5
AND MONTH(BirthDate) < 9
ORDER BY BirthDate



