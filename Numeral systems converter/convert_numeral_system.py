# converting a number from sys_start to sys_end
def convert_num_sys(sys_start, sys_end):
    number = result = input('Write an integer number')
    if not number.isdigit():
        return 'Dude, an integer number means not float or string argument!!!'
    match sys_start:
        case 10:
            result = convert_from_dec(number, sys_end)
        case 2:
            result = convert_from_bin(number, sys_end)
        case 8:
            result = convert_from_oct(number, sys_end)
        case 16:
            result = convert_from_hex(number, sys_end)
    return result


def convert_from_dec(dec_num, sys_end):
    result = dec_num
    match sys_end:
        case 2:                                         # convert from dec to bin
            result = str(bin(dec_num))[2:]
        case 8:                                         # convert from dec to oct
            result = str(oct(dec_num))[2:]
        case 16:                                        # convert from dec to hex
            result = str(hex(dec_num))[2:].upper()
    return result


def convert_from_bin(bin_num, sys_end):
    result = bin_num
    match sys_end:
        case 8:                                         # convert from bin to oct
            dec_num = int(bin_num, 2)
            result = str(oct(dec_num))[2:]
        case 10:                                        # convert from bin to dec
            result = int(bin_num, 2)
        case 16:                                        # convert from bin to dec
            dec_num = int(bin_num, 2)
            result = str(hex(dec_num))[2:].upper()
    return result


def convert_from_oct(oct_num, sys_end):
    result = oct_num
    match sys_end:
        case 2:                                         # convert from oct to bin
            result = str(bin(int(oct_num, 8)))[2:]
        case 10:                                        # convert from oct to dec
            result = int(oct_num, 8)
        case 16:                                        # convert from oct to hex
            result = str(hex(int(oct_num, 8)))[2:].upper()
    return result


def convert_from_hex(hex_num, sys_end):
    result = hex_num
    match sys_end:
        case 2:                                         # convert from hex to bin
            dec_num = int(hex_num)
            result = str(bin(dec_num))[2:].upper()
        case 8:                                         # convert from hex to oct
            dec_num = int(hex_num)
            result = str(oct(dec_num))[2:]
        case 10:                                        # convert from hex to dex
            result = int(hex_num)
    return result


# checking the number system for compliance with the list available
def wrong_system(system):
    while (not system.isdigit()) or (system not in [2, 8, 10, 16]):
        if not system.isdigit():
            print('Please, write a numeric answer')
        elif system not in [2, 8, 10, 16]:
            print("I can't convert from that system :( Please, write any system from this list:")
            print('2, 8, 10, 16')

        system = input('From which system you want to convert number?\n')

    return system


do_you_want = input('Do you want to convert number? (yes/no)\n')

if do_you_want in ['yes', 'y', 'да', 'д']:
    system_start = input('From which system you want to convert number?\n')
    system_start = wrong_system(system_start)
    system_end = input('To which system you want to convert number?\n')
    system_end = wrong_system(system_end)
    print(convert_num_sys(system_start, system_end))
else:
    print('Sorry to bother you. Have a nice day!')
