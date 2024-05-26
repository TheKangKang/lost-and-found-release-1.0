"""
URL configuration for lostAndFound project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app import views, market
from app import manager

urlpatterns = [
    path("admin/", admin.site.urls),
    path("getAll/user/", views.get_users),
    path("addUser/", views.add_user),
    path("getAll/manager/", manager.get_managers),
    path("addManager/", manager.add_manager),
    path("update/user/", views.update_user),
    path("loginUser/", views.login_user),
    path("loginManager/", manager.login_manager),
    path("users/query/", views.query_users),
    path('user/delete/', views.delete_user),
    path('user/update/', views.update_user),
    path('user/deletes/', views.delete_users),
    path('excel/import/', views.import_users_excel),
    path('excel/export/', views.export_users_excel),
    path('upload/', views.upload),
    path("managers/query/", manager.query_managers),
    path('manager/delete/', manager.delete_manager),
    path('manager/update/', manager.update_manager),
    path('manager/deletes/', manager.delete_managers),
    path('excel/Mimport/', manager.import_managers_excel),
    path('excel/Mexport/', manager.export_managers_excel),
    path('Mupload/', manager.upload),

    # 市场
    path("market/deletes/", market.delete_Markets),
    path("market/delete/", market.delete_Market),
    path("market/update/", market.update_Market),
    path("markets/query/", market.query_Markets),
    path("addMarket/", market.add_Market),
    path("getAll/markets/", market.get_Markets),


]

#  允许所有的media文件被访问
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
