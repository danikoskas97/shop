import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_project.settings')
import django
django.setup()

import random
from faker import Faker
from shop_app.models import Client, Product

# CONSIGNE
# creez 2 fonctions :
#   1. cree 1000 faux clients
#   2. cree 50 faux produits

fakegen = Faker()

def generate_brand():
    brands = ["Nike", "Adidas", "Reebook","Jordan","Banlenciaga" ,"asics", "Timberland", "Puma", "Fila",
    "Geox"]
    # pk index? 
    index = random.randint(0, 9)
    return brands[index]


def generate_clients():
    for client in range(1000):
        client = Client.objects.get_or_create(first_name=fakegen.first_name(), last_name=fakegen.last_name(), email=fakegen.email(), password=fakegen.password())[0]
        print(client)
        # client[0].save()

    
def generate_products():
    for product in range(50):
        price = random.randint(60, 400)
        # pk tu met brand ds cette def?
        brand = generate_brand()
    

        product = Product.objects.get_or_create(name=brand, price=price,description=fakegen.text(max_nb_chars=400))[0]
        print(product)
        


def populate():
    # generate_clients()
    generate_products()








if __name__ == '__main__':
  print('starting populate...')
  populate()
  print('done populating')



