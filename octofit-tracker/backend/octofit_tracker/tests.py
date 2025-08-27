from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@hero.com', name='Test Hero', team='Marvel')
        self.assertEqual(user.name, 'Test Hero')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user_email='test@hero.com', activity_type='Running', duration=30)
        self.assertEqual(activity.activity_type, 'Running')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team='Test Team', points=100)
        self.assertEqual(lb.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', difficulty='Easy')
        self.assertEqual(workout.difficulty, 'Easy')
