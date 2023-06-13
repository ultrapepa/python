

def split_name(name):
    first_name, last_name = names = name.split(maxsplit=1)
    return {
        'first_name': first_name,
        'last_name': last_name
    }

def is_palindrome(item):
    item = str(item)
    return item == item[::-1]

def build_list(item, count=1):
    items = []
    for _ in range(count):
        items.append(item)
    return items