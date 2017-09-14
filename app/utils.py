import random


# with open('app/static/adjectives.txt', 'r') as file:
#     adjective_list = file.read().split('\n')

# with open('app/static/adjectives.txt', 'r') as file:
#     animal_list = file.read().split('\n')


def generate_url_link_phrase():
    return str(random.randrange(0, 9999)) + '-' + str(random.randrange(0, 9999))
