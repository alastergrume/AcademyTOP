https://selectel.ru/blog/tutorials/how-to-create-tables-in-mysql/ - Учебник по MySQL



Алгоритм для работы с базой данных в интерактивном режиме в запущенном докер контейнере.
После успешного запуска докер контейнера, можно войти в контейнер в интерактивном режиме и подключиться к базе и выполнять запросы my SQL напрямую.

Ниже команды, которые позволяют работать с базой данных в контейнере в интерактивном режиме. 

1. Входим в интерактивный режим:
mysql> docker exec -it 3cc72cb32e12 /bin/bash - 

2. Подключаемся к mysql:
mysql> mysql -proot  
-- Входим в базу mysql. флаг -p подключение с паролем, root - пароль

3. Выводим информацию о базах данных:
mysql> show databases 
    -> ;

- Выводится список имеющихся баз данных

+--------------------+  
| Database           |  
+--------------------+  
| Academy            |  
| information_schema |  
| mysql              |  
| performance_schema |  
| sys                |  
+--------------------+  
5 rows in set (0.00 sec)

4. Подключаемся к интересущей нас базе данных
mysql> use Academy

5. Просмотр таблиц:
mysql> show tables
    -> ;

- Вывод

+-------------------+
| Tables_in_Academy |
+-------------------+
| Departments       |
+-------------------+
1 row in set (0.00 sec)


6. Отправка запроса на вывод информации из таблицы:

mysql> select * from Departments
    -> ;
+--------------+-----------+-------------------+-----------+
| DepartmentId | Financing | Name              | FacultyId |
+--------------+-----------+-------------------+-----------+
|            1 |    235.00 | Programming langs |         1 |
|            2 |    123.00 | Heroes study      |         2 |
|            3 |    986.00 | Music base        |         3 |
+--------------+-----------+-------------------+-----------+
3 rows in set (0.00 sec)

7. Запрос на добавление ещё одной таблицы:

mysql> CREATE TABLE Faculties(FacultyId int PRIMARY KEY, Name nvarchar(100) UNIQUE NOT NULL CHECK(Name != ''));       
Query OK, 0 rows affected, 1 warning (0.05 sec)

mysql> show tables
    -> ;
+-------------------+
| Tables_in_Academy |
+-------------------+
| Departments       |
| Faculties         |
+-------------------+
2 rows in set (0.00 sec)

8. Вывод информации о полях таблицы:

mysql> DESC Faculties
    -> ;
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| FacultyId | int          | NO   | PRI | NULL    |       |
| Name      | varchar(100) | NO   | UNI | NULL    |       |
+-----------+--------------+------+-----+---------+-------+
2 rows in set (0.00 sec)