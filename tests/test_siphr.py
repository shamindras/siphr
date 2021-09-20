"""Tests for `siphr` module."""
from typing import Generator

import pytest

import siphr


@pytest.fixture
def version() -> Generator[str, None, None]:
    """Sample pytest fixture."""
    yield siphr.__version__


def test_version(version: str) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    assert version == "0.1.0"
