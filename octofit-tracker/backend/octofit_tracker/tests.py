from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Test', email='test@example.com', team='Marvel', is_superhero=True)
        self.assertEqual(user.name, 'Test')
        self.assertEqual(user.team, 'Marvel')
        self.assertTrue(user.is_superhero)

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', description='Superhero team')
        self.assertEqual(team.name, 'Marvel')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(name='Test', email='test2@example.com', team='DC', is_superhero=True)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2025-12-23')
        self.assertEqual(activity.type, 'Running')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(name='Test', email='test3@example.com', team='Marvel', is_superhero=True)
        workout = Workout.objects.create(user=user, name='Pushups', description='Upper body', date='2025-12-23')
        self.assertEqual(workout.name, 'Pushups')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='DC', description='Superhero team')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)
