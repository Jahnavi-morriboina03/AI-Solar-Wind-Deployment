

"""
Wind Assessment Service

This module provides utility functions for:
1. Wind Classification
2. Capacity Factor Estimation
3. Overall Wind Site Assessment
"""


def calculate_wind_class(wind_speed: float) -> str:
    """
    Classify wind speed based on predefined ranges.

    Args:
        wind_speed (float): Wind speed in meters per second (m/s).

    Returns:
        str: Wind classification.
    """

    if wind_speed < 3:
        return "Poor"
    elif 3 <= wind_speed < 5:
        return "Moderate"
    elif 5 <= wind_speed < 7:
        return "Good"
    else:
        return "Excellent"


def calculate_capacity_factor(wind_speed: float) -> float:
    """
    Estimate wind turbine capacity factor based on wind speed.

    Capacity Factor Ranges:
    < 3 m/s      -> 0.10 (10%)
    3 - <5 m/s   -> 0.25 (25%)
    5 - <7 m/s   -> 0.40 (40%)
    >= 7 m/s     -> 0.55 (55%)

    Args:
        wind_speed (float): Wind speed in meters per second (m/s).

    Returns:
        float: Estimated capacity factor (0.0 to 1.0).
    """

    if wind_speed < 3:
        return 0.10
    elif wind_speed < 5:
        return 0.25
    elif wind_speed < 7:
        return 0.40
    else:
        return 0.55


def classify_wind_site(wind_speed: float) -> dict:
    """
    Assess a wind site using wind speed.

    Args:
        wind_speed (float): Wind speed in meters per second (m/s).

    Returns:
        dict: Wind assessment results.
    """

    return {
        "wind_speed": wind_speed,
        "wind_class": calculate_wind_class(wind_speed),
        "capacity_factor": calculate_capacity_factor(wind_speed)
    }