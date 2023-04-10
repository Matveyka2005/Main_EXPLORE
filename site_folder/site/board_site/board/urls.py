from board.views import *
from users.urls import users_urlpatterns
from django.urls import path
# !!!!!import cache_page for cache !!!!!!
from django.views.decorators.cache import cache_page


# app_name="board"

urlpatterns = [
    path('detail/<int:pk>/', cache_page(60)(ContentDetailView.as_view()), name="detail"),
    path('update/<int:pk>/', cache_page(20)(BbEditView.as_view()), name='update'),
    path('add/', cache_page(10)(BbCreateView.as_view()), name='add'),
    path('<int:rubric_id>/', ByRubricListView.as_view(), name="by_rubric"),
    path('', MainListView.as_view(), name="main"),
    path('search/', Search.as_view(), name="search"),
] + users_urlpatterns



# handler404 = PageNotFound404()
