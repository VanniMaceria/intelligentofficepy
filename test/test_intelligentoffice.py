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

    @patch.object(GPIO, "input")
    def test_check_third_quadrant_is_not_occupied(self, infrared: Mock):
        infrared.return_value = False
        office = IntelligentOffice()
        outcome = office.check_quadrant_occupancy(office.INFRARED_PIN3)
        self.assertFalse(outcome)

    @patch.object(GPIO, "input")
    def test_check_fourth_quadrant_is_occupied(self, infrared: Mock):
        infrared.return_value = True
        office = IntelligentOffice()
        outcome = office.check_quadrant_occupancy(office.INFRARED_PIN4)
        self.assertTrue(outcome)

    @patch.object(GPIO, "input")
    def test_check_fourth_quadrant_is_occupied(self, infrared: Mock):
        infrared.return_value = False
        office = IntelligentOffice()
        outcome = office.check_quadrant_occupancy(office.INFRARED_PIN4)
        self.assertFalse(outcome)

    @patch.object(GPIO, "input")
    def test_check_quadrant_raises_error(self, infrared: Mock):
        office = IntelligentOffice()
        self.assertRaises(IntelligentOfficeError, office.check_quadrant_occupancy, office.LED_PIN)

    @patch.object(SDL_DS3231, "read_datetime")
    @patch.object(GPIO, "output")
    def test_manage_blinds_based_on_time_blinds_opened(self, servo: Mock, clock: Mock):
        office = IntelligentOffice()
        office.blinds_open = False  #per sicurezza
        servo.return_value = 180
        clock.return_value = datetime(2025, 12, 18, 8, 00)
        office.manage_blinds_based_on_time()
        servo.assert_called_once_with(180)  #output indiretto
        self.assertTrue(office.blinds_open) #output diretto




