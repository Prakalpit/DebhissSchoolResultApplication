# accounts/urls.py
from django.urls import path,include
from .views import SignUpView

urlpatterns = [
    # path('signup/', SignUpView.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
]
'''
The signup window / page should no more exist
'''

