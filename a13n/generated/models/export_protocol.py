from enum import StrEnum


class ExportProtocol(StrEnum):
    GRPC = "grpc"
    HTTPPROTOBUF = "http/protobuf"

    def __str__(self) -> str:
        return str(self.value)
