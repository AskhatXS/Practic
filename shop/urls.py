from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views


urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='reg_log'),
    path('products/', views.ProductListCreate.as_view(), name='product_list'),
    path('products/<int:pk>/images/', views.ProductImageListCreate.as_view(), name='images'),
    path('products/<int:pk>/comments/', views.CommentListCreate.as_view(), name='comment'),
    path('products/<int:pk>/ratings/', views.RatingListCreate.as_view(), name='rating'),
    path('editors/', views.EditorListCreate.as_view(), name='editor'),
    path('products/c_editors/', views.CommentForEditor.as_view(), name='c_for_edit'),
    path('products/r_editors/', views.RatingForEditor.as_view(), name='r_for_edit'),
    path('products/create/', views.ProductUpdate.as_view(), name='update'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
