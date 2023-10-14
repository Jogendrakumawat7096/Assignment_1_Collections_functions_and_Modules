'''
Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
300}, o {'item': 'item1', 'amount': 750}]
'''

data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]


combined = {}


for dict in data:
    if dict['item'] in combined:
        combined[dict['item']] += dict['amount']
    else:
        combined[dict['item']] = dict['amount']


print(combined)