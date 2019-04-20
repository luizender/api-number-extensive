"""The number resource that is responsible for convert number to
number in extensive

"""

import logging
from flask_restful import Resource, abort
from api.defines import (
    MAX_NUMBER_SUPPORT,
    MIN_NUMBER_SUPPORT,
    NUMBER_EXTENSIVE,
    UNIT_EXTENSIVE
)

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
            return True, None
        except BaseException as error:  # pylint: disable=broad-except
            LOGGER.debug('Received a invalid number: %s', str(error))
            return False, 'Need to inform a number between %s and %s to convert' % (
                MAX_NUMBER_SUPPORT, MIN_NUMBER_SUPPORT
            )

    @staticmethod
    def _padding_number(number):
        """Complete the number with zeros (0) if need

        :param number: The number to complete
        :type number: str
        :return: The number that was padded with zeros
        :rtype: str
        """
        pad = 3 - (len(number) % 3)
        if pad < 3:
            LOGGER.debug('Padding the number with %s zeros', pad)
            return ('0' * pad) + number
        LOGGER.debug('No need to pad the number')
        return number

    def _split_number(self, number):
        """Split the number in a list with numbers with three chars

        :param number: The number to split
        :type number: str
        :return: The list of numbers with three chars
        :rtype: list
        """
        number_padded = self._padding_number(number)
        LOGGER.debug('Splitting the number %s', number_padded)
        return [
            number_padded[i:i+3] for i in range(0, len(number_padded), 3)
        ]

    @staticmethod
    def _get_number_extensive(number):
        """Get the number in extensive form

        :param number: The number to get the extensive form
        :type number: str
        :return: The number in extensive
        :rtype: str
        """
        if int(number) == 0:
            return 'zero'
        if int(number) == 100:
            return 'cem'

        extensive = []
        hundred, ten, unit = number

        if int(hundred) > 0:
            extensive.append(NUMBER_EXTENSIVE[3][int(hundred)])

        if int(ten) == 1:
            extensive.append(NUMBER_EXTENSIVE[1][int(unit)])
            return ' e '.join(extensive)

        if int(ten) > 0:
            extensive.append(NUMBER_EXTENSIVE[2][int(ten)])

        if int(unit) > 0:
            extensive.append(NUMBER_EXTENSIVE[0][int(unit)])

        return ' e '.join(extensive)

    @staticmethod
    def _get_unit_extensive(number_extensive, unit):
        """Get the number in extensive with the unit in extensive

        :param number_extensive: The number in extensive
        :type number_extensive: str
        :param unit: The unit to get
        :type unit: int
        :return: The number in extensive with the unit in extensive
        :rtype: str
        """
        if not unit:
            return None

        if number_extensive == 'um':
            return UNIT_EXTENSIVE[unit]

        return '%s %s' % (number_extensive, UNIT_EXTENSIVE[unit])

    def _convert_number(self, number):
        """Convert the number to number in extensive

        :param number: The number to convert
        :type number: str
        :return: The number in extensive
        :rtype: str
        """
        LOGGER.debug('Convert the number %s to number in extensive', number)

        negative = None
        if int(number) < 0:
            number = number[1:]
            negative = 'menos'

        complete_number = ''
        number_splitted = self._split_number(number)
        number_splitted.reverse()

        for cur_number in number_splitted:
            number_extensive = self._get_number_extensive(cur_number)
            LOGGER.debug(
                'Number %s in extensive is %s', cur_number, number_extensive
            )

            number_with_unit = self._get_unit_extensive(
                number_extensive, number_splitted.index(cur_number)
            )
            if number_with_unit:
                number_extensive = number_with_unit

            if not complete_number or complete_number == 'zero':
                complete_number = number_extensive
                continue

            complete_number = '%s e %s' % (number_extensive, complete_number)

        LOGGER.debug(
            'The number %s was convert to %s', number, complete_number
        )

        if negative:
            return '%s %s' % (negative, complete_number)

        return complete_number

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
            'extenso': self._convert_number(number)
        }
