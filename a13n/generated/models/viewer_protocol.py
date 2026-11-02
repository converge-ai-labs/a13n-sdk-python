from enum import StrEnum


class ViewerProtocol(StrEnum):
    IFRAME = "iframe"
    VNC = "vnc"

    def __str__(self) -> str:
        return str(self.value)
