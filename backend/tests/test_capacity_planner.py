from backend.app.optimization.capacity_planner import (
    CapacityPlanner
)


def test_solar_capacity():

    planner = CapacityPlanner()

    result = planner.plan_capacity({
        "land_area": 100,
        "solar_score": 80,
        "wind_score": 40,
        "deployment": "Solar"
    })

    assert result["solar_capacity_mw"] == 16.0
    assert result["wind_capacity_mw"] == 0.0
    assert result["total_capacity_mw"] == 16.0


def test_wind_capacity():

    planner = CapacityPlanner()

    result = planner.plan_capacity({
        "land_area": 100,
        "solar_score": 40,
        "wind_score": 80,
        "deployment": "Wind"
    })

    assert result["solar_capacity_mw"] == 0.0
    assert result["wind_capacity_mw"] == 80.0
    assert result["total_capacity_mw"] == 80.0


def test_hybrid_capacity():

    planner = CapacityPlanner()

    result = planner.plan_capacity({
        "land_area": 100,
        "solar_score": 80,
        "wind_score": 70,
        "deployment": "Hybrid"
    })

    assert result["solar_capacity_mw"] == 16.0
    assert result["wind_capacity_mw"] == 70.0
    assert result["total_capacity_mw"] == 86.0


def test_zero_land_area():

    planner = CapacityPlanner()

    result = planner.plan_capacity({
        "land_area": 0,
        "solar_score": 90,
        "wind_score": 90,
        "deployment": "Hybrid"
    })

    assert result["total_capacity_mw"] == 0.0