def validate_input(c_pass,defer,fail):
    if c_pass.isdigit() and defer.isdigit() and fail.isdigit():
        valid_status = 1
    else:
        valid_status = 0

    return valid_status

def validate_total(c_pass,defer,fail):
    total = int(c_pass) + int(defer) + int(fail)
    if total == 120:
        valid_status = 1
    else:
        valid_status = 0

    return valid_status

def validate_range(c_pass,defer,fail):
    c_pass = int(c_pass)
    defer  = int(defer)
    fail   = int(fail)
    value_list = [c_pass,defer,fail]
    valid_status = 1
    for val in value_list:
      if val in range(0,140,20):
        if valid_status != 0:
            valid_status = 1
      else:
        valid_status = 0
    return valid_status

def progression_outcome(c_pass,defer,fail):
    result = ''
    c_pass = int(c_pass)
    defer  = int(defer)
    fail   = int(fail)
    if c_pass == 120 :
        result = "Progress"
    elif c_pass == 100 :
        result = "Progress – module trailer"
    elif fail >= 80 :
        result = "Exclude "
    else :
        result = "Do not progress – module retriever"

    return result

def studentVersion():
    result = ''
    c_pass = input("Enter the Pass Credit :")
    defer  = input("Enter Defer Credit :")
    fail   = input("Enter Fail Credit :")

    if   validate_input(c_pass,defer,fail) == 0:
        result = 'Integers required'
    elif validate_range(c_pass,defer,fail) == 0:
        result = 'Range error'
    elif validate_total(c_pass,defer,fail) == 0:
        result = 'Total incorrect'
    else:
        result = progression_outcome(c_pass,defer,fail)

    return result


def staffVersion():
    dict_histogram = {
    'Progress'  : 0,
    'Trailing'  : 0,
    'Retriever' : 0,
    'Excluded'  : 0,
    }
    flag = 1
    while (flag):
        userInput = input('Enter Any Text To Continue... Press q To Quit : ')
        if userInput != 'q':
            output = studentVersion()
            if output == 'Progress':
                dict_histogram['Progress'] = dict_histogram['Progress'] + 1
            elif output == 'Progress – module trailer':
                dict_histogram['Trailing'] = dict_histogram['Trailing'] + 1
            elif output == 'Do not progress – module retriever':
                dict_histogram['Retriever'] = dict_histogram['Retriever'] + 1
            else:
                dict_histogram['Excluded'] = dict_histogram['Excluded'] + 1
        else:
            for dict_val in dict_histogram:
                print(dict_val,' ',dict_histogram[dict_val],': ',dict_histogram[dict_val]* '*')
            print(sum(dict_histogram.values()),' outcomes in total.')
            exit()


print('Enter the option to continue...\n1 - Student Version\n2 - Staff Version')
opt = int(input('Enter the option : '))
if opt == 1:
    result = studentVersion()
    print('Output : ',result)
elif opt == 2:
    staffVersion()

