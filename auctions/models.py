from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

#Auction Listing model
class Listing(models.Model):
    seller = models.CharField(max_length=64)
    item_name = models.CharField(max_length=64)
    item_description = models.TextField(max_length=100)
    current_bid = models.IntegerField()
    category = models.CharField(max_length=64)
    img_url = models.CharField(max_length=200, default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

#Model For Bids
class Bid(models.Model):
    bid = models.IntegerField()
    user = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    listingid = models.IntegerField()

#Model for comments
class Comment(models.Model):
    user = models.CharField(max_length=64)
    comment = models.CharField(max_length=200)
    listingid = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

# model for watchlist
class Watchlist(models.Model):
    user = models.CharField(max_length=64)
    listingid = models.IntegerField()

# model to store the winners
class Winner(models.Model):
    owner = models.CharField(max_length=64)
    winner = models.CharField(max_length=64)
    listingid = models.IntegerField()
    winprice = models.IntegerField()
    title = models.CharField(max_length=64, null=True)