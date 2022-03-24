from django.urls import path 
from .views import LugarView, AvistamientoView, EspecieView
urlpatterns = [
    path('lugares/', LugarView.as_view(), name='lugares_list'),
    path('lugares/<int:id>', LugarView.as_view(), name='lugares_process'),
    path('especies/', EspecieView.as_view(), name='especies_list'),
    path('especies/<int:id>', EspecieView.as_view(), name='especies_process'),
    path('avistamientos/', AvistamientoView.as_view(), name='avistamientos_list'),
    path('avistamientos/especies/<int:ide>', AvistamientoView.as_view(), name='avistamientos_by_especies_process'),

]
