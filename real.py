# метод, принимающий аргументами переменные и оператор совершаемый над ними.

from fractions import Fraction
from math import gcd
import re

def calc(a,b,oper):
    # если получили строку
    if type(a) == str and type(b) == str: 
        if a.find('/') < 0 and b.find('/') < 0:
            a_real = float(a)
            b_real = float(b)
            return operation(a_real, b_real, oper)
        else:
            if a[a.find('/') + 1] == '0' or b[b.find('/') + 1] == '0': return 'Division by zero'
            else: return parce_fraction_answer(operation_fraction(pars_fraction(a), pars_fraction(b), oper))

    # если получили кортеж
    if type(a) == tuple and type(b) == tuple: 
        a_real = float(a[0])
        b_real = float(b[0])
        return operation(a_real, b_real, oper)

# принимает два числа с плаваюшей точкой и возвращает ответ по операции
def operation (n1, n2, oper):
    round_match = max(len(str(n1).split('.')[1]), len(str(n2).split('.')[1])) 
    match oper:
        case '+': return str(round(n1 + n2, round_match)) 
        case '-': return str(round(n1 - n2, round_match))
        case '*': return str(round(n1 * n2, round_match))
        case '/':
            if float(n2) == 0.0: 
                return 'Division by zero'
            else: 
                return str(round(n1 / n2, round_match))

# принимает на вход две дроби простого вида a/b и возвращает ответ операции над ними
def operation_fraction (n1, n2, oper):
    match oper:
        case '+': return f'{Fraction(n1).numerator * Fraction(n2).denominator + Fraction(n2).numerator * Fraction(n1).denominator}/{Fraction(n2).denominator * Fraction(n1).denominator}'
        case '-': return f'{Fraction(n1).numerator * Fraction(n2).denominator - Fraction(n2).numerator * Fraction(n1).denominator}/{Fraction(n2).denominator * Fraction(n1).denominator}'
        case '*': return f'{Fraction(n1).numerator * Fraction(n2).numerator}/{Fraction(n1).denominator * Fraction(n2).denominator}'
        case '/': return f'{Fraction(n1).numerator * Fraction(n2).denominator}/{Fraction(n2).numerator * Fraction(n1).denominator}'

# приводим к виду простой дроби вида a/b
def pars_fraction (number):
    ans_str = re.split(' |/', number)
    sign = ''
    if len(ans_str) > 2:
        if int(ans_str[0]) < 0:
            sign = '-'
            ans_str[0] = f'{abs(int(ans_str[0]))}'
        return f'{sign}{int(ans_str[0]) * int(ans_str[2]) + int(ans_str[1])}/{ans_str[2]}'
    else: 
        return number

# выделяем в дроби целочисленную состовляющую (если есть), получаем вид    x a/b
def parce_fraction_answer (number):
    ans_str = (list(map(int, number.split('/'))))
    sign = ''
    
    if ans_str[0] < 0: 
        sign = '-'
        ans_str[0] = int(ans_str[0]) * -1

    # если число целое, то возвращаем одно число
    if len(ans_str) < 2:
        return f'{number}'
    # если знаменатель дроби навен 1, то возвращаем только числитель как целое число
    elif ans_str[1] == 1:
        return f'{ans_str[0]}'
    # если числитель равен нулю - возвращаем НОЛЬ
    elif ans_str[0] == 0:
        return f'{ans_str[0]}'
    # если знаменатель равен нулю - возвращаем предупреждение
    elif ans_str[1] == 0:
        return 'Division by zero'
    # если числитель равен знаменателю - возвращаем единицу с входным знаком
    elif ans_str[0] == ans_str[1]:
        return f'{sign}1'
    # если числитель больше знаменателя, то вычисляем целую часть дроби, сокращаем (если это возможно) дробную часть и возвращаем ответ
    elif ans_str[0] > ans_str[1]:
        int_num = int(ans_str[0] / ans_str[1])
        fract_nod = gcd(ans_str[0], ans_str[1])
        ans_str[0] = int(ans_str[0] / fract_nod)
        ans_str[1] = int(ans_str[1] / fract_nod)
        if (ans_str[0] - int_num * ans_str[1]) == 0:
            return f'{sign}{int_num}'
        else:
            return f'{sign}{int_num} {ans_str[0] - int_num * ans_str[1]}/{ans_str[1]}'
    # во всех остальных случаях просто сокращаем дробь (если это возможно) и возвращаем ответ
    else:
        fract_nod = gcd(ans_str[0], ans_str[1])
        return f'{sign}{ans_str[0] / fract_nod}/{ans_str[1] / fract_nod}'