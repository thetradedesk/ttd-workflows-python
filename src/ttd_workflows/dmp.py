"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from ttd_workflows import models, utils
from ttd_workflows._hooks import HookContext
from ttd_workflows.types import BaseModel, OptionalNullable, UNSET
from ttd_workflows.utils import get_security_from_env
from ttd_workflows.utils.unmarshal_json_response import unmarshal_json_response
from typing import Any, Mapping, Optional, Union, cast


class Dmp(BaseSDK):
    def get_first_party_data_job(
        self,
        *,
        request: Optional[
            Union[models.FirstPartyDataInput, models.FirstPartyDataInputTypedDict]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GetFirstPartyDataJobResponse:
        r"""Submit a job for first-party data retrieval for an advertiser

        When a first-party data query is submitted, a job ID is returned.
        This job ID can be used to poll for the job's status using the associated operation under \"Job Status\".

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, Optional[models.FirstPartyDataInput])
        request = cast(Optional[models.FirstPartyDataInput], request)

        req = self._build_request(
            method="POST",
            path="/standardjob/firstpartydata",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, True, "json", Optional[models.FirstPartyDataInput]
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["5XX"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="getFirstPartyDataJob",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "4XX", "500", "503", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "202", "application/json"):
            return models.GetFirstPartyDataJobResponse(
                standard_job_submit_response=unmarshal_json_response(
                    Optional[models.StandardJobSubmitResponse], http_res
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
            )
        if utils.match_response(
            http_res, ["400", "401", "403", "404"], "application/json"
        ):
            response_data = unmarshal_json_response(
                models.ProblemDetailsErrorData, http_res
            )
            raise models.ProblemDetailsError(response_data, http_res)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, ["500", "503", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)

        raise models.APIError("Unexpected response received", http_res)

    async def get_first_party_data_job_async(
        self,
        *,
        request: Optional[
            Union[models.FirstPartyDataInput, models.FirstPartyDataInputTypedDict]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GetFirstPartyDataJobResponse:
        r"""Submit a job for first-party data retrieval for an advertiser

        When a first-party data query is submitted, a job ID is returned.
        This job ID can be used to poll for the job's status using the associated operation under \"Job Status\".

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, Optional[models.FirstPartyDataInput])
        request = cast(Optional[models.FirstPartyDataInput], request)

        req = self._build_request_async(
            method="POST",
            path="/standardjob/firstpartydata",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, True, "json", Optional[models.FirstPartyDataInput]
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["5XX"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="getFirstPartyDataJob",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "4XX", "500", "503", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "202", "application/json"):
            return models.GetFirstPartyDataJobResponse(
                standard_job_submit_response=unmarshal_json_response(
                    Optional[models.StandardJobSubmitResponse], http_res
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
            )
        if utils.match_response(
            http_res, ["400", "401", "403", "404"], "application/json"
        ):
            response_data = unmarshal_json_response(
                models.ProblemDetailsErrorData, http_res
            )
            raise models.ProblemDetailsError(response_data, http_res)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, ["500", "503", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)

        raise models.APIError("Unexpected response received", http_res)

    def get_third_party_data_job(
        self,
        *,
        request: Optional[
            Union[models.ThirdPartyDataInput, models.ThirdPartyDataInputTypedDict]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GetThirdPartyDataJobResponse:
        r"""Submit a job for third-party data retrieval for a partner

        When a third-party data query is submitted, a job ID is returned.
        This job ID can be used to poll for the job's status, and when complete, the results download link,
        using the associated operation under \"Job Status\".

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, Optional[models.ThirdPartyDataInput])
        request = cast(Optional[models.ThirdPartyDataInput], request)

        req = self._build_request(
            method="POST",
            path="/standardjob/thirdpartydata",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, True, "json", Optional[models.ThirdPartyDataInput]
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["5XX"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="getThirdPartyDataJob",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "4XX", "500", "503", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "202", "application/json"):
            return models.GetThirdPartyDataJobResponse(
                standard_job_submit_response=unmarshal_json_response(
                    Optional[models.StandardJobSubmitResponse], http_res
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
            )
        if utils.match_response(
            http_res, ["400", "401", "403", "404"], "application/json"
        ):
            response_data = unmarshal_json_response(
                models.ProblemDetailsErrorData, http_res
            )
            raise models.ProblemDetailsError(response_data, http_res)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, ["500", "503", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)

        raise models.APIError("Unexpected response received", http_res)

    async def get_third_party_data_job_async(
        self,
        *,
        request: Optional[
            Union[models.ThirdPartyDataInput, models.ThirdPartyDataInputTypedDict]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GetThirdPartyDataJobResponse:
        r"""Submit a job for third-party data retrieval for a partner

        When a third-party data query is submitted, a job ID is returned.
        This job ID can be used to poll for the job's status, and when complete, the results download link,
        using the associated operation under \"Job Status\".

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, Optional[models.ThirdPartyDataInput])
        request = cast(Optional[models.ThirdPartyDataInput], request)

        req = self._build_request_async(
            method="POST",
            path="/standardjob/thirdpartydata",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, True, "json", Optional[models.ThirdPartyDataInput]
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["5XX"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="getThirdPartyDataJob",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "4XX", "500", "503", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "202", "application/json"):
            return models.GetThirdPartyDataJobResponse(
                standard_job_submit_response=unmarshal_json_response(
                    Optional[models.StandardJobSubmitResponse], http_res
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
            )
        if utils.match_response(
            http_res, ["400", "401", "403", "404"], "application/json"
        ):
            response_data = unmarshal_json_response(
                models.ProblemDetailsErrorData, http_res
            )
            raise models.ProblemDetailsError(response_data, http_res)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, ["500", "503", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)

        raise models.APIError("Unexpected response received", http_res)
