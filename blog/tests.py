from django.test import TestCase, Client


class BlogTestCase(TestCase, Client):
    def setUp(self):
        self.c = Client()

    def text_index_accese(self):
        res = self.c.get('/')
        self.assertEqual(1, 1)