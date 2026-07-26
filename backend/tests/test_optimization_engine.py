from backend.app.optimization.deployment_optimizer import (
    DeploymentOptimizer
)

from backend.app.optimization.capacity_planner import (
    CapacityPlanner
)

from backend.app.optimization.expansion_analyzer import (
    ExpansionAnalyzer
)

from backend.app.optimization.deployment_plan import (
    DeploymentPlanGenerator
)


def generate_deployment_plan(site):

    deployment_optimizer = DeploymentOptimizer()
    capacity_planner = CapacityPlanner()
    expansion_analyzer = ExpansionAnalyzer()
    plan_generator = DeploymentPlanGenerator()

    # Step 1: Select deployment technology
    deployment_result = deployment_optimizer.optimize({
        "solar_score": site["solar_score"],
        "wind_score": site["wind_score"]
    })

    # Step 2: Calculate recommended capacity
    capacity_result = capacity_planner.plan_capacity({
        "land_area": site["land_area"],
        "solar_score": site["solar_score"],
        "wind_score": site["wind_score"],
        "deployment": deployment_result["deployment"]
    })

    # Step 3: Analyze expansion feasibility
    expansion_result = expansion_analyzer.analyze({
        "available_land_area": site[
            "available_land_area"
        ],

        "required_land_area": site[
            "required_land_area"
        ],

        "available_budget": site[
            "available_budget"
        ],

        "expansion_cost": site[
            "expansion_cost"
        ],

        "environmental_restriction": site[
            "environmental_restriction"
        ],

        "available_grid_capacity": site[
            "available_grid_capacity"
        ],

        "infrastructure_score": site[
            "infrastructure_score"
        ]
    })

    # Step 4: Generate final deployment plan
    return plan_generator.generate_plan(
        deployment_result,
        capacity_result,
        expansion_result
    )


def test_multiple_sites_produce_different_plans():

    solar_site = {
        "solar_score": 90,
        "wind_score": 40,
        "land_area": 100,

        "available_land_area": 200,
        "required_land_area": 100,

        "available_budget": 10000000,
        "expansion_cost": 5000000,

        "environmental_restriction": False,
        "available_grid_capacity": 100,
        "infrastructure_score": 80
    }

    wind_site = {
        "solar_score": 40,
        "wind_score": 90,
        "land_area": 100,

        "available_land_area": 200,
        "required_land_area": 100,

        "available_budget": 10000000,
        "expansion_cost": 5000000,

        "environmental_restriction": False,
        "available_grid_capacity": 100,
        "infrastructure_score": 80
    }

    hybrid_site = {
        "solar_score": 90,
        "wind_score": 90,
        "land_area": 100,

        "available_land_area": 200,
        "required_land_area": 100,

        "available_budget": 10000000,
        "expansion_cost": 5000000,

        "environmental_restriction": False,
        "available_grid_capacity": 100,
        "infrastructure_score": 80
    }

    solar_plan = generate_deployment_plan(
        solar_site
    )

    wind_plan = generate_deployment_plan(
        wind_site
    )

    hybrid_plan = generate_deployment_plan(
        hybrid_site
    )
    print("\nSolar Plan:")
    print(solar_plan)

    print("\nWind Plan:")
    print(wind_plan)

    print("\nHybrid Plan:")
    print(hybrid_plan)

    assert (
        solar_plan["recommended_technology"]
        == "Solar"
    )

    assert (
        wind_plan["recommended_technology"]
        == "Wind"
    )

    assert (
        hybrid_plan["recommended_technology"]
        == "Hybrid"
    )

    assert (
        solar_plan["recommended_technology"]
        != wind_plan["recommended_technology"]
    )

    assert (
        wind_plan["recommended_technology"]
        != hybrid_plan["recommended_technology"]
    )


def test_different_land_area_changes_capacity():

    large_site = generate_deployment_plan({
        "solar_score": 90,
        "wind_score": 40,
        "land_area": 100,

        "available_land_area": 200,
        "required_land_area": 100,

        "available_budget": 10000000,
        "expansion_cost": 5000000,

        "environmental_restriction": False,
        "available_grid_capacity": 100,
        "infrastructure_score": 80
    })

    small_site = generate_deployment_plan({
        "solar_score": 90,
        "wind_score": 40,
        "land_area": 50,

        "available_land_area": 100,
        "required_land_area": 80,

        "available_budget": 10000000,
        "expansion_cost": 5000000,

        "environmental_restriction": False,
        "available_grid_capacity": 100,
        "infrastructure_score": 80
    })

    assert (
        large_site["recommended_capacity_mw"]
        > small_site["recommended_capacity_mw"]
    )


def test_constraints_affect_expansion_status():

    expandable_site = generate_deployment_plan({
        "solar_score": 90,
        "wind_score": 40,
        "land_area": 100,

        "available_land_area": 200,
        "required_land_area": 100,

        "available_budget": 10000000,
        "expansion_cost": 5000000,

        "environmental_restriction": False,
        "available_grid_capacity": 100,
        "infrastructure_score": 80
    })

    restricted_site = generate_deployment_plan({
        "solar_score": 90,
        "wind_score": 40,
        "land_area": 100,

        "available_land_area": 100,
        "required_land_area": 80,

        "available_budget": 5000000,
        "expansion_cost": 10000000,

        "environmental_restriction": True,
        "available_grid_capacity": 5,
        "infrastructure_score": 30
    })

    assert (
        expandable_site["expansion_status"]
        == "Expandable"
    )

    assert (
        restricted_site["expansion_status"]
        == "Not Expandable"
    )