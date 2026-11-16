"""Общие тесты «чёрного ящика» для всех трёх версий TemperatureConverter."""

import pytest

from interfaces.temperature_converter import ITemperatureConverter


@pytest.mark.blackbox
def test_implements_interface(converter):
    """ЧЯ-01. Класс создаётся и реализует интерфейс."""
    assert isinstance(converter, ITemperatureConverter)


@pytest.mark.blackbox
@pytest.mark.parametrize("celsius, expected", [
    (0, 32.0),
    (100, 212.0),
    (-40, -40.0),
])
def test_to_fahrenheit(converter, celsius, expected):
    """ЧЯ-02/03/04. Проверка перевода из Цельсия в Фаренгейт."""
    assert converter.to_fahrenheit(celsius) == pytest.approx(expected)


@pytest.mark.blackbox
@pytest.mark.parametrize("celsius, expected", [
    (0, 273.15),
    (-273.15, 0.0),
])
def test_to_kelvin(converter, celsius, expected):
    """ЧЯ-05/06. Проверка перевода из Цельсия в Кельвин."""
    assert converter.to_kelvin(celsius) == pytest.approx(expected, abs=1e-9)


@pytest.mark.blackbox
@pytest.mark.parametrize("fahrenheit, expected", [
    (32, 0.0),
    (212, 100.0),
])
def test_from_fahrenheit(converter, fahrenheit, expected):
    """ЧЯ-07/08. Проверка перевода из Фаренгейта в Цельсий."""
    assert converter.from_fahrenheit(fahrenheit) == pytest.approx(expected)


@pytest.mark.blackbox
@pytest.mark.parametrize("kelvin, expected", [
    (273.15, 0.0),
    (0, -273.15),
])
def test_from_kelvin(converter, kelvin, expected):
    """ЧЯ-09/10. Проверка перевода из Кельвина в Цельсий."""
    assert converter.from_kelvin(kelvin) == pytest.approx(expected, abs=1e-9)


@pytest.mark.blackbox
def test_roundtrip_celsius_fahrenheit(converter):
    """ЧЯ-11. Проверка обратимости преобразования C → F → C."""
    original = 36.6
    result = converter.from_fahrenheit(converter.to_fahrenheit(original))
    assert result == pytest.approx(original, abs=1e-9)


@pytest.mark.blackbox
def test_roundtrip_celsius_kelvin(converter):
    """ЧЯ-12. Проверка обратимости преобразования C → K → C."""
    original = 100.0
    result = converter.from_kelvin(converter.to_kelvin(original))
    assert result == pytest.approx(original, abs=1e-9)


@pytest.mark.blackbox
def test_large_number(converter):
    """ЧЯ-13. Проверка обработки большого числа."""
    result = converter.to_fahrenheit(1e10)
    assert isinstance(result, float)
    assert result == pytest.approx(1e10 * 9 / 5 + 32, rel=1e-9)


@pytest.mark.blackbox
@pytest.mark.parametrize("method", [
    "to_fahrenheit", "to_kelvin", "from_fahrenheit", "from_kelvin"
])
@pytest.mark.parametrize("value", ["100", None])
def test_non_numeric_input(converter, method, value):
    """ЧЯ-14/15. Все методы отклоняют строку и None исключением."""
    with pytest.raises((TypeError, ValueError)):
        getattr(converter, method)(value)
