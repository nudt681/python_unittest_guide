#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.Car import Car
import pytest
speed_data = {45, 50, 55, 100}


@pytest.mark.parametrize("speed_brake", speed_data)
def test_brake(speed_brake):
    car = Car(50)
    car.brake()
    assert car.speed == speed_brake


def test_step():
    assert False


def test_say_state():
    assert True


def test_average_speed():
    assert False


def test_accelerate():
    assert False