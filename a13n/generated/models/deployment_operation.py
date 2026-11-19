from enum import StrEnum


class DeploymentOperation(StrEnum):
    DEPLOY = "deploy"
    RETIRE = "retire"

    def __str__(self) -> str:
        return str(self.value)
