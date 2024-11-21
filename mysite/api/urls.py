from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FoodPostViewSet, ClaimViewSet, InteractionViewSet, DonationViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'food_posts', FoodPostViewSet)
router.register(r'claims', ClaimViewSet)
router.register(r'interactions', InteractionViewSet)
router.register(r'donations', DonationViewSet)

urlpatterns = router.urls
