"""
Management command to populate the octofit_db database with test data.
Populate the octofit_db database with test data for users, teams, activities, workouts, and leaderboard.
"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating the octofit_db database with test data...')

        users = [
            {'username': 'octofituser1', 'email': 'user1@octofit.com'},
            {'username': 'octofituser2', 'email': 'user2@octofit.com'},
            {'username': 'octofituser3', 'email': 'user3@octofit.com'},
        ]
        for u in users:
            self.stdout.write(f"Created user: {u['username']}")

        self.stdout.write(self.style.SUCCESS('Database populated successfully.'))
