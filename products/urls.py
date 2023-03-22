

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from  products.views import products, basket_add, basket_delete

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),

    path('category/<int:category_id>/',products, name='category'),# фильтрация по категориям

    path('page/<int:page_number>/',products, name='paginator'), # пагинация

    path('basket-add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket-delete/<int:id>/', basket_delete, name='basket_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
