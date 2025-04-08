from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(_id=ObjectId(), username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
            User(_id=ObjectId(), username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
            User(_id=ObjectId(), username='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword'),
            User(_id=ObjectId(), username='crashoverride', email='crashoverride@mhigh.edu', password='crashoverridepassword'),
            User(_id=ObjectId(), username='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(_id=ObjectId(), name='Blue Team')
        team2 = Team(_id=ObjectId(), name='Gold Team')
        # Convert User objects to dictionaries before assigning to the members field
        team1.members = [user.__dict__ for user in [users[0], users[1]]]
        team2.members = [user.__dict__ for user in [users[2], users[3], users[4]]]
        team1.save()
        team2.save()

        # Create activities
        # Convert User objects to dictionaries before assigning to the user field in Activity
        activities = [
            Activity(_id=ObjectId(), user=users[0].__dict__, activity_type='Cycling', duration=timedelta(hours=1)),
            Activity(_id=ObjectId(), user=users[1].__dict__, activity_type='Crossfit', duration=timedelta(hours=2)),
            Activity(_id=ObjectId(), user=users[2].__dict__, activity_type='Running', duration=timedelta(hours=1, minutes=30)),
            Activity(_id=ObjectId(), user=users[3].__dict__, activity_type='Strength', duration=timedelta(minutes=30)),
            Activity(_id=ObjectId(), user=users[4].__dict__, activity_type='Swimming', duration=timedelta(hours=1, minutes=15)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        # Convert User objects to dictionaries before assigning to the user field in Leaderboard
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0].__dict__, score=100),
            Leaderboard(_id=ObjectId(), user=users[1].__dict__, score=90),
            Leaderboard(_id=ObjectId(), user=users[2].__dict__, score=95),
            Leaderboard(_id=ObjectId(), user=users[3].__dict__, score=85),
            Leaderboard(_id=ObjectId(), user=users[4].__dict__, score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event'),
            Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition'),
            Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon'),
            Workout(_id=ObjectId(), name='Strength Training', description='Training for strength'),
            Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        # Add debug statements to log data being processed
        self.stdout.write(self.style.NOTICE(f"Users: {users}"))
        self.stdout.write(self.style.NOTICE(f"Team1 Members: {team1.members}"))
        self.stdout.write(self.style.NOTICE(f"Activities: {activities}"))
        self.stdout.write(self.style.NOTICE(f"Leaderboard Entries: {leaderboard_entries}"))
        self.stdout.write(self.style.NOTICE(f"Workouts: {workouts}"))

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
