from classcat import Pets

cats = [
    {
        'name': 'baron',
        'gender': 'male',
        'age': '2'
    },
    {
        'name': 'sam',
        'gender': 'male',
        'age': '2'
    }
]

for cat in cats:
    c = Pets(name=cat.get('name'), gender=cat.get('gender'), age=cat.get('age'))
    print(c.name)
    print(c.gender)
    print(c.age)