// Курс:
// «Язык сценариев JavaScript и библиотека jQuery»»
// Модуль 1
// ТЕМА: ВВЕДЕНИЕ В JAVASCRIPT
// Домашнее задание №2


// Задание №1
// var user = {
//     name: 'Иван',
//     age: `${+prompt(`Сколько тебе лет?`)}`
// }

// if (user.age < 12)
//     {
//         alert('Вы ребенок');
// } 
// else if (user.age >= 12 && user.age <18) 
//     {
//         alert('Вы подросток');
// }
// else if (user.age >= 18 && user.age <60)
//     {
//         alert('Вы взрослый');
// }
// else if (user.age >= 60)
//     {
//         alert('Вы пенсионер');
// }

// Задание №2
// var numbers = {
//     0: ')',
//     1: '!',
//     2: '@',
//     3: '#',
//     4: '$',
//     5: '%',
//     6: '^',
//     7: '&',
//     8: '*',
//     9: '(',
// }
// let user_prompt = +prompt('Inter number')
// alert(numbers[user_prompt])

// Задание №3

// let usernumber = prompt('Inter number');
// var numb_mass = usernumber.split('');
// if (numb_mass[0]==numb_mass[1] || numb_mass[1]==numb_mass[2] || numb_mass[0]==numb_mass[2])
// {
//     alert('В числе есть одиноковые числа!');
// }
// else {
//     alert('В числе нет одинаковых чисел');
// }

// Задание №4
// let user_year = +prompt('Введите год')
// if ((user_year%400 == 0 || user_year%4 == 0) && user_year%100 != 0)
// {
//     alert('Год високосный!')
// }
// else {alert('Это не високомный год')}