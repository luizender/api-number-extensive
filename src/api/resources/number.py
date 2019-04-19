"""The number resource that is responsible for convert number to
number in extensive

"""

import logging
from flask_restful import Resource, abort
from api.settings import MAX_NUMBER_SUPPORT, MIN_NUMBER_SUPPORT

LOGGER = logging.getLogger(__name__)


class NumberResource(Resource):
    """Responsible for convert number to number in extensive

    """

    @staticmethod
    def _valid_number(number):
        """Validate the received number and send a response 400 (Bad Request)
        in case of invalid number

        :param number: The number to validate
        :type number: str
        :return: Return True or False and the message to send to the client
        :rtype: tuple
        """
        try:
            number_int = int(number)
            if number_int < MIN_NUMBER_SUPPORT or number_int > MAX_NUMBER_SUPPORT:
                LOGGER.debug('Number %s outside of range accepted', number)
                return False, 'Number need to be a value between %s and %s' % (
                    MAX_NUMBER_SUPPORT, MIN_NUMBER_SUPPORT
                )
            return True
        except BaseException as error:
            LOGGER.debug('Received a invalid number: %s', str(error))
            return False, 'Need to inform a number between %s and %s to convert' % (
                MAX_NUMBER_SUPPORT, MIN_NUMBER_SUPPORT
            )

    def get(self, number=None):
        """Convert the number to number in extensive format

        :param number: The number to convert
        :type number: str
        """
        LOGGER.debug('Validating the number received')
        valid, message = self._valid_number(number)
        if not valid and message:
            abort(400, message=message)

        return {
            'extenso': 'Not implemented yet'
        }
