from django.urls import path

from telecaller import views

urlpatterns = [

    path('createemployee',views.EmployeeCreate.as_view(), name='employeecreate'),
    path('createstudent', views.StudentCreate.as_view(), name='studentcreate'),
    path('updatestudent/<int:id>',views.StudentUpdate.as_view(),name='updatestudent'),
    path('deletestudent/<int:id>',views.StudentDelete.as_view(),name='deletestudent'),
    path('ajax/load_cities/',views.load_cities,name='ajax_load_cities'),
    path('enquiries',views.EnquiriesList.as_view(), name='enquirieslist'),
    path('telehome', views.TeleHome.as_view(), name='telehome'),
    path('batchlist',views.BatchList.as_view(),name='batchlist')
]
