from django.test import TestCase
from django.contrib.auth import get_user_model



class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating user with an email is successful"""

        name = 'bayram'
        email = 'test@yahoo.com',
        password = 'test1234'
        user = get_user_model().objects.create_user(
            name=name,
            email=email,
            password=password,
            )

        self.assertEqual(user.name, name)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_uer_email_normalized(self):
        """Test the email for a new user is normalized""" 
                
        email = 'BAYRAM@yahoo.com'
        user = get_user_model().objects.create_user(email, 'test1234') 

        self.assertEqual(user.email, email)


    def test_new_user_invalid_email(self):
        """Test creating new user with no email"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')


    def test_create_new_superuser(self):
        """Test creating new superuser"""

        email = 'test@yahoo.com'
        password = 'test1234'

        user = get_user_model().objects.create_superuser(
            'alak@yahoo.com',
            'test1234',
        )

        self.assertTrue(user.is_superuser)
        self.assert_true(user.is_staff)


        
