def how_to_write_expression():
    print(f"""
Правила запису виразу:
1. Операції з виразами пишуться без пробілів (p|q, а не p | q)
2. Після коми — пробіл
3. Те, чому має дорівнювати спрощена множина диз'юнктів, перенести в основний вираз з Not, 
   тобто p |= q -> p, ~q
4. Заміни
    а) ∨ -> |
    б) ¬ -> ~
5. Якщо маєте імплікацію, то використовуйте наступну властивість:
   p => q -> ~p | q
""")


def simplify_using_resol_algo(expression):
    separated_by_commas = expression.split(", ") # просто розділений рядок по диз'юнктам
    result = [] # масив рядків, розділених по кон'юкції для легшої роботи з елементами)
    res = [] # масив символів, що вже піддались законам логіки
    for expr in separated_by_commas:
        result.append(expr.split("|"))

    for symbols in result:
        for symbol in symbols:
            res.append(symbol)

    elements_to_remove = []

    print(f"Маємо наступні символи:\n{res}")
    print("Приберемо всі однакові значення, залишивиши одне, за властивість X|X=X")
    res = list(set(res))
    total_len = 0
    print(res)
    for elem in res:
        not_elem = "~" + elem
        if not_elem in res and res.count(not_elem) == res.count(elem):
            print(f"Застосуємо властивість, що: {elem}|{not_elem}=Т")
            elements_to_remove.extend([elem, not_elem])

            upd = [item for item in res if item not in elements_to_remove]
            print(upd)
            total_len = len(upd)

    return f"Оскільки довжина заданої множини = {total_len}, то множина {'невиконувана' if total_len != 0 else 'виконувана'}"


def unification_algorithm_for_disjunctive_pair(array_of_disjunctions):
    unifications = {}

    for disjunction in array_of_disjunctions:
        for i in range(len(disjunction) - 1):
            for j in range(i + 1, len(disjunction)):
                elem_1, elem_2 = disjunction[i], disjunction[j]

                if len(elem_1) == len(elem_2) and elem_1 != elem_2:
                    key, value = sorted([elem_1, elem_2])
                    unifications[key] = value

    # Convert the dictionary to a list of strings
    total = [f"{key} -> {value}" for key, value in unifications.items()]

    return total


how_to_write_expression()
print(simplify_using_resol_algo("p|q|~r, ~s, t|s, t, r, r|t, ~p, ~q"))

disjunctions = [
    ['x', 'y', 'f(y)'],
    ['u', 'f(v)', 'v']
]

print(unification_algorithm_for_disjunctive_pair(disjunctions))