from backend.app.optimization.expansion_analyzer import (
    ExpansionAnalyzer
)


def test_expandable_site():

    analyzer = ExpansionAnalyzer()

    result = analyzer.analyze({
        "maximum_capacity_mw": 100,
        "current_capacity_mw": 60
    })

    assert result["expansion_status"] == (
        "Expandable"
    )

    assert result["remaining_capacity_mw"] == 40


def test_limited_expansion_site():

    analyzer = ExpansionAnalyzer()

    result = analyzer.analyze({
        "maximum_capacity_mw": 100,
        "current_capacity_mw": 80
    })

    assert result["expansion_status"] == (
        "Limited Expansion"
    )

    assert result["remaining_capacity_mw"] == 20


def test_not_expandable_site():

    analyzer = ExpansionAnalyzer()

    result = analyzer.analyze({
        "maximum_capacity_mw": 100,
        "current_capacity_mw": 95
    })

    assert result["expansion_status"] == (
        "Not Expandable"
    )


def test_fully_utilized_site():

    analyzer = ExpansionAnalyzer()

    result = analyzer.analyze({
        "maximum_capacity_mw": 100,
        "current_capacity_mw": 100
    })

    assert result["expansion_status"] == (
        "Not Expandable"
    )


def test_invalid_maximum_capacity():

    analyzer = ExpansionAnalyzer()

    result = analyzer.analyze({
        "maximum_capacity_mw": 0,
        "current_capacity_mw": 50
    })

    assert result["expansion_status"] == (
        "Not Expandable"
    )