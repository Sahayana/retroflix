from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('',views.base, name='base'),
    path('main/',views.main, name='home'),
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
    path('github/', views.to_github, name='github'),
    path('github/callback/', views.from_github, name='github_login'),
    path('kakao/', views.to_kakao, name='kakao'),
    path('kakao/callback/', views.from_kakao, name='kakako_login'),
    path('logout/', views.log_out, name='logout'),
    path('mypage/',views.my_page, name='mypage'),
    path('pwchange/',views.pw_change, name='pwchange'),
    path('idchange/', views.id_change, name='idchange'),
    path('email_ajax/',views.email_ajax, name='email_ajax'),
    path('certify_ajax/',views.certify_ajax, name='certify_ajax'),
    path('isid/',views.is_id, name='is_id'),
    path('my-modify/',views.my_modify, name='my_modify'),
    path('birth-change/', views.birth_change, name='birth-change'),
    path('gender-change/', views.gender_change, name='gender-change'),
    path('like-or-donlike/',views.like_or_donlike,name='like_or_donlike'),

]