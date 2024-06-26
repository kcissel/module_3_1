calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    string = (len(string), string.upper(), string.lower())
    print(string)
    return count_calls()
def is_contains(string, list_to_search):
    if string in list_to_search:
        print(True)
    else:
        print(False)
    return count_calls()


print(string_info('Paramedic'))
print(string_info('America'))
print(is_contains('Shake', ['smoke', 'Shot', 'shAKe']))
print(is_contains('mom', ['mommy', 'money']))
print(calls)
