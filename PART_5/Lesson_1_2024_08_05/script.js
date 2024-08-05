// Тема №1 Изучение JavaScript

//INFO Функция, которая выводит информацию про элементы, которые находятся на страничке

// for(let i = 0; i < document.body.childNodes.length; i++) {
//                 alert(document.body.childNodes[i]);
//             }


// INFO В данном блоке создается переменная div по типу div, создается элемент на страничке и в этом блоке выводится сообщение.

let div = document.createElement('div');
div.className = 'alert'; // присваивается имя класса в созданной переменной
div.innerHTML = '<strong>Всем Привет</strong> Вы прочитали сообщение на экране. <br> Нажмите кнопку  ok'; // Записываем сообщение в переменную
document.body.appendChild(div); // Выводим сообщение


ul3.before('before, Это строка, которая из скрипта!!!')
ul3.style.backgroundColor = 'red';


let liFirst = document.createElement('li');
liFirst.innerHTML = 'prebend111';
ul3.prepend(liFirst);

let liLast = document.createElement('li');
liLast.innerHTML = 'LAST111';
ul3.append(liLast);

// Типы данных:
// в JS 7 типов данных и они объеденены в группы, а так же можно создавать свои типы данные


// Домашнее задание!

// 1.: Приветствие пользователя по имени
// let login_name = prompt('Введите Ваше имя ')
// alert('Привет ' +login_name +'!');

//2.: Вычисление возраста по году рождения
// let birthday = prompt('Введите год Вашего рождения') // Ввод года рождения
// let currentDate = new Date().getFullYear() // Метод выводит текущий год
// let age = currentDate-birthday // Производит вычисления возраста
// alert('Вам сейчас ' + age + ' лет!') // Выводит информацию о возрасте

// 3.: Периметр квадрата
// let squre_len = prompt('Введите длину стороны квадрата')
// alert('Периметр равен - '+squre_len*2)

// 4.: Вычиселение площади окружности
// let circle_radius = prompt('Введите радиус окружности - ')
// alert('Площадь окружности равна - ' +(circle_radius**2)*3.14)

// 5.: Вычисление скорости движения между городами
// let distance = prompt('Введите расстояние между городами')
// let travel_time = prompt('За сколько часов необходимо добраться?')
// alert('Скорость движения должна быть, км/ч - '+distance/travel_time)

// 6.: Конвертер валют
// let curency = prompt('Введите сумму')
// const well = 0.91297 // Объявление константы
// alert((curency*well).toFixed(2)+' Евро') // Умножение константы и округление вывода до двух знаков после запятой

// 7.: Вычисление количества файлов размером в 820 МБ
// let flash_value_gb = prompt('Объем Вашей флешки в Гб?')
// const value_value_mb = 1024
// const file_value = 820
// let flash_mb = (flash_value_gb*value_value_mb)
// alert('На Вашей флешке поместиться ' +Math.floor(flash_mb/file_value)+ ' файлов') // округляет в меньшую сторону

// 8.: Вычисление количества шоколадок и сдачи в кошельке
// let cash_balance = prompt('Введите остаток денежных средств')
// let price_shokolate = prompt('Введите цену одной шоколадки')
// let amount_chocolate = Math.floor(cash_balance/price_shokolate)
// let end_balance = cash_balance-(amount_chocolate*price_shokolate)
// alert('При Вашем балансе вы можете купить ' + amount_chocolate + ' шоколадок, и в кошельке останется ' + end_balance + ' рублей.')

// 9.: Трехзначное число задом наперед
let usernumber = prompt('Введите трехзначное число') //125
let a = usernumber%100 // 1
let b = usernumber%10 // 12.5
let c = 
alert('Первернутое число - '+cba)
 