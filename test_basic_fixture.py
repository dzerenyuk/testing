a = [x for x in range(100)]
def scroll():
    global a
    i = a[0:10]
    a = a[10:]
    return i
def scroll_to(item):
    list_of_items = scroll()
    if is_displayed(item, list_of_items) == True:
        return True


def is_displayed(item, list_of_items):
    for x in list_of_items:
        if x == item:
            return True
            break
    scroll_to(item)
print(scroll_to(12))