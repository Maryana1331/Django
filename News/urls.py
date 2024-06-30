from django.urls import path

from News import views
from News.views import HomeNews, NewsByCategory, ViewNews, AddNews,register, user_login, user_logout

# from News.views import index,get_category,view_news,add_news, test

urlpatterns = [
    path('', HomeNews.as_view(), name='Home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='Category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='View_news'),
    path('news/add_news', AddNews.as_view(), name='Add_news'),
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('logout', user_logout, name="logout"),

    #path('test/', test, name='test'),
    # path('', index, name='Home'),
    # path('category/<int:category_id>/', get_category, name='Category'),
    # path('news/<int:pk>/', views.view_news, name='view_news'),
    # path('news/add_news', add_news, name='Add_news'),
]
