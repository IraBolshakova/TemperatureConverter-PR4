"""Абстрактный интерфейс конвертера температур."""

from abc import ABC, abstractmethod


class ITemperatureConverter(ABC):
    """Интерфейс для перевода температур между шкалами."""

    __slots__ = ()

    @abstractmethod
    def to_fahrenheit(self, celsius: float) -> float:
        """Преобразует градусы Цельсия в градусы Фаренгейта."""
        raise NotImplementedError

    @abstractmethod
    def to_kelvin(self, celsius: float) -> float:
        """Преобразует градусы Цельсия в кельвины."""
        raise NotImplementedError

    @abstractmethod
    def from_fahrenheit(self, fahrenheit: float) -> float:
        """Преобразует градусы Фаренгейта в градусы Цельсия."""
        raise NotImplementedError

    @abstractmethod
    def from_kelvin(self, kelvin: float) -> float:
        """Преобразует кельвины в градусы Цельсия."""
        raise NotImplementedError
