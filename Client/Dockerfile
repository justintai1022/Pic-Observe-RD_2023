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
RUN pip install opentelemetry-api==1.12.0
RUN pip install opentelemetry-distro==0.33b0
RUN pip install opentelemetry-exporter-otlp==1.12.0
RUN pip install opentelemetry-exporter-otlp-proto-grpc==1.12.0
RUN pip install opentelemetry-exporter-otlp-proto-http==1.12.0
RUN pip install opentelemetry-propagator-b3==1.12.0
RUN pip install opentelemetry-sdk==1.12.0
RUN pip install opentelemetry-semantic-conventions==0.33b0
RUN pip install opentelemetry-util-http==0.33b0
RUN pip install opentelemetry-instrumentation-logging==0.33b0 # for loki have traceID
RUN pip install requests
RUN pip install grpcio
# 將當前目錄複製到容器的code目錄
ADD . /code/

#四月改成不要用pod的方式實作，改用K8S中的CronJob的形式來做，讓這個POD每五鐘執行一次，所以把下面的指令註解掉
#CMD ["opentelemetry-instrument","--traces_exporter","otlp", "python3", "client.py","justin"]