# ------------------------- Лекция -----------------------------

# --------------------- Массивы (Списки) -----------------------

# list1 = ["Drama", "Comedy", "Fantasy"]
# list2 = []
# list3 = list(("Marh", "Algoritmika", "DataBases"))
# print(list3)
# print(list3[2])
listDZ = []
for i in range(25):
    listDZ.append(i)
# print(listDZ)
# Верхний правый угол
for i in range(5):
    for j in range(5):
        if i == 0:
            listDZ[5 * i + j] = "*"
        elif i == 1 and j > 0 and j < 4:
            listDZ[5 * i + j] = "*"
        elif i == 2 and j == i:
            listDZ[5 * i + j] = "*"
        else:
            listDZ[5 * i + j] = "."
# Вывод на экран
for i in range(5):
    for j in range(5):
        print(listDZ[5 * i + j], end="\t")
    print("\n")

print("\n")


for i in range(5):
    for j in range(5):
        if i == j:
            listDZ[5 * i + j] = "*"
        elif j >= i + 1:
            listDZ[5 * i + j] = "*"
        else:
            listDZ[5 * i + j] = "."
# Вывод на экран
for i in range(5):
    for j in range(5):
        print(listDZ[5 * i + j], end="\t")
    print("\n")
