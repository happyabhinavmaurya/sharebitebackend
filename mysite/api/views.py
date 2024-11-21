from rest_framework import viewsets
from .models import User, FoodPost, Claim, Interaction, Donation
from .serializers import UserSerializer, FoodPostSerializer, ClaimSerializer, InteractionSerializer, DonationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FoodPostViewSet(viewsets.ModelViewSet):
    queryset = FoodPost.objects.all()
    serializer_class = FoodPostSerializer

class ClaimViewSet(viewsets.ModelViewSet):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
