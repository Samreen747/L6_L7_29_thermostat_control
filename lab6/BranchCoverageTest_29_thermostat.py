
from thermostat_control import (
    target_temperature,
    hvac_action,
    energy_alert,
)


# =====================================
# 1. TARGET TEMPERATURE BRANCH TESTS
# =====================================

def test_away_mode():
    assert target_temperature("away", True, 12) == 16


def test_sleep_before_6():
    assert target_temperature("sleep", True, 5) == 18


def test_sleep_after_22():
    assert target_temperature("sleep", True, 22) == 18


def test_sleep_during_day():
    assert target_temperature("sleep", True, 12) == 20


def test_unoccupied():
    assert target_temperature("home", False, 12) == 18


def test_occupied_morning():
    assert target_temperature("home", True, 7) == 22


def test_occupied_not_morning():
    assert target_temperature("home", True, 10) == 20


def test_occupied_evening():
    assert target_temperature("home", True, 18) == 21


def test_occupied_not_evening():
    assert target_temperature("home", True, 22) == 20


# =====================================
# 2. HVAC ACTION BRANCH TESTS
# =====================================

def test_hvac_idle():
    assert hvac_action(20, 20.5, 10) == "idle"


def test_hvac_not_idle():
    assert hvac_action(18, 22, 10) == "heat"


def test_hvac_heat_boost():
    assert hvac_action(18, 22, 2) == "heat_boost"


def test_hvac_heat_normal():
    assert hvac_action(18, 22, 5) == "heat"


def test_hvac_cool_boost():
    assert hvac_action(25, 20, 35) == "cool_boost"


def test_hvac_cool_normal():
    assert hvac_action(25, 20, 30) == "cool"


# =====================================
# 3. ENERGY ALERT BRANCH TESTS
# =====================================

def test_energy_empty_readings():
    assert energy_alert([], 10) == "ok"


def test_energy_no_reading_over_limit():
    assert energy_alert([5, 8, 10], 10) == "ok"


def test_energy_reading_over_limit():
    assert energy_alert([15], 10) == "critical"


def test_energy_critical():
    assert energy_alert([15, 16, 5], 10) == "critical"


def test_energy_warning():
    assert energy_alert([15, 5], 10) == "warning"


def test_energy_warning_multiple():
    assert energy_alert([15, 5, 6, 7], 10) == "warning"
