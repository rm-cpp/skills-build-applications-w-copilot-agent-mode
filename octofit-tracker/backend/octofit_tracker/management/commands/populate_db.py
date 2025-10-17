
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB to create unique index on email
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']
        db.users.create_index('email', unique=True)

        # Clear all collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel.name),
            User.objects.create(email='captainamerica@marvel.com', name='Captain America', team=marvel.name),
            User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team=marvel.name),
            User.objects.create(email='batman@dc.com', name='Batman', team=dc.name),
            User.objects.create(email='superman@dc.com', name='Superman', team=dc.name),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team=dc.name),
        ]

        # Activities
        Activity.objects.create(user='Iron Man', type='Running', duration=30, date=date(2025, 10, 1))
        Activity.objects.create(user='Captain America', type='Cycling', duration=45, date=date(2025, 10, 2))
        Activity.objects.create(user='Spider-Man', type='Swimming', duration=25, date=date(2025, 10, 3))
        Activity.objects.create(user='Batman', type='Running', duration=40, date=date(2025, 10, 1))
        Activity.objects.create(user='Superman', type='Cycling', duration=60, date=date(2025, 10, 2))
        Activity.objects.create(user='Wonder Woman', type='Swimming', duration=35, date=date(2025, 10, 3))

        # Leaderboard
        Leaderboard.objects.create(team=marvel.name, points=100)
        Leaderboard.objects.create(team=dc.name, points=120)

        # Workouts
        Workout.objects.create(name='Push Ups', description='Do 3 sets of 15 push ups', difficulty='Easy')
        Workout.objects.create(name='5K Run', description='Run 5 kilometers', difficulty='Medium')
        Workout.objects.create(name='HIIT', description='20 min high intensity interval training', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data!'))
