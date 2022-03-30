from django.urls import path
# from sayhello.views import HelloWorldView
from helloapp.views import HelloWorldView, HelloView, Goodbye

urlpatterns = [
    # helloapp/
    path('', HelloWorldView.as_view(), name='hello_world'),
    path('<name>', HelloView.as_view(), name='hello_name'),
    path('goodbye/<name>', Goodbye.as_view(), name='goodbye_name'),
]
