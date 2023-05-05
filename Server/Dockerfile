# 從倉庫拉取帶有python 3.10的 Linux 環境
FROM python:3.10.7

# 設置 python 環境變數
ENV PYTHONUNBUFFERED 1

# 創建 code 文件夾並將其設置為工作目錄
RUN mkdir /code
WORKDIR /code
# 更新 pip
RUN pip install pip -U
# 將 requirements.txt 複製到容器的code目錄
ADD requirements.txt /code/
# 安裝庫
RUN pip install -r requirements.txt
RUN pip install opentelemetry-api
RUN pip install opentelemetry-distro
RUN pip install opentelemetry-exporter-otlp
RUN pip install opentelemetry-exporter-otlp-proto-grpc
RUN pip install opentelemetry-exporter-otlp-proto-http
RUN pip install opentelemetry-instrumentation
RUN pip install opentelemetry-instrumentation-flask
RUN pip install opentelemetry-instrumentation-requests
RUN pip install opentelemetry-instrumentation-wsgi
RUN pip install opentelemetry-propagator-b3
RUN pip install opentelemetry-proto
RUN pip install opentelemetry-sdk
RUN pip install opentelemetry-semantic-conventions
RUN pip install opentelemetry-util-http
RUN pip install opentelemetry-instrumentation-logging # for loki have traceID
RUN pip install flask
RUN pip install requests
RUN pip install grpcio
RUN apt-get update &&  apt-get install -y  curl
RUN apt-get install -y iputils-ping
RUN apt-get install -y dnsutils
# 將當前目錄複製到容器的code目錄
ADD . /code/

CMD ["opentelemetry-instrument","--traces_exporter","otlp", "python3", "server_uninstrumented.py"]