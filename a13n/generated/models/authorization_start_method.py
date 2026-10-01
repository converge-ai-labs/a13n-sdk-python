from enum import StrEnum


class AuthorizationStartMethod(StrEnum):
    BROWSER_CALLBACK = "browser_callback"
    MANUAL_CALLBACK = "manual_callback"

    def __str__(self) -> str:
        return str(self.value)
