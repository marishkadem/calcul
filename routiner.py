import logger as lr
import viewer as vr
import real as rr
import complex as rc

def frac_trans(value):
    st = value.split('/')
    st1 = st[0].split()
    return f'{st[0].strip()}/{st[1].strip()}' if len(st1) == 1 else f'{st1[0].strip()} {st1[1].strip()}/{st[1].strip()}'

def calc(first_numb, second_numb, numb_oper):
    lr.log_info(f'{first_numb} {numb_oper} {second_numb}')

    if vr.is_float(first_numb) and vr.is_float(second_numb): 
        first_numb = (float(first_numb),)
        second_numb = (float(second_numb),)
        return rr.calc(first_numb, second_numb, numb_oper)

    if vr.is_frac(first_numb) and vr.is_frac(second_numb):
        first_numb = frac_trans(first_numb)
        second_numb = frac_trans(second_numb)
        return rr.calc(first_numb, second_numb, numb_oper)
    
    if vr.is_complex(first_numb) and vr.is_complex(second_numb):
        first_numb = str(complex(first_numb))
        second_numb = str(complex(second_numb))
        return rc.calc(first_numb, second_numb, numb_oper)
    
    err = 'given numbers have different types or inappropriate format'
    return 