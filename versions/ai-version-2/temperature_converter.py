"""Реализация DeepSeek (AI-v2) из практической работы №1."""

from interfaces.temperature_converter import ITemperatureConverter


class TemperatureConverter(ITemperatureConverter):
    """Реализация без состояния с __slots__ и константами класса."""

    __slots__ = ()

    _KELVIN_OFFSET: float = 273.15
    _FAHRENHEIT_MULTIPLIER: float = 9.0 / 5.0
    _FAHRENHEIT_OFFSET: float = 32.0

    def to_fahrenheit(self, celsius: float) -> float:
        return celsius * self._FAHRENHEIT_MULTIPLIER + self._FAHRENHEIT_OFFSET

    def to_kelvin(self, celsius: float) -> float:
        return celsius + self._KELVIN_OFFSET

    def from_fahrenheit(self, fahrenheit: float) -> float:
        return (fahrenheit - self._FAHRENHEIT_OFFSET) / self._FAHRENHEIT_MULTIPLIER

    def from_kelvin(self, kelvin: float) -> float:
        return kelvin - self._KELVIN_OFFSET
