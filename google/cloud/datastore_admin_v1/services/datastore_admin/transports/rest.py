# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
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
import logging
import json  # type: ignore

from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming
from google.api_core import gapic_v1
import google.protobuf

from google.protobuf import json_format
from google.api_core import operations_v1

from requests import __version__ as requests_version
import dataclasses
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings


from google.cloud.datastore_admin_v1.types import datastore_admin
from google.cloud.datastore_admin_v1.types import index
from google.longrunning import operations_pb2  # type: ignore


from .rest_base import _BaseDatastoreAdminRestTransport
from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = logging.getLogger(__name__)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=f"requests@{requests_version}",
)

if hasattr(DEFAULT_CLIENT_INFO, "protobuf_runtime_version"):  # pragma: NO COVER
    DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class DatastoreAdminRestInterceptor:
    """Interceptor for DatastoreAdmin.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DatastoreAdminRestTransport.

    .. code-block:: python
        class MyCustomDatastoreAdminInterceptor(DatastoreAdminRestInterceptor):
            def pre_create_index(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_index(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_index(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_index(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_entities(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_entities(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_index(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_index(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_entities(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_entities(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_indexes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_indexes(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DatastoreAdminRestTransport(interceptor=MyCustomDatastoreAdminInterceptor())
        client = DatastoreAdminClient(transport=transport)


    """

    def pre_create_index(
        self,
        request: datastore_admin.CreateIndexRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastore_admin.CreateIndexRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_index

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DatastoreAdmin server.
        """
        return request, metadata

    def post_create_index(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_index

        DEPRECATED. Please use the `post_create_index_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DatastoreAdmin server but before
        it is returned to user code. This `post_create_index` interceptor runs
        before the `post_create_index_with_metadata` interceptor.
        """
        return response

    def post_create_index_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_index

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DatastoreAdmin server but before it is returned to user code.

        We recommend only using this `post_create_index_with_metadata`
        interceptor in new development instead of the `post_create_index` interceptor.
        When both interceptors are used, this `post_create_index_with_metadata` interceptor runs after the
        `post_create_index` interceptor. The (possibly modified) response returned by
        `post_create_index` will be passed to
        `post_create_index_with_metadata`.
        """
        return response, metadata

    def pre_delete_index(
        self,
        request: datastore_admin.DeleteIndexRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastore_admin.DeleteIndexRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_index

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DatastoreAdmin server.
        """
        return request, metadata

    def post_delete_index(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_index

        DEPRECATED. Please use the `post_delete_index_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DatastoreAdmin server but before
        it is returned to user code. This `post_delete_index` interceptor runs
        before the `post_delete_index_with_metadata` interceptor.
        """
        return response

    def post_delete_index_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_index

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DatastoreAdmin server but before it is returned to user code.

        We recommend only using this `post_delete_index_with_metadata`
        interceptor in new development instead of the `post_delete_index` interceptor.
        When both interceptors are used, this `post_delete_index_with_metadata` interceptor runs after the
        `post_delete_index` interceptor. The (possibly modified) response returned by
        `post_delete_index` will be passed to
        `post_delete_index_with_metadata`.
        """
        return response, metadata

    def pre_export_entities(
        self,
        request: datastore_admin.ExportEntitiesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastore_admin.ExportEntitiesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for export_entities

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DatastoreAdmin server.
        """
        return request, metadata

    def post_export_entities(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_entities

        DEPRECATED. Please use the `post_export_entities_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DatastoreAdmin server but before
        it is returned to user code. This `post_export_entities` interceptor runs
        before the `post_export_entities_with_metadata` interceptor.
        """
        return response

    def post_export_entities_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_entities

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DatastoreAdmin server but before it is returned to user code.

        We recommend only using this `post_export_entities_with_metadata`
        interceptor in new development instead of the `post_export_entities` interceptor.
        When both interceptors are used, this `post_export_entities_with_metadata` interceptor runs after the
        `post_export_entities` interceptor. The (possibly modified) response returned by
        `post_export_entities` will be passed to
        `post_export_entities_with_metadata`.
        """
        return response, metadata

    def pre_get_index(
        self,
        request: datastore_admin.GetIndexRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastore_admin.GetIndexRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_index

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DatastoreAdmin server.
        """
        return request, metadata

    def post_get_index(self, response: index.Index) -> index.Index:
        """Post-rpc interceptor for get_index

        DEPRECATED. Please use the `post_get_index_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DatastoreAdmin server but before
        it is returned to user code. This `post_get_index` interceptor runs
        before the `post_get_index_with_metadata` interceptor.
        """
        return response

    def post_get_index_with_metadata(
        self, response: index.Index, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[index.Index, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_index

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DatastoreAdmin server but before it is returned to user code.

        We recommend only using this `post_get_index_with_metadata`
        interceptor in new development instead of the `post_get_index` interceptor.
        When both interceptors are used, this `post_get_index_with_metadata` interceptor runs after the
        `post_get_index` interceptor. The (possibly modified) response returned by
        `post_get_index` will be passed to
        `post_get_index_with_metadata`.
        """
        return response, metadata

    def pre_import_entities(
        self,
        request: datastore_admin.ImportEntitiesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastore_admin.ImportEntitiesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for import_entities

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DatastoreAdmin server.
        """
        return request, metadata

    def post_import_entities(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for import_entities

        DEPRECATED. Please use the `post_import_entities_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DatastoreAdmin server but before
        it is returned to user code. This `post_import_entities` interceptor runs
        before the `post_import_entities_with_metadata` interceptor.
        """
        return response

    def post_import_entities_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for import_entities

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DatastoreAdmin server but before it is returned to user code.

        We recommend only using this `post_import_entities_with_metadata`
        interceptor in new development instead of the `post_import_entities` interceptor.
        When both interceptors are used, this `post_import_entities_with_metadata` interceptor runs after the
        `post_import_entities` interceptor. The (possibly modified) response returned by
        `post_import_entities` will be passed to
        `post_import_entities_with_metadata`.
        """
        return response, metadata

    def pre_list_indexes(
        self,
        request: datastore_admin.ListIndexesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastore_admin.ListIndexesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_indexes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DatastoreAdmin server.
        """
        return request, metadata

    def post_list_indexes(
        self, response: datastore_admin.ListIndexesResponse
    ) -> datastore_admin.ListIndexesResponse:
        """Post-rpc interceptor for list_indexes

        DEPRECATED. Please use the `post_list_indexes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DatastoreAdmin server but before
        it is returned to user code. This `post_list_indexes` interceptor runs
        before the `post_list_indexes_with_metadata` interceptor.
        """
        return response

    def post_list_indexes_with_metadata(
        self,
        response: datastore_admin.ListIndexesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastore_admin.ListIndexesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_indexes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DatastoreAdmin server but before it is returned to user code.

        We recommend only using this `post_list_indexes_with_metadata`
        interceptor in new development instead of the `post_list_indexes` interceptor.
        When both interceptors are used, this `post_list_indexes_with_metadata` interceptor runs after the
        `post_list_indexes` interceptor. The (possibly modified) response returned by
        `post_list_indexes` will be passed to
        `post_list_indexes_with_metadata`.
        """
        return response, metadata

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DatastoreAdmin server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the DatastoreAdmin server but before
        it is returned to user code.
        """
        return response

    def pre_delete_operation(
        self,
        request: operations_pb2.DeleteOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DatastoreAdmin server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the DatastoreAdmin server but before
        it is returned to user code.
        """
        return response

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DatastoreAdmin server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the DatastoreAdmin server but before
        it is returned to user code.
        """
        return response

    def pre_list_operations(
        self,
        request: operations_pb2.ListOperationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.ListOperationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DatastoreAdmin server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the DatastoreAdmin server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class DatastoreAdminRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DatastoreAdminRestInterceptor


class DatastoreAdminRestTransport(_BaseDatastoreAdminRestTransport):
    """REST backend synchronous transport for DatastoreAdmin.

    Google Cloud Datastore Admin API

    The Datastore Admin API provides several admin services for
    Cloud Datastore.

    Concepts: Project, namespace, kind, and entity as defined in the
    Google Cloud Datastore API.

    Operation: An Operation represents work being performed in the
    background.

    EntityFilter: Allows specifying a subset of entities in a
    project. This is specified as a combination of kinds and
    namespaces (either or both of which may be all).

    Export/Import Service:

    - The Export/Import service provides the ability to copy all or
      a subset of entities to/from Google Cloud Storage.
    - Exported data may be imported into Cloud Datastore for any
      Google Cloud Platform project. It is not restricted to the
      export source project. It is possible to export from one
      project and then import into another.
    - Exported data can also be loaded into Google BigQuery for
      analysis.
    - Exports and imports are performed asynchronously. An Operation
      resource is created for each export/import. The state
      (including any errors encountered) of the export/import may be
      queried via the Operation resource.

    Index Service:

    - The index service manages Cloud Datastore composite indexes.
    - Index creation and deletion are performed asynchronously. An
      Operation resource is created for each such asynchronous
      operation. The state of the operation (including any errors
      encountered) may be queried via the Operation resource.

    Operation Service:

    - The Operations collection provides a record of actions
      performed for the specified project (including any operations
      in progress). Operations are not created directly but through
      calls on other collections or resources.
    - An operation that is not yet done may be cancelled. The
      request to cancel is asynchronous and the operation may
      continue to run for some time after the request to cancel is
      made.
    - An operation that is done may be deleted so that it is no
      longer listed as part of the Operation collection.
    - ListOperations returns all pending operations, but not
      completed operations.
    - Operations are created by service DatastoreAdmin, but are
      accessed via service google.longrunning.Operations.

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
        interceptor: Optional[DatastoreAdminRestInterceptor] = None,
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
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or DatastoreAdminRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
                "google.longrunning.Operations.CancelOperation": [
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/operations/*}:cancel",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateIndex(
        _BaseDatastoreAdminRestTransport._BaseCreateIndex, DatastoreAdminRestStub
    ):
        def __hash__(self):
            return hash("DatastoreAdminRestTransport.CreateIndex")

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
            request: datastore_admin.CreateIndexRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create index method over HTTP.

            Args:
                request (~.datastore_admin.CreateIndexRequest):
                    The request object. The request for
                [google.datastore.admin.v1.DatastoreAdmin.CreateIndex][google.datastore.admin.v1.DatastoreAdmin.CreateIndex].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseDatastoreAdminRestTransport._BaseCreateIndex._get_http_options()
            )

            request, metadata = self._interceptor.pre_create_index(request, metadata)
            transcoded_request = _BaseDatastoreAdminRestTransport._BaseCreateIndex._get_transcoded_request(
                http_options, request
            )

            body = _BaseDatastoreAdminRestTransport._BaseCreateIndex._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseDatastoreAdminRestTransport._BaseCreateIndex._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.datastore.admin_v1.DatastoreAdminClient.CreateIndex",
                    extra={
                        "serviceName": "google.datastore.admin.v1.DatastoreAdmin",
                        "rpcName": "CreateIndex",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastoreAdminRestTransport._CreateIndex._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_index(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_index_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.datastore.admin_v1.DatastoreAdminClient.create_index",
                    extra={
                        "serviceName": "google.datastore.admin.v1.DatastoreAdmin",
                        "rpcName": "CreateIndex",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteIndex(
        _BaseDatastoreAdminRestTransport._BaseDeleteIndex, DatastoreAdminRestStub
    ):
        def __hash__(self):
            return hash("DatastoreAdminRestTransport.DeleteIndex")

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
            request: datastore_admin.DeleteIndexRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete index method over HTTP.

            Args:
                request (~.datastore_admin.DeleteIndexRequest):
                    The request object. The request for
                [google.datastore.admin.v1.DatastoreAdmin.DeleteIndex][google.datastore.admin.v1.DatastoreAdmin.DeleteIndex].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseDatastoreAdminRestTransport._BaseDeleteIndex._get_http_options()
            )

            request, metadata = self._interceptor.pre_delete_index(request, metadata)
            transcoded_request = _BaseDatastoreAdminRestTransport._BaseDeleteIndex._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseDatastoreAdminRestTransport._BaseDeleteIndex._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.datastore.admin_v1.DatastoreAdminClient.DeleteIndex",
                    extra={
                        "serviceName": "google.datastore.admin.v1.DatastoreAdmin",
                        "rpcName": "DeleteIndex",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastoreAdminRestTransport._DeleteIndex._get_response(
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

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_index(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_index_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.datastore.admin_v1.DatastoreAdminClient.delete_index",
                    extra={
                        "serviceName": "google.datastore.admin.v1.DatastoreAdmin",
                        "rpcName": "DeleteIndex",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportEntities(
        _BaseDatastoreAdminRestTransport._BaseExportEntities, DatastoreAdminRestStub
    ):
        def __hash__(self):
            return hash("DatastoreAdminRestTransport.ExportEntities")

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
            request: datastore_admin.ExportEntitiesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export entities method over HTTP.

            Args:
                request (~.datastore_admin.ExportEntitiesRequest):
                    The request object. The request for
                [google.datastore.admin.v1.DatastoreAdmin.ExportEntities][google.datastore.admin.v1.DatastoreAdmin.ExportEntities].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseDatastoreAdminRestTransport._BaseExportEntities._get_http_options()
            )

            request, metadata = self._interceptor.pre_export_entities(request, metadata)
            transcoded_request = _BaseDatastoreAdminRestTransport._BaseExportEntities._get_transcoded_request(
                http_options, request
            )

            body = _BaseDatastoreAdminRestTransport._BaseExportEntities._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseDatastoreAdminRestTransport._BaseExportEntities._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.datastore.admin_v1.DatastoreAdminClient.ExportEntities",
                    extra={
                        "serviceName": "google.datastore.admin.v1.DatastoreAdmin",
                        "rpcName": "ExportEntities",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastoreAdminRestTransport._ExportEntities._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_export_entities(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_entities_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.datastore.admin_v1.DatastoreAdminClient.export_entities",
                    extra={
                        "serviceName": "google.datastore.admin.v1.DatastoreAdmin",
                        "rpcName": "ExportEntities",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetIndex(
        _BaseDatastoreAdminRestTransport._BaseGetIndex, DatastoreAdminRestStub
    ):
        def __hash__(self):
            return hash("DatastoreAdminRestTransport.GetIndex")

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
            request: datastore_admin.GetIndexRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> index.Index:
            r"""Call the get index method over HTTP.

            Args:
                request (~.datastore_admin.GetIndexRequest):
                    The request object. The request for
                [google.datastore.admin.v1.DatastoreAdmin.GetIndex][google.datastore.admin.v1.DatastoreAdmin.GetIndex].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.index.Index:
                    Datastore composite index definition.
            """

            http_options = (
                _BaseDatastoreAdminRestTransport._BaseGetIndex._get_http_options()
            )

            request, metadata = self._interceptor.pre_get_index(request, metadata)
            transcoded_request = (
                _BaseDatastoreAdminRestTransport._BaseGetIndex._get_transcoded_request(
                    http_options, request
                )
            )

            # Jsonify the query params
            query_params = (
                _BaseDatastoreAdminRestTransport._BaseGetIndex._get_query_params_json(
                    transcoded_request
                )
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.datastore.admin_v1.DatastoreAdminClient.GetIndex",
                    extra={
                        "serviceName": "google.datastore.admin.v1.DatastoreAdmin",
                        "rpcName": "GetIndex",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastoreAdminRestTransport._GetIndex._get_response(
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

            # Return the response
            resp = index.Index()
            pb_resp = index.Index.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_index(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_index_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = index.Index.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.datastore.admin_v1.DatastoreAdminClient.get_index",
                    extra={
                        "serviceName": "google.datastore.admin.v1.DatastoreAdmin",
                        "rpcName": "GetIndex",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ImportEntities(
        _BaseDatastoreAdminRestTransport._BaseImportEntities, DatastoreAdminRestStub
    ):
        def __hash__(self):
            return hash("DatastoreAdminRestTransport.ImportEntities")

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
            request: datastore_admin.ImportEntitiesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the import entities method over HTTP.

            Args:
                request (~.datastore_admin.ImportEntitiesRequest):
                    The request object. The request for
                [google.datastore.admin.v1.DatastoreAdmin.ImportEntities][google.datastore.admin.v1.DatastoreAdmin.ImportEntities].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseDatastoreAdminRestTransport._BaseImportEntities._get_http_options()
            )

            request, metadata = self._interceptor.pre_import_entities(request, metadata)
            transcoded_request = _BaseDatastoreAdminRestTransport._BaseImportEntities._get_transcoded_request(
                http_options, request
            )

            body = _BaseDatastoreAdminRestTransport._BaseImportEntities._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseDatastoreAdminRestTransport._BaseImportEntities._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.datastore.admin_v1.DatastoreAdminClient.ImportEntities",
                    extra={
                        "serviceName": "google.datastore.admin.v1.DatastoreAdmin",
                        "rpcName": "ImportEntities",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastoreAdminRestTransport._ImportEntities._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_import_entities(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_import_entities_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.datastore.admin_v1.DatastoreAdminClient.import_entities",
                    extra={
                        "serviceName": "google.datastore.admin.v1.DatastoreAdmin",
                        "rpcName": "ImportEntities",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListIndexes(
        _BaseDatastoreAdminRestTransport._BaseListIndexes, DatastoreAdminRestStub
    ):
        def __hash__(self):
            return hash("DatastoreAdminRestTransport.ListIndexes")

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
            request: datastore_admin.ListIndexesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datastore_admin.ListIndexesResponse:
            r"""Call the list indexes method over HTTP.

            Args:
                request (~.datastore_admin.ListIndexesRequest):
                    The request object. The request for
                [google.datastore.admin.v1.DatastoreAdmin.ListIndexes][google.datastore.admin.v1.DatastoreAdmin.ListIndexes].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datastore_admin.ListIndexesResponse:
                    The response for
                [google.datastore.admin.v1.DatastoreAdmin.ListIndexes][google.datastore.admin.v1.DatastoreAdmin.ListIndexes].

            """

            http_options = (
                _BaseDatastoreAdminRestTransport._BaseListIndexes._get_http_options()
            )

            request, metadata = self._interceptor.pre_list_indexes(request, metadata)
            transcoded_request = _BaseDatastoreAdminRestTransport._BaseListIndexes._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseDatastoreAdminRestTransport._BaseListIndexes._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.datastore.admin_v1.DatastoreAdminClient.ListIndexes",
                    extra={
                        "serviceName": "google.datastore.admin.v1.DatastoreAdmin",
                        "rpcName": "ListIndexes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastoreAdminRestTransport._ListIndexes._get_response(
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

            # Return the response
            resp = datastore_admin.ListIndexesResponse()
            pb_resp = datastore_admin.ListIndexesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_indexes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_indexes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = datastore_admin.ListIndexesResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.datastore.admin_v1.DatastoreAdminClient.list_indexes",
                    extra={
                        "serviceName": "google.datastore.admin.v1.DatastoreAdmin",
                        "rpcName": "ListIndexes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_index(
        self,
    ) -> Callable[[datastore_admin.CreateIndexRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateIndex(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_index(
        self,
    ) -> Callable[[datastore_admin.DeleteIndexRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteIndex(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_entities(
        self,
    ) -> Callable[[datastore_admin.ExportEntitiesRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportEntities(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_index(self) -> Callable[[datastore_admin.GetIndexRequest], index.Index]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetIndex(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def import_entities(
        self,
    ) -> Callable[[datastore_admin.ImportEntitiesRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportEntities(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_indexes(
        self,
    ) -> Callable[
        [datastore_admin.ListIndexesRequest], datastore_admin.ListIndexesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListIndexes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseDatastoreAdminRestTransport._BaseCancelOperation, DatastoreAdminRestStub
    ):
        def __hash__(self):
            return hash("DatastoreAdminRestTransport.CancelOperation")

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
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:
            r"""Call the cancel operation method over HTTP.

            Args:
                request (operations_pb2.CancelOperationRequest):
                    The request object for CancelOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseDatastoreAdminRestTransport._BaseCancelOperation._get_http_options()
            )

            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request = _BaseDatastoreAdminRestTransport._BaseCancelOperation._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseDatastoreAdminRestTransport._BaseCancelOperation._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.datastore.admin_v1.DatastoreAdminClient.CancelOperation",
                    extra={
                        "serviceName": "google.datastore.admin.v1.DatastoreAdmin",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastoreAdminRestTransport._CancelOperation._get_response(
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
        _BaseDatastoreAdminRestTransport._BaseDeleteOperation, DatastoreAdminRestStub
    ):
        def __hash__(self):
            return hash("DatastoreAdminRestTransport.DeleteOperation")

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
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:
            r"""Call the delete operation method over HTTP.

            Args:
                request (operations_pb2.DeleteOperationRequest):
                    The request object for DeleteOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseDatastoreAdminRestTransport._BaseDeleteOperation._get_http_options()
            )

            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request = _BaseDatastoreAdminRestTransport._BaseDeleteOperation._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseDatastoreAdminRestTransport._BaseDeleteOperation._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.datastore.admin_v1.DatastoreAdminClient.DeleteOperation",
                    extra={
                        "serviceName": "google.datastore.admin.v1.DatastoreAdmin",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastoreAdminRestTransport._DeleteOperation._get_response(
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
        _BaseDatastoreAdminRestTransport._BaseGetOperation, DatastoreAdminRestStub
    ):
        def __hash__(self):
            return hash("DatastoreAdminRestTransport.GetOperation")

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
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the get operation method over HTTP.

            Args:
                request (operations_pb2.GetOperationRequest):
                    The request object for GetOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.Operation: Response from GetOperation method.
            """

            http_options = (
                _BaseDatastoreAdminRestTransport._BaseGetOperation._get_http_options()
            )

            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request = _BaseDatastoreAdminRestTransport._BaseGetOperation._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseDatastoreAdminRestTransport._BaseGetOperation._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.datastore.admin_v1.DatastoreAdminClient.GetOperation",
                    extra={
                        "serviceName": "google.datastore.admin.v1.DatastoreAdmin",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastoreAdminRestTransport._GetOperation._get_response(
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
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.datastore.admin_v1.DatastoreAdminAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.datastore.admin.v1.DatastoreAdmin",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(
        _BaseDatastoreAdminRestTransport._BaseListOperations, DatastoreAdminRestStub
    ):
        def __hash__(self):
            return hash("DatastoreAdminRestTransport.ListOperations")

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
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.ListOperationsResponse:
            r"""Call the list operations method over HTTP.

            Args:
                request (operations_pb2.ListOperationsRequest):
                    The request object for ListOperations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.ListOperationsResponse: Response from ListOperations method.
            """

            http_options = (
                _BaseDatastoreAdminRestTransport._BaseListOperations._get_http_options()
            )

            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request = _BaseDatastoreAdminRestTransport._BaseListOperations._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseDatastoreAdminRestTransport._BaseListOperations._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.datastore.admin_v1.DatastoreAdminClient.ListOperations",
                    extra={
                        "serviceName": "google.datastore.admin.v1.DatastoreAdmin",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastoreAdminRestTransport._ListOperations._get_response(
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
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.datastore.admin_v1.DatastoreAdminAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.datastore.admin.v1.DatastoreAdmin",
                        "rpcName": "ListOperations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("DatastoreAdminRestTransport",)
