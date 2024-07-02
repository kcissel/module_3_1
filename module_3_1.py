calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains (string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]


print(string_info('Paramedic'))
print(string_info('America'))
print(is_contains('Shake', ['smoke', 'Shot', 'shAKe']))
print(is_contains('mom', ['mommy', 'money']))
print(calls)
