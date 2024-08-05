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

// 1.:
let login_name = prompt('Введите Ваше имя ')
alert('Привет ' +login_name +'!');

//2.:

