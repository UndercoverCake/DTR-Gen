from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
	path('', views.home, name="home"),
	path('adminpanel/', views.register, name="adminpanel"),
    path('change-password/<int:user_id>/', views.change_password, name='change-password'),
	path('preview/', views.preview, name="preview"),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),
    path('form/', views.saveTimes, name="saveTimes"),
    path('deactivate-user/<int:user_id>/', views.deactivate_user, name='deactivate-user'),
    path('activate-user/<int:user_id>/', views.activate_user, name='activate-user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete-user'),
    path('adminpanel/search', views.searchBar, name='searchBar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)