from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse, resolve

from tasks.models import Task
from tasks.views import TaskList



client = Client()

"""
Tests for url redirection and access
"""




def create_task(title, description):
    """
    Create a new task with the given 'title' and 'description'
    """
    return Task.objects.create(title="", description=description)


class LoginTestCase(TestCase):

    def test_non_logged_user_redirect_to_logging(self):
        """
        Checking redirection for logging page from 'tasks' page with main page url. For no logged user
        """
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.url, '/login/?next=/')

    def setUp(self):
        """
        Create a new user for further tests
        """
        self.client = Client()
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

    def testLogin(self):
        """
        Test for logging a user into application
        """
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 200)




    # def test_task_create(self):
    #     """
    #     The detail view of a task with a "title" and "description"
    #     """
    #     new_task = create_task(title='title', description='description')
    #     url = reverse('task-delete:title', args=(new_task.id,))
    #     response = self.client.get(url)
    #     print(response)
    #     self.assertContains(response, new_task.title)
