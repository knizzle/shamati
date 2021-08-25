import itertools

heb_word = [['ד'], ['א', 'ה', 'ע', ''], ['ף']]

results = list(itertools.product(*heb_word))
print(results)

for result in results:
    result = ''.join(result)
    print(result)