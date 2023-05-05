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

from flask import Flask, request
import logging
from opentelemetry import trace


app = Flask(__name__)
tracer = trace.get_tracer(__name__)

@app.route("/server_request")
def server_request():
    with tracer.start_as_current_span("example-request"):
        logging.warning("Log message in span3")
    print(request.args.get("param"))
    return "served"


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8082)