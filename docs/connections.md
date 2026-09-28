# Connections and authentication

Most server applications should use a workspace API key. Cookie sessions are for applications that already implement a Service login flow. Choose one explicitly; the SDK does not discover a workspace or borrow credentials from your browser.

## Connect with a workspace API key

Keep one Client open for related work and close it when the application scope ends:

```python
import asyncio
import os

from a13n import Client


async def main() -> None:
    async with Client(
        os.environ["A13N_SERVICE_URL"],
        os.environ["A13N_API_TOKEN"],
        timeout=30,
    ) as client:
        page = await client.resources.agents.list(limit=10)
        for agent in page.value.items:
            print(agent.id, agent.name)


if __name__ == "__main__":
    asyncio.run(main())
```

Run this with the same environment as the [quick start](../README.md#quick-start). It prints up to ten visible Agents; an empty list is valid and is not an authentication error.

Use the **Service** base URL, not the Console URL, and do not append `/api/v1`. A deployment may have a base-path prefix; keep the prefix supplied by your administrator. The key determines its workspace, so this mode does not require workspace discovery or a workspace header. It also does not send or retain session cookies.

Store the key in your application's secret configuration. Do not include it in source code, example URLs, browser bundles, or diagnostic logs.

## Use a private certificate authority

For a Service signed by your organization's CA, provide the CA bundle rather than disabling verification:

```python
from a13n import Client


async def check_private_service(service_url: str, api_key: str, ca_file: str) -> None:
    async with Client(service_url, api_key, ca_bundle=ca_file) as client:
        response = await client.resources.agents.list(limit=1)
        print("Connected; request ID:", response.request_id)
```

The SDK uses explicit connection configuration and does not take proxy or CA settings from ambient HTTP environment variables. A certificate failure is a connection-configuration problem; changing the API key will not fix it. Confirm the hostname, certificate chain, and correct CA file with your administrator.

## Use an existing login session

Session mode requires cookies from your login flow, its origin, the current CSRF token for writes, and an explicit workspace ID for workspace operations:

```python
import httpx2

from a13n import Client


async def list_session_agents(
    service_url: str,
    console_origin: str,
    cookies: httpx2.Cookies,
    csrf_token: str,
    workspace_id: str,
) -> None:
    async with Client.session(
        service_url,
        origin=console_origin,
        cookies=cookies,
        csrf_token=csrf_token,
        workspace_id=workspace_id,
    ) as client:
        async for agent in client.resources.agents.iter(limit=20):
            print(agent.id, agent.name)
```

This function does not log in. Pass a cookie jar obtained through your application's supported login flow, not a fabricated cookie name. Session mode keeps a private copy of the supplied jar; it does not mutate your caller-owned jar. The SDK does not refresh expired login credentials automatically.

When your login flow returns a replacement CSRF token, update the open session Client with `client.set_csrf_token(new_token)`. This method is not available as an authentication shortcut on API-key Clients.

### Workspace selection is deliberate

`workspace_id` is a default for workspace-scoped routes. The Client does not send that header to public or organization/admin routes. An operation's explicit `x_workspace_id` takes precedence when your session is authorized to access another workspace:

```python
from a13n import Client


async def list_in_workspace(session_client: Client, workspace_id: str) -> None:
    page = await session_client.resources.agents.list(x_workspace_id=workspace_id, limit=20)
    for agent in page.value.items:
        print(agent.id, agent.name)
```

Use this override on a session Client. It does not turn an API key into a credential for a different workspace. Organization and administration resources still require their explicit owner IDs and the appropriate permissions; selecting a workspace is not an elevation of authority.

## Client lifetime and request limits

`async with Client(...)` closes owned connections and streams on exit. In a long-running async service, create the Client in application startup/lifespan and call `await client.aclose()` during shutdown. Do not create one Client for every streamed frame, and do not close it while another part of your application still needs it.

`timeout` controls an ordinary HTTP request. [Interaction observation](streaming-and-results.md#bound-how-long-you-wait) has a separate overall budget that includes queue time and execution. A request timeout or task cancellation says nothing by itself about whether a previously submitted write was accepted.

`Client(service_url)` with no token is an intentionally public, cookieless Client. A protected endpoint will reject it; there is no automatic fallback to local credentials.

## Diagnose a connection problem

| Symptom                             | First check                                                                             |
| ----------------------------------- | --------------------------------------------------------------------------------------- |
| Invalid base URL before any request | Remove credentials, query strings, fragments, and the API suffix from configuration.    |
| TLS or connection failure           | Verify the Service address, reachable network, hostname, and CA configuration.          |
| `401`                               | Check whether the key or login session is valid and unexpired.                          |
| `403`                               | Check the principal's permissions; for session writes also check origin and CSRF proof. |
| Agent missing from a list           | Check the selected workspace and visibility before assuming it was deleted.             |

Keep request IDs when reporting Service rejections. See [errors and recovery](errors-and-recovery.md) for exception categories and safe retry decisions.

[Back to the guide](README.md) · [Next: resource API](resources.md)
