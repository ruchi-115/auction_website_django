# Generated by Django 3.2.9 on 2021-12-11 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid_comment_listing_watchlist_winner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='listing_id',
            new_name='listingid',
        ),
    ]
