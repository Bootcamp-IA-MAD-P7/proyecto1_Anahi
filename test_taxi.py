import pytest
from taxi import Taxi, RATE_MOVING, RATE_STOPPED


@pytest.fixture
def taxi():
    return Taxi()

def test_initial_fare_is_zero(taxi):
    assert taxi.fare == 0.00

def test_initial_journey_inactive(taxi):
    assert taxi.journey_active is False

def test_initial_not_moving(taxi):
    assert taxi.moving is False

def test_start_activates_journey(taxi):
    taxi.start_journey()
    assert taxi.journey_active is True

def test_start_sets_moving(taxi):
    taxi.start_journey()
    assert taxi.moving is True

def test_start_resets_fare(taxi):
    taxi.fare = 9.99
    taxi.start_journey()
    assert taxi.fare == 0.00

def test_taximeter_moving(taxi):
    taxi.start_journey()
    taxi.taximeter()
    assert taxi.fare == pytest.approx(RATE_MOVING)

def test_taximeter_stopped(taxi):
    taxi.start_journey()
    taxi.set_stopped()
    taxi.taximeter()
    assert taxi.fare == pytest.approx(RATE_STOPPED)

def test_taximeter_accumulates(taxi):
    taxi.start_journey()
    taxi.taximeter()   # moving
    taxi.taximeter()   # moving
    taxi.set_stopped()
    taxi.taximeter()   # stopped
    assert taxi.fare == pytest.approx(2 * RATE_MOVING + RATE_STOPPED)

def test_set_stopped(taxi):
    taxi.start_journey()
    taxi.set_stopped()
    assert taxi.moving is False

def test_set_moving_after_stop(taxi):
    taxi.start_journey()
    taxi.set_stopped()
    taxi.set_moving()
    assert taxi.moving is True

def test_end_returns_fare(taxi):
    taxi.start_journey()
    taxi.taximeter()
    taxi.taximeter()
    result = taxi.end_journey()
    assert result == pytest.approx(2 * RATE_MOVING)

def test_end_deactivates_journey(taxi):
    taxi.start_journey()
    taxi.end_journey()
    assert taxi.journey_active is False