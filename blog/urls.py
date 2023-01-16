from django.urls import path
# Project
from . import views
from . import mails
app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    # path('send-email/', mails.send_email, name='send_email'),
]