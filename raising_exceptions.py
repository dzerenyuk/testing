'''def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string')
    if width <= 2:
        raise Exception('Width must be greater than 2')
    if height <= 2:
        raise Exception('Height must be greater than 2')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2))+ symbol)
    print(symbol * width)
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        box_print(sym, w, h)
    except Exception as err:
        print('An exception occured: ' + str(err))
'''
import traceback
try:
    raise Exception('This is the error message')
except:
    error_file = open('errorInfo.txt', 'w')
    error_file.write(traceback.format_exc())
    error_file.close()
    #print('The traceback info was written to errorInfo.txt')
file = open('errorInfo.txt')
print(file.readlines())