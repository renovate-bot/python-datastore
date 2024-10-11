# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.auth.transport.requests import AuthorizedSession  # type: ignore
import json  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming
from google.api_core import gapic_v1

from google.protobuf import json_format

from requests import __version__ as requests_version
import dataclasses
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings


from google.cloud.datastore_v1.types import datastore
from google.longrunning import operations_pb2  # type: ignore


from .rest_base import _BaseDatastoreRestTransport
from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)


class DatastoreRestInterceptor:
    """Interceptor for Datastore.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DatastoreRestTransport.

    .. code-block:: python
        class MyCustomDatastoreInterceptor(DatastoreRestInterceptor):
            def pre_allocate_ids(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_allocate_ids(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_begin_transaction(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_begin_transaction(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_commit(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_commit(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_lookup(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_lookup(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reserve_ids(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_reserve_ids(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_rollback(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_rollback(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_run_aggregation_query(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_run_aggregation_query(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_run_query(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_run_query(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DatastoreRestTransport(interceptor=MyCustomDatastoreInterceptor())
        client = DatastoreClient(transport=transport)


    """

    def pre_allocate_ids(
        self, request: datastore.AllocateIdsRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[datastore.AllocateIdsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for allocate_ids

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastore server.
        """
        return request, metadata

    def post_allocate_ids(
        self, response: datastore.AllocateIdsResponse
    ) -> datastore.AllocateIdsResponse:
        """Post-rpc interceptor for allocate_ids

        Override in a subclass to manipulate the response
        after it is returned by the Datastore server but before
        it is returned to user code.
        """
        return response

    def pre_begin_transaction(
        self,
        request: datastore.BeginTransactionRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[datastore.BeginTransactionRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for begin_transaction

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastore server.
        """
        return request, metadata

    def post_begin_transaction(
        self, response: datastore.BeginTransactionResponse
    ) -> datastore.BeginTransactionResponse:
        """Post-rpc interceptor for begin_transaction

        Override in a subclass to manipulate the response
        after it is returned by the Datastore server but before
        it is returned to user code.
        """
        return response

    def pre_commit(
        self, request: datastore.CommitRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[datastore.CommitRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for commit

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastore server.
        """
        return request, metadata

    def post_commit(
        self, response: datastore.CommitResponse
    ) -> datastore.CommitResponse:
        """Post-rpc interceptor for commit

        Override in a subclass to manipulate the response
        after it is returned by the Datastore server but before
        it is returned to user code.
        """
        return response

    def pre_lookup(
        self, request: datastore.LookupRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[datastore.LookupRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for lookup

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastore server.
        """
        return request, metadata

    def post_lookup(
        self, response: datastore.LookupResponse
    ) -> datastore.LookupResponse:
        """Post-rpc interceptor for lookup

        Override in a subclass to manipulate the response
        after it is returned by the Datastore server but before
        it is returned to user code.
        """
        return response

    def pre_reserve_ids(
        self, request: datastore.ReserveIdsRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[datastore.ReserveIdsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for reserve_ids

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastore server.
        """
        return request, metadata

    def post_reserve_ids(
        self, response: datastore.ReserveIdsResponse
    ) -> datastore.ReserveIdsResponse:
        """Post-rpc interceptor for reserve_ids

        Override in a subclass to manipulate the response
        after it is returned by the Datastore server but before
        it is returned to user code.
        """
        return response

    def pre_rollback(
        self, request: datastore.RollbackRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[datastore.RollbackRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for rollback

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastore server.
        """
        return request, metadata

    def post_rollback(
        self, response: datastore.RollbackResponse
    ) -> datastore.RollbackResponse:
        """Post-rpc interceptor for rollback

        Override in a subclass to manipulate the response
        after it is returned by the Datastore server but before
        it is returned to user code.
        """
        return response

    def pre_run_aggregation_query(
        self,
        request: datastore.RunAggregationQueryRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[datastore.RunAggregationQueryRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for run_aggregation_query

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastore server.
        """
        return request, metadata

    def post_run_aggregation_query(
        self, response: datastore.RunAggregationQueryResponse
    ) -> datastore.RunAggregationQueryResponse:
        """Post-rpc interceptor for run_aggregation_query

        Override in a subclass to manipulate the response
        after it is returned by the Datastore server but before
        it is returned to user code.
        """
        return response

    def pre_run_query(
        self, request: datastore.RunQueryRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[datastore.RunQueryRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for run_query

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastore server.
        """
        return request, metadata

    def post_run_query(
        self, response: datastore.RunQueryResponse
    ) -> datastore.RunQueryResponse:
        """Post-rpc interceptor for run_query

        Override in a subclass to manipulate the response
        after it is returned by the Datastore server but before
        it is returned to user code.
        """
        return response

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.CancelOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastore server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Datastore server but before
        it is returned to user code.
        """
        return response

    def pre_delete_operation(
        self,
        request: operations_pb2.DeleteOperationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastore server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the Datastore server but before
        it is returned to user code.
        """
        return response

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.GetOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastore server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Datastore server but before
        it is returned to user code.
        """
        return response

    def pre_list_operations(
        self,
        request: operations_pb2.ListOperationsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.ListOperationsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastore server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Datastore server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class DatastoreRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DatastoreRestInterceptor


class DatastoreRestTransport(_BaseDatastoreRestTransport):
    """REST backend synchronous transport for Datastore.

    Each RPC normalizes the partition IDs of the keys in its
    input entities, and always returns entities with keys with
    normalized partition IDs. This applies to all keys and entities,
    including those in values, except keys with both an empty path
    and an empty or unset partition ID. Normalization of input keys
    sets the project ID (if not already set) to the project ID from
    the request.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "datastore.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[DatastoreRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'datastore.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            url_scheme=url_scheme,
            api_audience=api_audience,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or DatastoreRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _AllocateIds(_BaseDatastoreRestTransport._BaseAllocateIds, DatastoreRestStub):
        def __hash__(self):
            return hash("DatastoreRestTransport.AllocateIds")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: datastore.AllocateIdsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> datastore.AllocateIdsResponse:
            r"""Call the allocate ids method over HTTP.

            Args:
                request (~.datastore.AllocateIdsRequest):
                    The request object. The request for
                [Datastore.AllocateIds][google.datastore.v1.Datastore.AllocateIds].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.datastore.AllocateIdsResponse:
                    The response for
                [Datastore.AllocateIds][google.datastore.v1.Datastore.AllocateIds].

            """

            http_options = (
                _BaseDatastoreRestTransport._BaseAllocateIds._get_http_options()
            )
            request, metadata = self._interceptor.pre_allocate_ids(request, metadata)
            transcoded_request = (
                _BaseDatastoreRestTransport._BaseAllocateIds._get_transcoded_request(
                    http_options, request
                )
            )

            body = _BaseDatastoreRestTransport._BaseAllocateIds._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = (
                _BaseDatastoreRestTransport._BaseAllocateIds._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = DatastoreRestTransport._AllocateIds._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = datastore.AllocateIdsResponse()
            pb_resp = datastore.AllocateIdsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_allocate_ids(resp)
            return resp

    class _BeginTransaction(
        _BaseDatastoreRestTransport._BaseBeginTransaction, DatastoreRestStub
    ):
        def __hash__(self):
            return hash("DatastoreRestTransport.BeginTransaction")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: datastore.BeginTransactionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> datastore.BeginTransactionResponse:
            r"""Call the begin transaction method over HTTP.

            Args:
                request (~.datastore.BeginTransactionRequest):
                    The request object. The request for
                [Datastore.BeginTransaction][google.datastore.v1.Datastore.BeginTransaction].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.datastore.BeginTransactionResponse:
                    The response for
                [Datastore.BeginTransaction][google.datastore.v1.Datastore.BeginTransaction].

            """

            http_options = (
                _BaseDatastoreRestTransport._BaseBeginTransaction._get_http_options()
            )
            request, metadata = self._interceptor.pre_begin_transaction(
                request, metadata
            )
            transcoded_request = _BaseDatastoreRestTransport._BaseBeginTransaction._get_transcoded_request(
                http_options, request
            )

            body = _BaseDatastoreRestTransport._BaseBeginTransaction._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseDatastoreRestTransport._BaseBeginTransaction._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = DatastoreRestTransport._BeginTransaction._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = datastore.BeginTransactionResponse()
            pb_resp = datastore.BeginTransactionResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_begin_transaction(resp)
            return resp

    class _Commit(_BaseDatastoreRestTransport._BaseCommit, DatastoreRestStub):
        def __hash__(self):
            return hash("DatastoreRestTransport.Commit")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: datastore.CommitRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> datastore.CommitResponse:
            r"""Call the commit method over HTTP.

            Args:
                request (~.datastore.CommitRequest):
                    The request object. The request for
                [Datastore.Commit][google.datastore.v1.Datastore.Commit].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.datastore.CommitResponse:
                    The response for
                [Datastore.Commit][google.datastore.v1.Datastore.Commit].

            """

            http_options = _BaseDatastoreRestTransport._BaseCommit._get_http_options()
            request, metadata = self._interceptor.pre_commit(request, metadata)
            transcoded_request = (
                _BaseDatastoreRestTransport._BaseCommit._get_transcoded_request(
                    http_options, request
                )
            )

            body = _BaseDatastoreRestTransport._BaseCommit._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = (
                _BaseDatastoreRestTransport._BaseCommit._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = DatastoreRestTransport._Commit._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = datastore.CommitResponse()
            pb_resp = datastore.CommitResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_commit(resp)
            return resp

    class _Lookup(_BaseDatastoreRestTransport._BaseLookup, DatastoreRestStub):
        def __hash__(self):
            return hash("DatastoreRestTransport.Lookup")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: datastore.LookupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> datastore.LookupResponse:
            r"""Call the lookup method over HTTP.

            Args:
                request (~.datastore.LookupRequest):
                    The request object. The request for
                [Datastore.Lookup][google.datastore.v1.Datastore.Lookup].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.datastore.LookupResponse:
                    The response for
                [Datastore.Lookup][google.datastore.v1.Datastore.Lookup].

            """

            http_options = _BaseDatastoreRestTransport._BaseLookup._get_http_options()
            request, metadata = self._interceptor.pre_lookup(request, metadata)
            transcoded_request = (
                _BaseDatastoreRestTransport._BaseLookup._get_transcoded_request(
                    http_options, request
                )
            )

            body = _BaseDatastoreRestTransport._BaseLookup._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = (
                _BaseDatastoreRestTransport._BaseLookup._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = DatastoreRestTransport._Lookup._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = datastore.LookupResponse()
            pb_resp = datastore.LookupResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_lookup(resp)
            return resp

    class _ReserveIds(_BaseDatastoreRestTransport._BaseReserveIds, DatastoreRestStub):
        def __hash__(self):
            return hash("DatastoreRestTransport.ReserveIds")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: datastore.ReserveIdsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> datastore.ReserveIdsResponse:
            r"""Call the reserve ids method over HTTP.

            Args:
                request (~.datastore.ReserveIdsRequest):
                    The request object. The request for
                [Datastore.ReserveIds][google.datastore.v1.Datastore.ReserveIds].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.datastore.ReserveIdsResponse:
                    The response for
                [Datastore.ReserveIds][google.datastore.v1.Datastore.ReserveIds].

            """

            http_options = (
                _BaseDatastoreRestTransport._BaseReserveIds._get_http_options()
            )
            request, metadata = self._interceptor.pre_reserve_ids(request, metadata)
            transcoded_request = (
                _BaseDatastoreRestTransport._BaseReserveIds._get_transcoded_request(
                    http_options, request
                )
            )

            body = _BaseDatastoreRestTransport._BaseReserveIds._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = (
                _BaseDatastoreRestTransport._BaseReserveIds._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = DatastoreRestTransport._ReserveIds._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = datastore.ReserveIdsResponse()
            pb_resp = datastore.ReserveIdsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_reserve_ids(resp)
            return resp

    class _Rollback(_BaseDatastoreRestTransport._BaseRollback, DatastoreRestStub):
        def __hash__(self):
            return hash("DatastoreRestTransport.Rollback")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: datastore.RollbackRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> datastore.RollbackResponse:
            r"""Call the rollback method over HTTP.

            Args:
                request (~.datastore.RollbackRequest):
                    The request object. The request for
                [Datastore.Rollback][google.datastore.v1.Datastore.Rollback].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.datastore.RollbackResponse:
                    The response for
                [Datastore.Rollback][google.datastore.v1.Datastore.Rollback].
                (an empty message).

            """

            http_options = _BaseDatastoreRestTransport._BaseRollback._get_http_options()
            request, metadata = self._interceptor.pre_rollback(request, metadata)
            transcoded_request = (
                _BaseDatastoreRestTransport._BaseRollback._get_transcoded_request(
                    http_options, request
                )
            )

            body = _BaseDatastoreRestTransport._BaseRollback._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = (
                _BaseDatastoreRestTransport._BaseRollback._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = DatastoreRestTransport._Rollback._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = datastore.RollbackResponse()
            pb_resp = datastore.RollbackResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_rollback(resp)
            return resp

    class _RunAggregationQuery(
        _BaseDatastoreRestTransport._BaseRunAggregationQuery, DatastoreRestStub
    ):
        def __hash__(self):
            return hash("DatastoreRestTransport.RunAggregationQuery")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: datastore.RunAggregationQueryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> datastore.RunAggregationQueryResponse:
            r"""Call the run aggregation query method over HTTP.

            Args:
                request (~.datastore.RunAggregationQueryRequest):
                    The request object. The request for
                [Datastore.RunAggregationQuery][google.datastore.v1.Datastore.RunAggregationQuery].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.datastore.RunAggregationQueryResponse:
                    The response for
                [Datastore.RunAggregationQuery][google.datastore.v1.Datastore.RunAggregationQuery].

            """

            http_options = (
                _BaseDatastoreRestTransport._BaseRunAggregationQuery._get_http_options()
            )
            request, metadata = self._interceptor.pre_run_aggregation_query(
                request, metadata
            )
            transcoded_request = _BaseDatastoreRestTransport._BaseRunAggregationQuery._get_transcoded_request(
                http_options, request
            )

            body = _BaseDatastoreRestTransport._BaseRunAggregationQuery._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseDatastoreRestTransport._BaseRunAggregationQuery._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = DatastoreRestTransport._RunAggregationQuery._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = datastore.RunAggregationQueryResponse()
            pb_resp = datastore.RunAggregationQueryResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_run_aggregation_query(resp)
            return resp

    class _RunQuery(_BaseDatastoreRestTransport._BaseRunQuery, DatastoreRestStub):
        def __hash__(self):
            return hash("DatastoreRestTransport.RunQuery")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: datastore.RunQueryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> datastore.RunQueryResponse:
            r"""Call the run query method over HTTP.

            Args:
                request (~.datastore.RunQueryRequest):
                    The request object. The request for
                [Datastore.RunQuery][google.datastore.v1.Datastore.RunQuery].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.datastore.RunQueryResponse:
                    The response for
                [Datastore.RunQuery][google.datastore.v1.Datastore.RunQuery].

            """

            http_options = _BaseDatastoreRestTransport._BaseRunQuery._get_http_options()
            request, metadata = self._interceptor.pre_run_query(request, metadata)
            transcoded_request = (
                _BaseDatastoreRestTransport._BaseRunQuery._get_transcoded_request(
                    http_options, request
                )
            )

            body = _BaseDatastoreRestTransport._BaseRunQuery._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = (
                _BaseDatastoreRestTransport._BaseRunQuery._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = DatastoreRestTransport._RunQuery._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = datastore.RunQueryResponse()
            pb_resp = datastore.RunQueryResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_run_query(resp)
            return resp

    @property
    def allocate_ids(
        self,
    ) -> Callable[[datastore.AllocateIdsRequest], datastore.AllocateIdsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AllocateIds(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def begin_transaction(
        self,
    ) -> Callable[
        [datastore.BeginTransactionRequest], datastore.BeginTransactionResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BeginTransaction(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def commit(self) -> Callable[[datastore.CommitRequest], datastore.CommitResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Commit(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def lookup(self) -> Callable[[datastore.LookupRequest], datastore.LookupResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Lookup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def reserve_ids(
        self,
    ) -> Callable[[datastore.ReserveIdsRequest], datastore.ReserveIdsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ReserveIds(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def rollback(
        self,
    ) -> Callable[[datastore.RollbackRequest], datastore.RollbackResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Rollback(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def run_aggregation_query(
        self,
    ) -> Callable[
        [datastore.RunAggregationQueryRequest], datastore.RunAggregationQueryResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RunAggregationQuery(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def run_query(
        self,
    ) -> Callable[[datastore.RunQueryRequest], datastore.RunQueryResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RunQuery(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseDatastoreRestTransport._BaseCancelOperation, DatastoreRestStub
    ):
        def __hash__(self):
            return hash("DatastoreRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.CancelOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> None:
            r"""Call the cancel operation method over HTTP.

            Args:
                request (operations_pb2.CancelOperationRequest):
                    The request object for CancelOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options = (
                _BaseDatastoreRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request = _BaseDatastoreRestTransport._BaseCancelOperation._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = (
                _BaseDatastoreRestTransport._BaseCancelOperation._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = DatastoreRestTransport._CancelOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BaseDatastoreRestTransport._BaseDeleteOperation, DatastoreRestStub
    ):
        def __hash__(self):
            return hash("DatastoreRestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.DeleteOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> None:
            r"""Call the delete operation method over HTTP.

            Args:
                request (operations_pb2.DeleteOperationRequest):
                    The request object for DeleteOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options = (
                _BaseDatastoreRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request = _BaseDatastoreRestTransport._BaseDeleteOperation._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = (
                _BaseDatastoreRestTransport._BaseDeleteOperation._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = DatastoreRestTransport._DeleteOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseDatastoreRestTransport._BaseGetOperation, DatastoreRestStub
    ):
        def __hash__(self):
            return hash("DatastoreRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.GetOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the get operation method over HTTP.

            Args:
                request (operations_pb2.GetOperationRequest):
                    The request object for GetOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                operations_pb2.Operation: Response from GetOperation method.
            """

            http_options = (
                _BaseDatastoreRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request = (
                _BaseDatastoreRestTransport._BaseGetOperation._get_transcoded_request(
                    http_options, request
                )
            )

            # Jsonify the query params
            query_params = (
                _BaseDatastoreRestTransport._BaseGetOperation._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = DatastoreRestTransport._GetOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.Operation()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_operation(resp)
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(
        _BaseDatastoreRestTransport._BaseListOperations, DatastoreRestStub
    ):
        def __hash__(self):
            return hash("DatastoreRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.ListOperationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.ListOperationsResponse:
            r"""Call the list operations method over HTTP.

            Args:
                request (operations_pb2.ListOperationsRequest):
                    The request object for ListOperations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                operations_pb2.ListOperationsResponse: Response from ListOperations method.
            """

            http_options = (
                _BaseDatastoreRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request = (
                _BaseDatastoreRestTransport._BaseListOperations._get_transcoded_request(
                    http_options, request
                )
            )

            # Jsonify the query params
            query_params = (
                _BaseDatastoreRestTransport._BaseListOperations._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = DatastoreRestTransport._ListOperations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_operations(resp)
            return resp

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("DatastoreRestTransport",)
