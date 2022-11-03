from django.test import TestCase
from my_admin.models import Customer

# Create your tests here.
class CustomerLoginTest(TestCase):
    def setUp(self):
        Customer.objects.create(username="AnthonyTan", password_hash='3cceea5b8fb7d5ced3f0ea6162e83a7a',
                                password_salt='717604', name='Anthony', phone=123456789,
                                email='test@163.com', bank_card=1234)

    def test_login_success(self):
        session = self.client.session
        session['verifyCode'] = '2333'
        # session['csrfmiddlewaretoken'] = 'rg2eQEGY0Fs6LG6cgmXn6kc2NbsB4832UGkV8EXl7ms3QEDVmK0dsXrYL6BSseS4'
        session.save()
        response = self.client.post('/movie_web/login',
                                    {'username': 'AnthonyTan', 'password': '12345678', 'verifyCode': '2333'})
        self.assertEqual(response.status_code, 302)

    def test_login_fail(self):  # password is incorrect
        session = self.client.session
        session['verifyCode'] = '2333'
        # session['csrfmiddlewaretoken'] = 'rg2eQEGY0Fs6LG6cgmXn6kc2NbsB4832UGkV8EXl7ms3QEDVmK0dsXrYL6BSseS4'
        session.save()
        response = self.client.post('/movie_web/login',
                                    {'username': 'AnthonyTan', 'password': '1234567', 'verifyCode': '2333'})
        self.assertIn(b'password is incorrect', response.content)
