from collections import Counter

def top_3_frequentes(lista):
    return [item[0] for item in Counter(lista).most_common(3)]

print(top_3_frequentes([1, 2, 2, 3, 3, 3, 4]))  
