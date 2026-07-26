from backend.app.optimization.deployment_optimizer import (
    DeploymentOptimizer
)


def test_solar_deployment():
    optimizer = DeploymentOptimizer()

    result = optimizer.optimize({
        "solar_score": 90,
        "wind_score": 40
    })

    assert result["deployment"] == "Solar"


def test_wind_deployment():
    optimizer = DeploymentOptimizer()

    result = optimizer.optimize({
        "solar_score": 40,
        "wind_score": 90
    })

    assert result["deployment"] == "Wind"


def test_hybrid_deployment():
    optimizer = DeploymentOptimizer()

    result = optimizer.optimize({
        "solar_score": 90,
        "wind_score": 90
    })

    assert result["deployment"] == "Hybrid"


def test_not_recommended():
    optimizer = DeploymentOptimizer()

    result = optimizer.optimize({
        "solar_score": 40,
        "wind_score": 40
    })

    assert result["deployment"] == "Not Recommended"