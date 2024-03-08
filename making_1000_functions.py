import random


# 1. Stwórz funkcję, która zwraca sumę 2 liczb

def to_sum_up(digit1, digit2):
    return digit1 + digit2

# 2. Stwórz funkcję, która zwraca róznicę 2 liczb


def difference(digit1, digit2):
    return digit1 - digit2

# 3. Stwórz funkcję, która zwraca iloczyn 2 liczb


def product(digit1, digit2):
    return  digit1 * digit2

# 4. Stwórz funckję, która zwraca iloraz 2 liczb


def quotient(digit1, digit2):
    return digit1 / digit2

# 5. Stwórz funkcję, która zwraca iloraz 2 liczb - zabezpiecz się przed dzieleniem przez 0


def quotient2(digit1, digit2):
    if digit2 == 0:
        raise ZeroDivisionError('Nie dzielimy przez 0!')
    return digit1 / digit2


# 6. Stwórz funkcję, która zwraca listę 5 liczb w zakresie od 50 do 1000

def get_random_digits():
    random_digits = []
    for _ in range(5):
        digit = random.randint(50, 1000)
        random_digits.append(digit)
    return random_digits

# 7. Stwórz funkcję, która zwraca posortowaną listę 10 liczb w zakresie od 5 do 1000, rosnąco


def get_random_digits2():
    random_digits = []
    for _ in range(10):
        digit = random.randint(5, 1000)
        random_digits.append(digit)
    return sorted(random_digits)

# print(get_random_digits2())

# 8. Stwórz funkcję, która zwraca posortowaną listę 20 liczb w zakresie od 5 do 1000, malejąco


def get_random_digits3():
    random_digits = []
    for _ in range(20):
        digit = random.randint(5, 1000)
        random_digits.append(digit)
    random_digits.sort(reverse=True)
    return random_digits

# print(get_random_digits3())

# 9. Stwórz funkcję, która zwraca posortowaną listę n(nie większą niz zakres) liczb w zakresie 0 - 1000, rosnąco


def get_n_random_digits(amount_of_digits):
    random_digits = []
    if not 0 <= amount_of_digits < 1000:
        raise ValueError('Podana liczba wykracza poza zakres(0 - 1000)')
    for digit in range(amount_of_digits):
        random_digits.append(random.randint(0, 1000))
    return sorted(random_digits)

# print(get_n_random_digits(1001))
# print(get_n_random_digits(-1))

# 10. Stwórz funckję, która zwraca listę unikalnych n liczb w zakresie podanym przez uzytkownika


def get_n_digits(amount_of_digits):
    min_range_of_digits = int(input('Podaj dolny zakres: '))
    max_range_of_digits = int(input('Podaj górny zakres: '))
    digits = set()
    for digit in range(amount_of_digits):
        digits.add(random.randint(min_range_of_digits, max_range_of_digits))
    return digits

# print(get_n_digits(3))

# 11. Stwórz funkcję, która zwraca listę liczb od 0 do 10


def get_11_digits():
    list_of_digits = []
    for digit in range(0, 11):
        list_of_digits.append(digit)
    return list_of_digits

# print(get_11_digits())

# 12. Stwórz funkcję, która przyjmuje listę liter i ma je połączyć po '-'


def joining_letters(list_of_letters):
    return '-'.join(list_of_letters)

# print(joining_letters(['a', 'b', 'c']))

# 13. Stwórz funkcję, która przyjmuje listę liczb i zwraca ich sumę


def get_sum_of_digits(list_of_digits):
    return sum(list_of_digits)

# print(get_sum_of_digits([1, 3, 5]))

# 14. Stwórz funkcję, która zwraca najmniejszą wartość z listy


def get_min_digit(digits):
    min_digit = digits[0]
    for digit in digits:
        if digit < min_digit:
            min_digit = digit
    return min_digit

# print(get_min_digit([1, 0, 4, 6]))
# print(get_min_digit([1, 0, 4, 6, -6]))

# 15. Stwórz funkcję, która zwraca największą wartość z listy


def get_max_digit(digits):
    max_digit = digits[0]
    for digit in digits:
        if digit > max_digit:
            max_digit = digit
    return max_digit


# print(get_max_digit([1, 0, 4, 6, -6]))

# 16. Stwórz funkcję, która zwraca największą i najmniejszą wartość z listy


def get_max_and_min(digits):
    max_digit = digits[0]
    min_digit = digits[0]
    for digit in digits:
        if digit > max_digit:
            max_digit = digit
        if digit < min_digit:
            min_digit = digit
    return max_digit, min_digit


# print(get_max_and_min([1, 0, 4, 6, -6]))

# 17. Stwórz funkcję, która zwróci słownik wartość-index dla liczb z podanej listy

def get_value_and_index(digits):
    val_and_idx = {}
    for val, idx in enumerate(digits):
        val_and_idx[val] = idx
    return val_and_idx

# print(get_value_and_index([1, 0, 4, 6, -6]))

# 18. Stwórz funkcję, która wita uzytkownika - nowy(hello stranger!) szefa(hello 'imię'!)


def hello_user():
    name = input('Podaj swoje imię: ')
    bosses = ['Konrad', 'Karolina', 'Klaudia', 'Dominik']
    if name not in bosses:
        return 'Hello stranger!'
    return f'Hello {name}!'

# print(hello_user())

# 19. Stwórz funkcję, która sprawdzi, czy wyraz jest palindromem


def check_palindrome(word):
    return word.lower() == word.lower()[::-1]

# print(check_palindrome('Kayak'))

# 20. Stwórz funkcję, która obliczy średnią arytmetyczną elementów listy


def get_avr(digits):
    counter = 0
    sum_of_digits = 0
    for digit in digits:
        sum_of_digits += digit
        counter += 1
    return sum_of_digits / counter

# print(get_avr([1, 2, 3, 4, 5, 6, 7]))

# 21. Stwórz funkcję, która wyświetla imię uzytkownika


def print_name():
    print(f'Imię uzytkownika to {input("podaj imię uzytkowniku: ")}')

# print_name()

# 22. Napisz funkcję, która zwróci typ danych parametru


def get_type(arg):
    return type(arg)

# 23. Napisz funkcję, która zwróci 1 i ostatnią literę wyrazu


def get_first_and_last_letter(word):
    return word[:1], word[-1]

# print(get_first_and_last_letter('Kalina'))

# 24. Napisz funkcję, która policzy ilość wystąpień dla litery a w napisie


def counting_a(message):
    return message.count('a')

# print(counting_a('Konrad ma nierbieskie oczy, Halina się uparła i chce zrobić mu na złość'))

# 25. Napisz funkcję wyliczającą potęgę dla elementów listy


def get_squ(digits):
    result = []
    for digit in digits:
        result.append(digit ** 2)
    return result

# 26. Stwórz funkcję, która podzieli bez reszty podane elementy listy, przez podaną przez uzytkownika liczbę


def get_p(digits):
    result = []
    dig = input('podaj liczbę')
    for digit in digits:
        result.append(digit // dig)
    return result

# 27. Napisz funkcję wyliczającą potęgę dla elementów listy, zsumuje i podzieli przez 6


def get_summmmm(digits):
    result = []
    sum = 0
    for digit in digits:
        element = digit ** 2
        result.append(element)
        sum += element
    return sum / 6

# print(get_summmmm([2, 4, 5, 6, 3, 10, 15]))

# 28. Napisz funkcję, która zsumuje elementy listy - nie uzywając funkcji sum i zwróci tą sumę


def get_my_sum(digits):
    my_sum = 0
    for digit in digits:
        my_sum += digit
    return my_sum

# 29. Napisz funkcję, która zwróci napis złozony z elementów listy i tylko pierwszy element będzie z duzej litery


def get_string(words):
    result = ' '.join(words)
    result = result.lower()
    return result.capitalize()

# print(get_string(['Ala', 'Komin', 'na', 'albo']))

# 30. Napisz funkcję, która odejmie elementy listy(o roznych typach danych)


def get_diff(elements):
    result = elements[0]
    result = int(result)
    for element in elements[1:]:
        result -= int(element)
    return result

# print(get_diff(['1', 1, 5, '10']))

