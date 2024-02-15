# urls.py
from django.urls import path
from .views import predict_food

urlpatterns = [
    path('predict_food/', predict_food, name='predict_food'),
    # 다른 URL 패턴들을 추가할 수 있습니다.
]
