import requests

from ..models import DishItem
def get_urlss(lista_dishes, dicc):
    lista = []
    for dish in lista_dishes: 
        lista_urls_per_dish = []
        for item in dish:
            dish_item = DishItem.objects.filter(name=item).first()
            if dish_item:
                print("ya existe")
                url = dish_item.url # obtener URL del objeto existente
            else:
                print('no existe')
                id = dicc[item]['closest_match_id']
                url = f'https://static.arasaac.org/pictograms/{id}/{id}_300.png'
                response = requests.get(url)
                if response.ok:
                    dish_item = DishItem.objects.create(name=item, url=url) # crear objeto si no existe
            lista_urls_per_dish.append(url)
        lista.append(lista_urls_per_dish)

    return lista
