from django.urls import path
from .views import UploadView,home,ResultPage

urlpatterns = [
    path('upload/', UploadView.as_view(), name='upload-results'),
    path('', home, name='index'),
    path('MyRes/', ResultPage, name='rs-page'),

]