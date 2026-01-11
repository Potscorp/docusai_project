from django.urls import path
from . import views
app_name = 'website'



urlpatterns = [
    path('', views.index, name='index'),
    path("upload/", views.upload_page, name="upload"),
    path("result/", views.result_page, name="result"),
    path("reports/", views.reports_list, name="reports"),
    path("analyze/", views.analyze_report, name="analyze"),
    path('ai-doctor/', views.ai_doctor, name='ai_doctor'),
    path('lab-test/', views.lab_test, name='lab_test'),
    path('second-opinion/', views.second_opinion, name='second_opinion'),
    path('blog/', views.blog, name='blog'),
    path('symptoms-guide/', views.symptoms_guide, name='symptoms_guide'),
    path('knowledge-base/', views.knowledge_base, name='knowledge_base'),
    path('glossary/', views.glossary, name='glossary'),
    path('pricing/', views.pricing, name='pricing'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('dashboard/', views.dashboard, name='dashboard'),
]


