FROM debian:bullseye-slim AS certs
WORKDIR /certs
RUN apt-get update && \
    apt-get install -y openssl && \
    openssl req -new -newkey rsa:2048 -nodes \
      -keyout key.pem \
      -x509 -days 365 \
      -out cert.pem \
      -subj "/C=US/ST=Texas/L=Austin/O=BlakeDeBenon/OU=ENG/CN=blakedebenon.com"
# Use build that includes bazel
# Source build file to build manually: https://github.com/bazelbuild/continuous-integration/blob/master/bazel/oci/Dockerfile
FROM gcr.io/bazel-public/bazel:8.1.1

# Prepare for setup
USER root

# Copy certs
COPY --from=certs /certs /certs
RUN chown ubuntu /certs --recursive

# Install & Setup AWS CLI
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get install -y zip && \
    apt-get install -y clang
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install
RUN aws configure set default.region us-east-1
RUN rm aws -rf && rm awscliv2.zip

# Setup Monorepo
RUN mkdir /home/ubuntu/demo_monorepo
RUN chown ubuntu /home/ubuntu --recursive
COPY . /home/ubuntu/demo_monorepo

# Run Example FastAPI
USER ubuntu
WORKDIR /home/ubuntu/demo_monorepo
RUN bazel build //services/example_fast_api/src/service:app
ENTRYPOINT ["bazel", "run", "//services/example_fast_api/src/service:app", "--", "--port", "3000", "--ssl_keyfile", "/certs/key.pem", "--ssl_certfile", "/certs/cert.pem"]
