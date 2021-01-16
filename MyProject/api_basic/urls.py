from django.urls import path,include
from .views import article_list,article_detail,ArticleAPIView,ArticlesDetails,GenricAPIView ,ArticleViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenVerifyView

router=DefaultRouter()
router.register('article',ArticleViewSet,basename='article')

urlpatterns = [
	path('viewset/',include(router.urls)),
	path('viewset/article/<int:pk>/',include(router.urls)),
	# path('article/',ArticleAPIView.as_view()),
	path('article/',article_list),
	path('generic/article/<int:id>/',GenricAPIView.as_view()),
	# path('detail/<int:pk>',article_detail)
	# path('detail/<int:id>',ArticlesDetails.as_view())

	# jwt
	path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
	path('refershtoken/',TokenRefreshView.as_view(),name='token_refresh'),
	path('verifytoken/',TokenVerifyView.as_view(),name='token_verify'),
]
