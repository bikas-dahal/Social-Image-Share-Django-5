from django.urls import path, include
from. import views

urlpatterns = [
    
    path('post/<int:pk>/delete', views.BlogDeleteView.as_view(), name='blog_delete'),
    path('post/<int:pk>/edit', views.BlogUpdateView.as_view(), name='blog_edit'),
    path('post/new/', views.BlogCreateView.as_view(), name='create_blog'),
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('test', views.test, name='test')
] 

