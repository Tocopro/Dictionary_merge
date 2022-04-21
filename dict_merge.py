# dictionary merge

dict_a = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict_b = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

dict_c = {**dict_a, **dict_b}
print(dict_c)

