from django.db import models

# User Model
class User(models.Model):
    USER_TYPES = [('Individual', 'Individual'), ('NGO', 'NGO'), ('Restaurant', 'Restaurant')]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

# Food Post Model
class FoodPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='food_posts')
    food_name = models.CharField(max_length=100)
    food_description = models.TextField()
    food_image = models.ImageField(upload_to='food_images/')
    location = models.CharField(max_length=255)
    expiration_info = models.DateTimeField()
    status = models.CharField(max_length=20, default='Available')

# Claim Model
class Claim(models.Model):
    food_post = models.ForeignKey(FoodPost, on_delete=models.CASCADE, related_name='claims')
    claimer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='claims')
    claim_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

# Interaction Model
class Interaction(models.Model):
    INTERACTION_TYPES = [('Like', 'Like'), ('Bookmark', 'Bookmark'), ('Share', 'Share')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interactions')
    food_post = models.ForeignKey(FoodPost, on_delete=models.CASCADE, related_name='interactions')
    interaction_type = models.CharField(max_length=20, choices=INTERACTION_TYPES)
    interaction_date = models.DateTimeField(auto_now_add=True)

# Donation Model
class Donation(models.Model):
    food_post = models.ForeignKey(FoodPost, on_delete=models.CASCADE, related_name='donations')
    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donations')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donation_date = models.DateTimeField(auto_now_add=True)
