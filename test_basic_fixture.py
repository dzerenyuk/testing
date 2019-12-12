a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, 21,22]
def scroll():
    global a
    i = a[0:10]
    a = a[10:]
    return i
def scroll_to(item):
    list_of_items = scroll()
    x = is_displayed(item, list_of_items)
    return x
def is_displayed(item, list_of_items):
    if item in list_of_items:
        return True
    elif len(list_of_items) < 10:
        return False
    else:
        scroll_to(item)

print(scroll_to(12))