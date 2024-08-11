calls = 0
def count_calls ():
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls ()
    kort1 = (len(string),string.upper(),string.lower())
    if kort1 is not None:
        return print (kort1)




def is_contains(string,list_to_search):
    count_calls()
    list_to_search_lower = [li.lower() for li in list_to_search]
    string_lower = string.lower()
    if list_to_search_lower.count(string_lower):
        r = True
    else:
        r = False
    if r is not None:
        return print(r)

#print(string_info('Capybara'))
#print(string_info('Armageddon'))
#print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
#print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
#print(calls)

string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN']) # Urban ~ urBAN
is_contains('cycle', ['recycling', 'cyclic']) # No matches
print(calls)