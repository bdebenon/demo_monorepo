# Example Monorepo

### Domain

Domain layers consist of domain models and use cases.

### Infra

Infra layers consist of Repositories which return domain models.

### Service

Services shouldn't have "business logic" in them. They can carry out a number of steps required to fulfill an
application need.


## Bazel
Demo Monorepo uses Bazel to manage dependencies and build artifacts. 

### Clearing bazel cache

Standard clean (try this first)

```
bazel clean
```

Clean everything

```
bazel clean --expunge
```

### Install Bazel

Install Bazel version 8.1.1

https://bazel.build/install/ubuntu

### Setup Buildifier

#### Install Go
```bash
sudo snap install go --classic
```

#### Install buildifier via go

```bash
go install github.com/bazelbuild/buildtools/buildifier@latest
```
(installs the binary to ~/go/bin/buildifier)

#### Add go binaries to path
```bash
echo "PATH=$PATH:~/go/bin" >> ~/.bashrc
```

#### (Optional) Setup IntelliJ

- Install `Bazel for IntelliJ`
- Set buildifier binary in 'Bazel Settings' (example '/home/work/go/bin/buildifier')
