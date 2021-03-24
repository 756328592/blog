# 进行users 子应用的视图路由
from django.urls import path
from users.views import registerView

urlpatterns = [
    # Path的第一个参数 路由
    # Path的第二个参数 视图函数名
    path('register/', registerView.as_view(), name='register'),
]
