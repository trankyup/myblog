from django.urls import path

from . import  views
app_name = '[blog]'
urlpatterns = [
    path('index/', views.index),#用^$约束空字符串
    path('article/<int:article_id>', views.article_page,name = 'article_page'),
    path('edit/<int:article_id>', views.edit_page,name='edit_page'),
    path('edit/action/', views.edit_action,name='edit_action')
]

