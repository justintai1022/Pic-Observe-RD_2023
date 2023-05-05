# Copyright The OpenTelemetry Authors
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


from sys import argv
from grpc import StatusCode

from requests import get

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter
)

from opentelemetry.propagate import inject
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
import logging


resource = Resource.create({SERVICE_NAME: "test-service-2"})
span_exporter = OTLPSpanExporter()

tracer_provider = TracerProvider(resource=resource)
trace.set_tracer_provider(tracer_provider)

span_processor = BatchSpanProcessor(span_exporter)
tracer_provider.add_span_processor(span_processor)


tracer = trace.get_tracer_provider().get_tracer(__name__)

assert len(argv) == 2

with tracer.start_as_current_span("client"):
    logging.warning("Log message in client span1")
    client_current_span = trace.get_current_span()
    ctx = trace.get_current_span().get_span_context()
    link_from_current = trace.Link(ctx)
    client_current_span.set_attribute("operation","client")
    client_current_span.set_attribute("operation.name", "Saying hello!")
    client_current_span.set_attribute("operation.other-stuff", [1, 2, 3])
    try:
        with tracer.start_as_current_span("client-server"):
            logging.warning("Log message in client span2")
            client_server_current_span = trace.get_current_span()
            client_server_current_span.set_attribute("operation","client-server")
            client_server_current_span.add_event("Gonna try it!")
            headers = {}
            inject(headers)
            requested = get(
                "http://172.20.49.90:80/server_request",
                params={"param": argv[1]},
                headers=headers,
            )

            assert requested.status_code == 200
            client_server_current_span.add_event("Did it!")
            with tracer.start_as_current_span("test1",links=[link_from_current]):
                logging.warning("Log message in client span4")
                print ('foo')
                with tracer.start_as_current_span("test2"):
                    logging.warning("Log message in client span5")
                    print ('book')
    except Exception as ex:
        client_current_span.set_status(StatusCode.Error)
        client_current_span.record_exception(ex)