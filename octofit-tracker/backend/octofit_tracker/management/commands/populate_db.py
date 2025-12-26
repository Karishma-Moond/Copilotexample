from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team='Marvel', is_superhero=True)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team='Marvel', is_superhero=True)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team='DC', is_superhero=True)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team='DC', is_superhero=True)

        # Create activities
        Activity.objects.create(user=tony, type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=clark, type='Flying', duration=120, date=timezone.now().date())

        # Create workouts
        Workout.objects.create(user=tony, name='Iron Suit Training', description='Suit up!', date=timezone.now().date())
        Workout.objects.create(user=steve, name='Shield Practice', description='Shield throws', date=timezone.now().date())
        Workout.objects.create(user=bruce, name='Batcave Workout', description='Gadgets and stealth', date=timezone.now().date())
        Workout.objects.create(user=clark, name='Fortress Training', description='Kryptonian strength', date=timezone.now().date())

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=200)
        Leaderboard.objects.create(team=dc, points=180)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
