from horizon.test import helpers as test


class HelloTests(test.TestCase):
    # Unit tests for hello.
    def test_me(self):
        self.assertTrue(1 + 1 == 2)
