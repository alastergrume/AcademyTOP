// Задание №7
let value = +prompt('Сколько сейчас часов?');
let value2 = +prompt('Сколько сейчас минут?');
let houre = 23 - value;
let minute = 60 - value2;
alert(`До конца дня осталось ${houre} часов - ${minute} минут`)


// Работа с объектами 07/08/2024

//Создание пустых объектов
var obj = new Object();
var obj2 = {};

// Добавляем свойства/атрбут в объект, используя обычный синтаксис 
obj['Name'] = 'Vasya';
obj.Age = 16;
alert(obj.Name + obj.Age);

//Проверка свойств
if ('Age' in obj) {
    alert('Age Exists');
}
else { 
    alert('Age Not Exists');
}

// Удаление атрибутов:
delete obj.Age;
alert("Age deleted");

//Проверка свойств
if ('Age' in obj) {
    alert('Age Exists');
}
else { 
    alert('Age Not Exists');
}

// Создание объектов словарей
var student = {
    name: 'Daria',
    lastName: 'Student',
    age: 23
};

var student2 = {
    name: 'Vova',
    lastName: 'Petrov',
    age: 23,
    address: {
        street: 'Lenina',
        city: 'Moscow',
        country: 'Russian Federation'
    }
};

alert(student2.address.city);

// Перебор словарей

for (var tempProperty in student)
{
    alert(tempProperty) // название свойства
    alert(student[tempProperty]) // значение
};


// Массивы

arrayName = new Array();
arrayName = new Array(20);
arrayName = new Array(11,12,13,14,15,16,17,18,19,20,21);

// Присвоенеи значений эллементам массива
var arr = new Array();
arr[0] = 34; 
arr[1] = 22;
arr[2] = 1;


var arr2 = []; //Пустой список
alert(arr2.length);
// Оформление циклов:
for (var i = 0; i < arr.length; i++) //Инициализируем переменную i, задается глубина цикла, задается шаг цикла 
{
    alert(arr[i]);
}


// Двумерные массивы

var arr = [
    [1, 2, 3],
    [2, 3, 6]
]
