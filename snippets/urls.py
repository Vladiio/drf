from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from snippets import views


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


# snippet_list = views.SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# snippet_detail = views.SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# snippet_highlight = views.SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=(renderers.StaticHTMLRenderer,))

# user_list = views.UserViewSet.as_view({
#     'get': 'list',
# })

# user_detail = views.UserViewSet.as_view({
#     'get': 'retrieve',
# })

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('obtain-auth-token/', obtain_auth_token),
    path('', include(router.urls)),

]
