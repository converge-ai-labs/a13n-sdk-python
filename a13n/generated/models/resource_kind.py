from enum import StrEnum


class ResourceKind(StrEnum):
    CONFIGMAP = "ConfigMap"
    NETWORKPOLICY = "NetworkPolicy"
    PERSISTENTVOLUMECLAIM = "PersistentVolumeClaim"
    POD = "Pod"
    SECRET = "Secret"

    def __str__(self) -> str:
        return str(self.value)
