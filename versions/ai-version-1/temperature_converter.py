"""Реализация Алисы (AI-v1) из практической работы №1."""

from interfaces.temperature_converter import ITemperatureConverter


class TemperatureConverter(ITemperatureConverter):
    @staticmethod
    def to_fahrenheit(celsius: float) -> float:
        return celsius * 9 / 5 + 32

    @staticmethod
    def to_kelvin(celsius: float) -> float:
        return celsius + 273.15

    @staticmethod
    def from_fahrenheit(fahrenheit: float) -> float:
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def from_kelvin(kelvin: float) -> float:
        return kelvin - 273.15
