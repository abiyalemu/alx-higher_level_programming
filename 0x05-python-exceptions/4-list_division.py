#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_dv = []
    for k in range(0, list_length):
        try:
            quotient = my_list_1[k] / my_list_2[k]
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except (ValueError, TypeError):
            print("wrong type")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            list_dv.append(quotient)
    return list_dv
