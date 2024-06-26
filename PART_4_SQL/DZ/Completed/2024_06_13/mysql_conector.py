import mysql.conector

try:
    connection = mysql.connector.connect(
        user='root', password='root', host='mysql', port=3306, database='Academy')
    
except Exception as e:
    print(f'Подключение не установлено! Ошибка - {e}')
    
print("Подключение осуществлено!")