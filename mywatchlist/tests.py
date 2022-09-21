from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class PageTesting (TestCase):
    def test_html_showed(self):
        # Because it's actually refering to it's main root
        response = Client().get(reverse('mywatchlist:show_watchlist'))
        self.assertEqual(response.status_code, 200)

    def test_xml_showed(self):
        response = Client().get(reverse('mywatchlist:show_xml'))
        self.assertEqual(response.status_code, 200)

    def test_json_showed(self):
        response = Client().get(reverse('mywatchlist:show_json'))
        self.assertEqual(response.status_code, 200)