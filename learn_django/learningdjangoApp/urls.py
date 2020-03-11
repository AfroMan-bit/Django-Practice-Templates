from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('signup', views.showsignupPage),
    path('signup/premium', views.showspremiumMembers),
    path('show/<int:itemId>', views.showinteger_only),
    path('profile/<itemId>', views.showitem_integer_or_words),
    path('logout', views.logout),
]

