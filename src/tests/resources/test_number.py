"""Responsible for test NumberResource class

"""

import json
from unittest import TestCase
from api.app import APP
from api.defines import MAX_NUMBER_SUPPORT, MIN_NUMBER_SUPPORT


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

    def test_get_number_0(self):
        """Test the get method with 0

        """
        resp = self.client.get('/0')
        self.assertEqual(resp.status_code, 200)

        data = json.loads(resp.data)

        self.assertDictEqual(
            data,
            {
                'extenso': 'zero'
            }
        )

    def test_get_number_1(self):
        """Test the get method with 1

        """
        resp = self.client.get('/1')
        self.assertEqual(resp.status_code, 200)

        data = json.loads(resp.data)

        self.assertDictEqual(
            data,
            {
                'extenso': 'um'
            }
        )

    def test_get_number_12(self):
        """Test the get method with 12

        """
        resp = self.client.get('/12')
        self.assertEqual(resp.status_code, 200)

        data = json.loads(resp.data)

        self.assertDictEqual(
            data,
            {
                'extenso': 'doze'
            }
        )

    def test_get_number_100(self):
        """Test the get method with 100

        """
        resp = self.client.get('/100')
        self.assertEqual(resp.status_code, 200)

        data = json.loads(resp.data)

        self.assertDictEqual(
            data,
            {
                'extenso': 'cem'
            }
        )

    def test_get_number_1112(self):
        """Test the get method with 1112

        """
        resp = self.client.get('/1112')
        self.assertEqual(resp.status_code, 200)

        data = json.loads(resp.data)

        self.assertDictEqual(
            data,
            {
                'extenso': 'mil e cento e doze'
            }
        )

    def test_get_number_99999(self):
        """Test the get method with 99999

        """
        resp = self.client.get('/99999')
        self.assertEqual(resp.status_code, 200)

        data = json.loads(resp.data)

        self.assertDictEqual(
            data,
            {
                'extenso': 'noventa e nove mil e novecentos e noventa e nove'
            }
        )

    def test_get_number_negative_99999(self):
        """Test the get method with -99999

        """
        resp = self.client.get('/-99999')
        self.assertEqual(resp.status_code, 200)

        data = json.loads(resp.data)

        self.assertDictEqual(
            data,
            {
                'extenso': 'menos noventa e nove mil e novecentos e noventa e nove'
            }
        )
