"""Responsible for test NumberResource class

"""

import json
from unittest import TestCase
from api.app import APP
from api.settings import MAX_NUMBER_SUPPORT, MIN_NUMBER_SUPPORT


class NumberResourceTestCase(TestCase):
    """Responsible for test NumberResource class

    """

    def setUp(self):
        """Create the client object

        """
        self.client = APP.test_client()

    def test_get_without_number(self):
        """Test the get method when number is None

        """
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 400)

        data = json.loads(resp.data)

        self.assertDictEqual(
            data,
            {
                'message': 'Need to inform a number between %s and %s to convert' % (
                    MAX_NUMBER_SUPPORT, MIN_NUMBER_SUPPORT
                )
            }
        )

    def test_get_invalid_number(self):
        """Test the get method when received a invalid number

        """
        resp = self.client.get('/999999')
        self.assertEqual(resp.status_code, 400)

        data = json.loads(resp.data)

        self.assertDictEqual(
            data,
            {
                'message': 'Number need to be a value between %s and %s' % (
                    MAX_NUMBER_SUPPORT, MIN_NUMBER_SUPPORT
                )
            }
        )
