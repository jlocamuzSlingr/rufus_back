from rest_framework import viewsets
from rest_framework.response import Response

from .utils.foto_a_texto import obtener_texto_imagen
from .models import Menu, Dish, DishItem
from .serializers import MenuSerializer, DishSerializer, DishItemSerializer
from .utils.dish_to_tag import get_closest_matches
from .utils.dish_to_tag import get_menu_items
from .utils.get_urls import get_urlss

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = response.data
        texto = obtener_texto_imagen(data) #[['milanesa de cerdo', 'papas fritas'], ['pancho', 'nuggets'], ['hamburguesa', 'fritas']]
        d = get_menu_items(texto, data)
        lista_of_urls_perdish = get_urlss(texto, get_closest_matches(d))
        return Response({'lista_of_urls_perdish': lista_of_urls_perdish})

    def list(self, request, *args, **kwargs):
        path_imagen = 'staticfiles/rest_framework/img/MENU_5XSjgIX.jpeg'
        #texto_imagen = obtener_texto_imagen(path_imagen)
        #print(texto_imagen)

        return super().list(request, *args, **kwargs)
class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class DishItemViewSet(viewsets.ModelViewSet):
    queryset = DishItem.objects.all()
    serializer_class = DishItemSerializer
