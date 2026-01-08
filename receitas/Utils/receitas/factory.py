from random import randint
from faker import Faker

fake = Faker('pt_BR')
categories = ['Sobremesa', 'Entrada', 'Prato Principal', 'Bebida']
current_id = 1

def rand_ratio():
    return randint(840, 900), randint(473, 573)

def make_receitas():
    global current_id
    receita = {
        'id': current_id,
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porção',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time_this_year(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.random_element(categories)
        },
        'cover': {
            'url': f'https://picsum.photos/{randint(840,900)}/{randint(473,573)}'
        }
    }
    current_id += 1
    return receita

if __name__ == '__main__':
    from pprint import pprint
    pprint(make_receitas())
