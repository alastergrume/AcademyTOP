SELECT FirstName, LastName, BirthDate, Email
FROM Students
WHERE EXISTS (SELECT * 
 FROM achievements
 WHERE achievements.StudentId = Students.Id
 )


 -- ANY/SOME - выполн€ют одно и тоже действие - 
 -- проверку выполнени€ заданного услови€ сравнени€,
 -- который определ€етс€ подзапросом

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

SELECT COUNT(*) AS [Count] -- COUNT - ‘ункци€-—четчик количества 
FROM Students
WHERE BirthDate < ANY (Select BirthDate from Teachers)


-- ALL - используетс€ при сравнении результатов подзапроса, таким образом чтобы указать условию все результаты, удовлетвор€ющие знанию позапроса без исключени€.


SELECT FirstName, LastName, Assesment 
FROM Students AS S, achievements as A
WHERE StudentId = S.ID AND
Assesment > ALL (
		SELECT AVG(Assesment) -- AVG - —реднеарифметическое
		FROM achievements
		-- GROUP BY StudentId
);



