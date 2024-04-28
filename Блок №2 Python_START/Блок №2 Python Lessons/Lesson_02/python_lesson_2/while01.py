# Логическое умножение Возвращает True если оба выражения равны True.
print("#1 Логическое умножение - оператор \"and\":")


def logic_operator_and(competent, responsible):
    choice_of_employer = competent and responsible
    if choice_of_employer == True:
        print("Вас взяли на работу потому что:", "competent >", competent, "\"and\"", "responsible >", responsible, "=",
              choice_of_employer)
    else:
        print("Вас не взяли на работу потому что:", "competent >", competent, "\"and\"", "responsible >", responsible,
              "=", choice_of_employer)


logic_operator_and(True, True)  # Возвращает True, если оба выражения равны True
logic_operator_and(True, False)  # Возвращает False, если хотя бы одно значение False

# Логическое сложение - оператор or. Возвращает True, если хотя бы одно из выражений True
print("\n#2 Логическое сложения - оператор \"or\":")


def logic_operator_or(competent, responsible):
    choice_of_employer = competent or responsible
    if choice_of_employer == True:
        print("Вас взяли на работу потому что:", "competent >", competent, "\"or\"", "responsible >", responsible, "=",
              choice_of_employer)
    else:
        print("Вас не взяли на работу потому что:", "competent >", competent, "\"or\"", "responsible >", responsible,
              "=", choice_of_employer)


logic_operator_or(True, False)  # Возвращает True, если хотя бы одно из выражений равно True
logic_operator_or(False, False)  # Возвращает False, если хотя бы одно значение False

# Логическое отрицание Возвращает значение обратное операнду
print("\n#3 Логическое отрицание - оператор \"not\":'\n")
previuosly_field = True
print("Ранне был уволен?:", previuosly_field, '\n'"Можем взять на работу?:", not previuosly_field)
previuosly_field = False
print("Ранне был уволен?:", previuosly_field, '\n'"Можем взять на работу?:", not previuosly_field)

# ----------------------------------------------------
print("\nПоследовательность выполнения - сначала выполняется not, затем and, затем or")

time = int(input("Enter the current time in hours: ")) % 24
ticket = False
money = True
luggage = False
print((money or ticket) and not luggage and time > 6)
# ----------------------------------------------------
# Логический оператор "if". Если условие "True" - выполняется условие


# ----------------------------------------------------

print("\nВложенное условие во вложенный цикл while\n")

floor = 1
energy = 70
print("I'm on the", floor, "floor")
while floor != 5:
    step = 0
    while step != 20:
        step += 1
        energy -= 1
        if energy == 0:
            print("I'm tired, I will rest a little")
            energy += 70
    floor += 1
    print("Now I'm on the", floor, "floor")
print("I've got to the right floor")
