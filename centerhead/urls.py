from django.urls import path

from centerhead import views

urlpatterns = [
            path('adminhome',views.AdminHome.as_view(),name='adminhome'),
            path('createcourse',views.CourseCreate.as_view(),name='coursecreate'),
            path('createbatch',views.BatchCreate.as_view(), name='batchcreate'),
            path('telecallerlist',views.TelecallerList.as_view(),name='telecallerlist'),
            path('deletetelcaller/<int:id>',views.TeleCallerDelete.as_view(),name='deletetelecaller'),
            path('createemployee', views.EmployeeCreate.as_view(), name='employeecreate'),

]