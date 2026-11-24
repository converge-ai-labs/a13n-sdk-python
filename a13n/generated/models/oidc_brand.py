from enum import StrEnum


class OIDCBrand(StrEnum):
    AUTH0 = "auth0"
    AUTHELIA = "authelia"
    AUTHENTIK = "authentik"
    CLOUDFLARE = "cloudflare"
    GENERIC = "generic"
    GITHUB = "github"
    GITLAB = "gitlab"
    GOOGLE = "google"
    KEYCLOAK = "keycloak"
    MICROSOFT = "microsoft"
    OKTA = "okta"
    ZITADEL = "zitadel"

    def __str__(self) -> str:
        return str(self.value)
