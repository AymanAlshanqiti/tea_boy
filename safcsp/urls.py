"""safcsp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tea_boy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', views.items_list, name='items-list'),
    path('orders/', views.orders_list, name='orders-list'),
    path('orders/create', views.order_create, name='order-create'),
    path('order/delete/<int:order_id>', views.order_delete, name='order-delete'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),

]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


