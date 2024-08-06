// Домашнее задание!

// 1.: Приветствие пользователя по имени
let login_name = prompt('Введите Ваше имя ')
alert('Привет ' +login_name +'!');

//2.: Вычисление возраста по году рождения
let birthday = prompt('Введите год Вашего рождения') // Ввод года рождения
let currentDate = new Date().getFullYear() // Метод выводит текущий год
let age = currentDate-birthday // Производит вычисления возраста
alert('Вам сейчас ' + age + ' лет!') // Выводит информацию о возрасте

// 3.: Периметр квадрата
let squre_len = prompt('Введите длину стороны квадрата')
alert('Периметр равен - '+squre_len*2)

// 4.: Вычиселение площади окружности
let circle_radius = prompt('Введите радиус окружности - ')
alert('Площадь окружности равна - ' +(circle_radius**2)*3.14)

// 5.: Вычисление скорости движения между городами
let distance = prompt('Введите расстояние между городами')
let travel_time = prompt('За сколько часов необходимо добраться?')
alert('Скорость движения должна быть, км/ч - '+distance/travel_time)

// 6.: Конвертер валют
let curency = prompt('Введите сумму')
const well = 0.91297 // Объявление константы
alert((curency*well).toFixed(2)+' Евро') // Умножение константы и округление вывода до двух знаков после запятой

// 7.: Вычисление количества файлов размером в 820 МБ
let flash_value_gb = prompt('Объем Вашей флешки в Гб?')
const value_value_mb = 1024
const file_value = 820
let flash_mb = (flash_value_gb*value_value_mb)
alert('На Вашей флешке поместиться ' +Math.floor(flash_mb/file_value)+ ' файлов') // округляет в меньшую сторону

// 8.: Вычисление количества шоколадок и сдачи в кошельке
let cash_balance = prompt('Введите остаток денежных средств')
let price_shokolate = prompt('Введите цену одной шоколадки')
let amount_chocolate = Math.floor(cash_balance/price_shokolate)
let end_balance = cash_balance-(amount_chocolate*price_shokolate)
alert('При Вашем балансе вы можете купить ' + amount_chocolate + ' шоколадок, и в кошельке останется ' + end_balance + ' рублей.')

// 9.: Трехзначное число наоборот
let usernumber = prompt('Введите трехзначное число') //125
let a = usernumber%10 // Находим первое число
let b = Math.floor((usernumber/10)%10) // Сначала избавляемся от последнего числа, разделив нацело и округлив в меньшую сторону, потом находим остаток от деления на 10 и получаем нужную цифру
let c = Math.floor(usernumber/100) // Последнюю цифру так же делим нацело и округляем, остаток искомое число.
alert('Первернутое число - '+a+b+c)
 
// 10.: Четное или не четное.
let even_number = prompt('Введите число для проверки на четность')
alert((even_number%2)==0)