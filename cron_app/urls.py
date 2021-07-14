from django.urls import  path,include
from .views import StudentView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('student_api',StudentView,basename='student_api')

app_name='cron_app'

urlpatterns=[
    path('',include(router.urls)),
]
