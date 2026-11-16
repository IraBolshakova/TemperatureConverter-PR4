"""Общие фикстуры для тестирования текущей реализации в выбранной ветке."""

import os
import pytest

from implementations.temperature_converter import TemperatureConverter


AI_VERSION = os.getenv("AI_VERSION", "ai-version-3")


@pytest.fixture
def converter():
    """Создаёт новый экземпляр конвертера для каждого теста."""
    return TemperatureConverter()
