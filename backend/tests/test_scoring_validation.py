from backend.app.evaluation.category_scoring import (
    calculate_renewable_resource_score,
    calculate_terrain_score,
    calculate_infrastructure_score
)

from backend.app.evaluation.ranking import (
    rank_candidate_sites
)


def test_higher_renewable_resources_increase_overall_score():
    """
    Higher solar irradiance and wind speed
    should increase the renewable resource score.
    """

    low_resource_score = calculate_renewable_resource_score(
        solar_irradiance=3,
        wind_speed=3
    )

    high_resource_score = calculate_renewable_resource_score(
        solar_irradiance=7,
        wind_speed=10
    )

    print("\nVALIDATION 1: RENEWABLE RESOURCES")
    print("=================================")
    print(f"Low resource score: {low_resource_score}")
    print(f"High resource score: {high_resource_score}")

    assert high_resource_score > low_resource_score


def test_poor_terrain_reduces_score():
    """
    Higher slope should reduce the terrain score.
    """

    good_terrain_score = calculate_terrain_score(
        slope=2,
        elevation=500
    )

    poor_terrain_score = calculate_terrain_score(
        slope=25,
        elevation=500
    )

    print("\nVALIDATION 2: TERRAIN")
    print("=====================")
    print(f"Good terrain score: {good_terrain_score}")
    print(f"Poor terrain score: {poor_terrain_score}")

    assert good_terrain_score > poor_terrain_score


def test_poor_infrastructure_reduces_score():
    """
    Greater distance from roads and grid
    should reduce the infrastructure score.
    """

    good_infrastructure_score = calculate_infrastructure_score(
        distance_to_road=2,
        distance_to_grid=5
    )

    poor_infrastructure_score = calculate_infrastructure_score(
        distance_to_road=40,
        distance_to_grid=90
    )

    print("\nVALIDATION 3: INFRASTRUCTURE")
    print("============================")
    print(
        f"Good infrastructure score: "
        f"{good_infrastructure_score}"
    )
    print(
        f"Poor infrastructure score: "
        f"{poor_infrastructure_score}"
    )

    assert good_infrastructure_score > poor_infrastructure_score


def test_ranking_changes_when_site_parameters_change():
    """
    When site parameters change and a site becomes better,
    its ranking should also improve.
    """

    site_a_score = calculate_renewable_resource_score(
        solar_irradiance=7,
        wind_speed=10
    )

    site_b_score = calculate_renewable_resource_score(
        solar_irradiance=4,
        wind_speed=4
    )

    sites = [
        {
            "site_id": "SITE-A",
            "overall_score": site_a_score
        },
        {
            "site_id": "SITE-B",
            "overall_score": site_b_score
        }
    ]

    ranked_sites = rank_candidate_sites(sites)

    print("\nVALIDATION 4: INITIAL RANKING")
    print("============================")
    print(
        f"Rank 1: {ranked_sites[0]['site_id']}"
    )

    assert ranked_sites[0]["site_id"] == "SITE-A"

    # Improve SITE-B
    site_b_score = calculate_renewable_resource_score(
        solar_irradiance=8,
        wind_speed=12
    )

    updated_sites = [
        {
            "site_id": "SITE-A",
            "overall_score": site_a_score
        },
        {
            "site_id": "SITE-B",
            "overall_score": site_b_score
        }
    ]

    updated_ranking = rank_candidate_sites(
        updated_sites
    )

    print("\nVALIDATION 4: UPDATED RANKING")
    print("=============================")
    print(
        f"Rank 1: {updated_ranking[0]['site_id']}"
    )

    assert updated_ranking[0]["site_id"] == "SITE-B"


def test_scoring_is_consistent():
    """
    The same input should always produce
    the same scoring result.
    """

    input_data = {
        "solar_irradiance": 5.8,
        "wind_speed": 6.2,
        "slope": 2.1,
        "elevation": 540,
        "distance_to_road": 5,
        "distance_to_grid": 10
    }

    result_1 = (
        calculate_renewable_resource_score(
            input_data["solar_irradiance"],
            input_data["wind_speed"]
        ),
        calculate_terrain_score(
            input_data["slope"],
            input_data["elevation"]
        ),
        calculate_infrastructure_score(
            input_data["distance_to_road"],
            input_data["distance_to_grid"]
        )
    )

    result_2 = (
        calculate_renewable_resource_score(
            input_data["solar_irradiance"],
            input_data["wind_speed"]
        ),
        calculate_terrain_score(
            input_data["slope"],
            input_data["elevation"]
        ),
        calculate_infrastructure_score(
            input_data["distance_to_road"],
            input_data["distance_to_grid"]
        )
    )

    print("\nVALIDATION 5: CONSISTENCY")
    print("=========================")
    print(f"First result:  {result_1}")
    print(f"Second result: {result_2}")

    assert result_1 == result_2