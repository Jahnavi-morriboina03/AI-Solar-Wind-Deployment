from backend.app.optimization.deployment_plan import (
    DeploymentPlanGenerator
)


def test_generate_hybrid_deployment_plan():

    generator = DeploymentPlanGenerator()

    deployment_result = {
        "deployment": "Hybrid"
    }

    capacity_result = {
        "total_capacity_mw": 86.0
    }

    expansion_result = {
        "expansion_status": "Expandable"
    }

    result = generator.generate_plan(
        deployment_result,
        capacity_result,
        expansion_result
    )

    assert result["recommended_technology"] == (
        "Hybrid"
    )

    assert result["recommended_capacity_mw"] == 86.0

    assert result["expansion_status"] == (
        "Expandable"
    )

    assert "Hybrid deployment" in (
        result["optimization_remarks"]
    )


def test_generate_solar_deployment_plan():

    generator = DeploymentPlanGenerator()

    result = generator.generate_plan(
        {
            "deployment": "Solar"
        },
        {
            "total_capacity_mw": 20.0
        },
        {
            "expansion_status": "Limited Expansion"
        }
    )

    assert result["recommended_technology"] == (
        "Solar"
    )

    assert result["recommended_capacity_mw"] == 20.0

    assert result["expansion_status"] == (
        "Limited Expansion"
    )


def test_generate_wind_deployment_plan():

    generator = DeploymentPlanGenerator()

    result = generator.generate_plan(
        {
            "deployment": "Wind"
        },
        {
            "total_capacity_mw": 50.0
        },
        {
            "expansion_status": "Not Expandable"
        }
    )

    assert result["recommended_technology"] == (
        "Wind"
    )

    assert result["recommended_capacity_mw"] == 50.0

    assert result["expansion_status"] == (
        "Not Expandable"
    )