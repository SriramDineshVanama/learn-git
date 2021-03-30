super_heroes = [
    {'name': 'Batman', 'age': '51', 'city': 'Gotham'},
    {'name': 'Ironman', 'age': '49', 'city': 'Atlanta'},
    {'name': 'Spiderman', 'age': '32', 'city': 'Brooklyn'}
]

print(super_heroes)

super_heroes.sort(key= lambda item:item['age'])
print(super_heroes)

super_heroes.sort(key= lambda item:item['city'])
print(super_heroes)

super_heroes.sort(key= lambda item:item['name'])
print(super_heroes)

def sorter(item):
    return item['name']

super_heroes.sort(key=sorter)
print(super_heroes)

super_heroes.sort(key = lambda item: item['age'])
print(super_heroes)