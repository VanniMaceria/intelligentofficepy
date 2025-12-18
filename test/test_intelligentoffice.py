import unittest
from datetime import datetime
from unittest.mock import patch, Mock, PropertyMock
import mock.GPIO as GPIO
from mock.SDL_DS3231 import SDL_DS3231
from mock.adafruit_veml7700 import VEML7700
from src.intelligentoffice import IntelligentOffice, IntelligentOfficeError


class TestIntelligentOffice(unittest.TestCase):

    @patch.object(GPIO, "input")
    def test_check_first_quadrant_is_occupied(self, infrared: Mock):
        infrared.return_value = True
        office = IntelligentOffice()
        outcome = office.check_quadrant_occupancy(office.INFRARED_PIN1)
        self.assertTrue(outcome)

    @patch.object(GPIO, "input")
    def test_check_first_quadrant_is_not_occupied(self, infrared: Mock):
        infrared.return_value = False
        office = IntelligentOffice()
        outcome = office.check_quadrant_occupancy(office.INFRARED_PIN1)
        self.assertFalse(outcome)

    @patch.object(GPIO, "input")
    def test_check_second_quadrant_is_occupied(self, infrared: Mock):
        infrared.return_value = True
        office = IntelligentOffice()
        outcome = office.check_quadrant_occupancy(office.INFRARED_PIN2)
        self.assertTrue(outcome)

    @patch.object(GPIO, "input")
    def test_check_second_quadrant_is_not_occupied(self, infrared: Mock):
        infrared.return_value = False
        office = IntelligentOffice()
        outcome = office.check_quadrant_occupancy(office.INFRARED_PIN2)
        self.assertFalse(outcome)

    @patch.object(GPIO, "input")
    def test_check_third_quadrant_is_occupied(self, infrared: Mock):
        infrared.return_value = True
        office = IntelligentOffice()
        outcome = office.check_quadrant_occupancy(office.INFRARED_PIN3)
        self.assertTrue(outcome)




