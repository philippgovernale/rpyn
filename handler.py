
import var
import stackop
import screen
import time

def num_handle():
    if var.key == '0' and var.leadingzero == False:
        print "set leadingzero"
        var.leadingzero = True
    elif var.number is None:
        var.number = int(var.key)
    elif var.number:
        var.number = int(str(var.number) + var.key)

    var.tostack = False

def add_decimal(num, dec_ins_loc):
    tot_num_len = len(str(num))
    if tot_num_len == dec_ins_loc:
        num = float(num)
    elif dec_ins_loc == 0:
        num = float('0.' + str(num))
    else:
        num = float(str(num)[:dec_ins_loc] + '.' + str(num)[-(tot_num_len - dec_ins_loc):])
    var.number = num


def match_and_operate(keyw):
    if keyw in var.operation_single:
        stackop.adv_operate_single(var.ADV_OPERATORS[keyw])
    elif keyw in var.operation_double:
        stackop.adv_operate_double(var.ADV_OPERATORS[keyw])
    elif keyw in var.operation_none:
        stackop.adv_operate_none(var.MATHS_CONSTANTS[keyw])
    elif keyw in var.operation_custom:
        var.ADV_OPERATORS[var.keyword]()


def operator_handler(operator):
    if not var.tostack:
        if var.number is not None:
            if var.decimal:
                add_decimal(var.number, var.decimal_insert)
                var.decimal = False
            var.stack.append(float(var.number))
        var.tostack = True
    stackop.operate(operator)
    var.number = None



def character_handler(char):
    var.command = True
    if var.comhelp:
        var.helpcommand += char
        if var.helpcommand[1:] in var.ADV_OPERATORS:
            screen.clear()
            screen.write(var.ADV_OPERATORS[var.helpcommand[1:]].__doc__)
            raw_input('\nPress enter to continue')
            screen.clear()
            var.comhelp = False
            var.keyword = None
            var.number = None
    elif var.keyword is None:
        var.keyword = var.key
        if var.keyword in var.ADV_OPERATORS or var.keyword in var.MATHS_CONSTANTS:
            match_and_operate(var.keyword)
            var.keyword = None
            var.number = None
    else:
        var.keyword += char
        if var.keyword in var.ADV_OPERATORS or var.keyword in var.MATHS_CONSTANTS:
            match_and_operate(var.keyword)
            var.keyword = None
            var.number = None



def decimal_handler():
    if var.number == None or var.number == 0:
        var.decimal_insert = 0
    else:
        var.decimal_insert = len(str(var.number))
    var.decimal = True
