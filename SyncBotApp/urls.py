from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path(route='', view=views.index, name="index"),
    path(route='login/', view=views.login, name="login"),
    path(route='sign-up/', view=views.sign_up, name="sign_up"),
    path(route='home/', view=views.home, name="home"),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('get_response/', views.get_response, name='get_response'),
    
    

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
