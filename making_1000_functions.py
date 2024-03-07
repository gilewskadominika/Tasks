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

print(check_palindrome('Kayak'))