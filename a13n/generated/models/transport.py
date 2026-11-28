from enum import StrEnum


class Transport(StrEnum):
    WEBRTC = "webrtc"
    WEBSOCKET = "websocket"

    def __str__(self) -> str:
        return str(self.value)
