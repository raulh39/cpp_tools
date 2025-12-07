# How to build:
#   docker build -t cpp:0.4 --build-arg USERNAME=$(id -nu) --build-arg USER_UID=$(id -u) --build-arg USER_GID=$(id -g) .
# How to run:
#   docker run --rm -it cpp:0.4

FROM fedora:43

ENV DEBIAN_FRONTEND=noninteractive

RUN dnf -y update && dnf -y install \
    clang-21 \
    llvm \
    lld \
    lldb \
    libcxx \
    libcxx-devel \
    libcxxabi \
    libcxxabi-devel \
    ninja-build \
    python3-pip \
    git \
    pkgconf-pkg-config \
    sudo \
    which \
    ca-certificates \
 && dnf clean all

RUN curl -L https://github.com/Kitware/CMake/releases/download/v4.2.0/cmake-4.2.0-linux-x86_64.sh -o /tmp/cmake.sh \
    && chmod +x /tmp/cmake.sh \
    && /tmp/cmake.sh --skip-license --prefix=/usr/local \
    && rm /tmp/cmake.sh

RUN pip3 install --no-cache-dir "conan>=2.0"

ARG USERNAME=dockeruser
ARG USER_UID=1000
ARG USER_GID=1000

RUN groupadd --gid ${USER_GID} ${USERNAME} \
 && useradd -ms /bin/bash --uid ${USER_UID} --gid ${USER_GID} ${USERNAME} \
 && echo "${USERNAME}:${USERNAME}" | chpasswd \
 && usermod -aG wheel ${USERNAME} \
 && echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-${USERNAME}

COPY conan-profiles/default /home/${USERNAME}/.conan2/profiles/default

RUN chown -R ${USERNAME}:${USERNAME} /home/${USERNAME}/.conan2

WORKDIR /workspace
USER ${USERNAME}
CMD ["/bin/bash", "-l"]
