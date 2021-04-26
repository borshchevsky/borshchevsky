from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views
from django.conf import settings

from .validators import group_check

urlpatterns = [
                  path('', views.index, name='index'),
                  path('goods/', views.ProductListView.as_view(), name='goods'),
                  path('goods/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
                  path('accounts/profile/', login_required(views.ProfileUpdate.as_view()),
                       name='profile-update'),
                  path('goods/add', group_check(views.CreateProduct.as_view()), name='goods-add'),
                  path('goods/<int:pk>/edit', group_check(views.UpdateProduct.as_view()), name='goods-edit'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
