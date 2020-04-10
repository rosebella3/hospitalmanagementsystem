from django.urls import path
from .views import dash, PatientCreate, PatientUpdate, PatientListView,\
                     CreateBill, BillListView, RequestTest, TestListView,\
                    CreateUser, UpdateUser, UsersListView, EditBill, UpdateTest,\
                     PatientDetail, BillDetail, TestDetail, UserDetail

urlpatterns = [
    path('', dash.as_view(), name='home'),
    path('add_patient', PatientCreate.as_view(), name="addpatient"),
    path('edit/<slug:pk>/patient', PatientUpdate.as_view(), name='update_patient'),
    path('patient/<slug:pk>/', PatientDetail.as_view(), name='patient_detail'),
    path('all_patients', PatientListView.as_view(), name='all_patients'),
    path('create_bill', CreateBill.as_view(), name='create_bill'),
    path('all_bills', BillListView.as_view(), name='all_bills'),
    path('bill/<slug:pk>/', BillDetail.as_view(), name='bill_detail'),
    path('request_test', RequestTest.as_view(), name='request_test'),
    path('all_tests', TestListView.as_view(), name='all_tests'),
    path('test/<slug:pk>/', TestDetail.as_view(), name='test_detail'),
    path('create_user', CreateUser.as_view(), name='create_user'),
    path('edit/<int:pk>/user', UpdateUser.as_view(), name='update_user'),
    path('user/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('all_users', UsersListView.as_view(), name='all_users'),
    path('edit/<int:pk>/bill', EditBill.as_view(), name='edit_bill'),
    path('edit<int:pk>/test', UpdateTest.as_view(), name='edit_test'),
    
]