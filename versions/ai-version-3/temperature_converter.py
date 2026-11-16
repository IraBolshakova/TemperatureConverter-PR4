"""Реализация GigaChat (AI-v3), используемая в ветках main и ai-version-3."""

from interfaces.temperature_converter import ITemperatureConverter


class TemperatureConverter(ITemperatureConverter):
    """Конвертер температур, реализующий интерфейс ITemperatureConverter."""

    def to_fahrenheit(self, celsius: float) -> float:
        """Перевод из Цельсия в Фаренгейт: (°C × 9/5) + 32."""
        return celsius * 9.0 / 5.0 + 32.0

    def to_kelvin(self, celsius: float) -> float:
        """Перевод из Цельсия в Кельвин: °C + 273.15."""
        return celsius + 273.15

    def from_fahrenheit(self, fahrenheit: float) -> float:
        """Перевод из Фаренгейта в Цельсий: (°F − 32) × 5/9."""
        return (fahrenheit - 32.0) * 5.0 / 9.0

    def from_kelvin(self, kelvin: float) -> float:
        """Перевод из Кельвина в Цельсий: K − 273.15."""
        return kelvin - 273.15
