# Нахождение среднего балла
def srballStep(spisok):
    srBall = sum(spisok) / len(spisok)
    if srBall < 10:
        print('Стипендии нет')
    else:
        print('Стипендия есть')