def calc(first_arg='', second_arg='', oper=''):
    # В первую очередь проверяем, не равен ли знаменатель нулю. 
    if second_arg == '0' and oper == '/':
        return "Division by zero"
    # Для начала, приводим входящие аргументы в надлежащий вид -- 'a+bj' --, чтобы метод complex() справился корректно.
    # Проверка первого аргумента на наличие знака операции.
    for i in first_arg:
        if '+' or '-' in i:
        # строка вида 'a+bj'
            a_complex = complex(first_arg)
            break
        if '+' or '-' not in i:
        # строка вида 'bj'
            a_complex = f'0+{first_arg}'
            complex(a_complex)
    # Проверка на наличие знака во втором аргументе: 
    for i in second_arg:
        if '+' or '-' in i:
            b_complex = complex(second_arg)
            break
        if '+' or '-' not in i:
            b_complex = f'0+{second_arg}'
            complex(second_arg)

    match oper:
        case '+':
            # Если в возвращаемом значении присутствует '1j', то '1' в подстроке будет опускаться.
            result = str(a_complex + b_complex)
            if '1j' in result:
                result.replace('1j','j')
            return result
        case '-':
            result = str(a_complex - b_complex)
            if '1j' in result:
                result.replace('1j','j')
            return result
        case '*': 
            result = str(a_complex * b_complex)
            if '1j' in result:
                result.replace('1j','j')
            return result
        case '/': 
            result = str(a_complex / b_complex)
            if '1j' in result:
                result.replace('1j','j')
                return result
            return result