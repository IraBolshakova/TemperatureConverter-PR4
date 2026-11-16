"""Тесты «белого ящика»; активируется набор для текущей AI_VERSION."""

import inspect
import pytest

from implementations.temperature_converter import TemperatureConverter
from conftest import AI_VERSION


@pytest.mark.whitebox
@pytest.mark.skipif(AI_VERSION != "ai-version-1", reason="Тест относится только к AI-v1 (Алиса)")
def test_alice_methods_are_instance_methods():
    """БЯ-01. Проверяет, что методы не объявлены как staticmethod."""
    method = inspect.getattr_static(TemperatureConverter, "to_fahrenheit")
    assert not isinstance(method, staticmethod), (
        "AI-v1 использует @staticmethod и не соблюдает контракт методов экземпляра"
    )


@pytest.mark.whitebox
@pytest.mark.skipif(AI_VERSION != "ai-version-1", reason="Тест относится только к AI-v1 (Алиса)")
def test_alice_integer_conversion_returns_float():
    """БЯ-02. Проверяет результат деления 9/5 в Python 3."""
    assert TemperatureConverter().to_fahrenheit(1) == pytest.approx(33.8)


@pytest.mark.whitebox
@pytest.mark.skipif(AI_VERSION != "ai-version-2", reason="Тест относится только к AI-v2 (DeepSeek)")
def test_deepseek_slots_prevent_new_attributes():
    """БЯ-03. Проверяет действие __slots__ = ()."""
    converter = TemperatureConverter()
    with pytest.raises(AttributeError):
        converter.x = 1


@pytest.mark.whitebox
@pytest.mark.skipif(AI_VERSION != "ai-version-2", reason="Тест относится только к AI-v2 (DeepSeek)")
def test_deepseek_class_constant_is_accessible():
    """БЯ-04. Проверяет константу _FAHRENHEIT_MULTIPLIER."""
    assert TemperatureConverter()._FAHRENHEIT_MULTIPLIER == pytest.approx(1.8)


@pytest.mark.whitebox
@pytest.mark.skipif(AI_VERSION != "ai-version-3", reason="Тест относится только к AI-v3 (GigaChat)")
def test_gigachat_rejects_kelvin_below_absolute_zero():
    """БЯ-05. Проверяет отклонение отрицательной температуры в Кельвинах."""
    with pytest.raises(ValueError):
        TemperatureConverter().from_kelvin(-1)


@pytest.mark.whitebox
@pytest.mark.skipif(AI_VERSION != "ai-version-3", reason="Тест относится только к AI-v3 (GigaChat)")
def test_gigachat_rejects_celsius_below_absolute_zero():
    """БЯ-06. Проверяет отклонение температуры ниже абсолютного нуля."""
    with pytest.raises(ValueError):
        TemperatureConverter().to_kelvin(-300)
