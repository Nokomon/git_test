from django.urls import path
# from . import views
import blogapp.views

urlpatterns = [
    path('post/<int:num>', blogapp.views.detail, name='detail'),
    path('new', blogapp.views.new, name='new'),
    path('new/create', blogapp.views.create, name='create'),
    path('update/<int:num>', blogapp.views.update, name='update'),
    path('delete/<int:num>', blogapp.views.delete, name='delete'),
    path('album/', blogapp.views.album, name='album'),
] 