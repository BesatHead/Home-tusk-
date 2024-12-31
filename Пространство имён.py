calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    length = len(string)
    upper_register = string.upper()
    lower_register = string.lower()
    return length, upper_register, lower_register

def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in (item.lower() for item in list_to_search)

print(string_info('Cowboy Bebop'))
print(string_info('Evangelion'))
print(is_contains('Hunter_X_Hunter', ['hunter_x_hunter', 'XHunter', '_Hunter']))
print(is_contains('Golden_Boy', ['Golden', 'Boy', 'boy_golden']))

print(calls)
