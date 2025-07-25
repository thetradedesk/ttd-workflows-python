"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from ._version import (
    __gen_version__,
    __openapi_doc_version__,
    __user_agent__,
    __version__,
)
from .httpclient import AsyncHttpClient, HttpClient
from .utils import Logger, RetryConfig, remove_suffix
from dataclasses import dataclass
from pydantic import Field
from ttd_workflows import models
from ttd_workflows.types import OptionalNullable, UNSET
from typing import Callable, Dict, Optional, Tuple, Union


SERVER_PROD = "prod"
r"""The production environment."""
SERVER_SANDBOX = "sandbox"
r"""The sandbox environment for testing."""
SERVERS = {
    SERVER_PROD: "https://api.thetradedesk.com/workflows",
    SERVER_SANDBOX: "https://ext-api.sb.thetradedesk.com/workflows",
}
"""Contains the list of servers available to the SDK"""


@dataclass
class SDKConfiguration:
    client: Union[HttpClient, None]
    client_supplied: bool
    async_client: Union[AsyncHttpClient, None]
    async_client_supplied: bool
    debug_logger: Logger
    security: Optional[Union[models.Security, Callable[[], models.Security]]] = None
    server_url: Optional[str] = ""
    server: Optional[str] = ""
    language: str = "python"
    openapi_doc_version: str = __openapi_doc_version__
    sdk_version: str = __version__
    gen_version: str = __gen_version__
    user_agent: str = __user_agent__
    retry_config: OptionalNullable[RetryConfig] = Field(default_factory=lambda: UNSET)
    timeout_ms: Optional[int] = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url is not None and self.server_url:
            return remove_suffix(self.server_url, "/"), {}
        if not self.server:
            self.server = SERVER_PROD

        if self.server not in SERVERS:
            raise ValueError(f'Invalid server "{self.server}"')

        return SERVERS[self.server], {}
