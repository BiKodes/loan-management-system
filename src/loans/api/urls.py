from django.urls import path
from blog.api.views import (
    loan_create_view,
    loan_detail_veiw,
    loan_update_detail_view,
    loan_delete_details_view
    )

app_name = 'loans'

urlpatterns = [
    path('<slug>/', loan_detail_veiw, name='detail'),
    path('<slug>/update', loan_update_detail_view, name='update'),
    path('<slug>/delete', loan_delete_details_view, name='delete'),
    path('create', loan_create_view, name='create')
]