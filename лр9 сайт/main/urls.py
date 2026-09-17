from django.urls import path
from .views import home, about  # Добавили импорт функции about

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),  # Новый адрес для второй страницы
]