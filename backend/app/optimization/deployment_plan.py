from typing import Dict


class DeploymentPlanGenerator:
    """
    Generates a complete deployment plan by combining
    deployment strategy, capacity planning, and
    expansion feasibility results.
    """

    def generate_plan(
        self,
        deployment_result: Dict,
        capacity_result: Dict,
        expansion_result: Dict
    ) -> Dict:

        technology = deployment_result.get(
            "deployment",
            "Not Recommended"
        )

        total_capacity = capacity_result.get(
            "total_capacity_mw",
            0.0
        )

        expansion_status = expansion_result.get(
            "expansion_status",
            "Not Expandable"
        )

        remarks = self._generate_remarks(
            technology,
            total_capacity,
            expansion_status
        )

        return {
            "recommended_technology": technology,
            "recommended_capacity_mw": total_capacity,
            "expansion_status": expansion_status,
            "optimization_remarks": remarks
        }

    def _generate_remarks(
        self,
        technology: str,
        capacity: float,
        expansion_status: str
    ) -> str:

        if technology == "Hybrid":
            technology_remark = (
                "Hybrid deployment is recommended "
                "to utilize both solar and wind resources."
            )

        elif technology == "Solar":
            technology_remark = (
                "Solar deployment is recommended "
                "based on the available solar resource."
            )

        elif technology == "Wind":
            technology_remark = (
                "Wind deployment is recommended "
                "based on the available wind resource."
            )

        else:
            technology_remark = (
                "The site is not currently suitable "
                "for renewable energy deployment."
            )

        capacity_remark = (
            f" Recommended capacity is "
            f"{capacity} MW."
        )

        expansion_remark = (
            f" Future expansion status: "
            f"{expansion_status}."
        )

        return (
            technology_remark
            + capacity_remark
            + expansion_remark
        )