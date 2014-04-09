from django import test
from django.core.urlresolvers import reverse

class BasicTestCase(test.TestCase):

    def test_default_image(self):
        '''Basic test to make sure it doesn't fail.'''
        self.client.get(reverse('tyler.views.get_image'))
