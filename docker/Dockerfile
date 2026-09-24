# Build the image: 
#     Start docker, then in the command line run:
#     docker build -t bones_img .
#
# Create and run in a container: 
#     docker run --name bones_container -v /path/to/bones/docker:/home --hostname docker -it bones_img
# 
#     This is setup for an interactive shell. 
#     The folder ~/docker will be created in you home (host) if not already there and connected to /home in the docker container
#     This makes it easy to access and share files back and forth
#     add the --rm flag to delete the container on exit, like docker run --rm --name ...
#
# Connect to and existing container: 
#     docker start -ai bones_container
# 
#     -a attaches, and -i is interactive
#
# When entering the docker container you will start in /app where bones is installed.
# You can do "cp -r bones /home" to copy the install to /home/bones.
# This location is mounted to the host at /path/to/bones/docker (in the docker run command above).
# You will see that /path/to/bones/docker/bones is now present on the host 
# and matches /home/bones in the container.
# Inside the container you can run the bones code, 
# and then view/plot/edit the files on your local host.
#
#################################################################################

FROM ubuntu:24.04 AS buildit

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
&& apt-get install -y --no-install-recommends \
    ca-certificates \
    software-properties-common \
    wget \
    tar \
    git \
    cmake \
    make \
    g++ \
    pkg-config \
    liblapack-dev \
    libboost-dev \
    libhdf5-dev \
    libyaml-cpp-dev \
    libfmt-dev \
    vim \
&& add-apt-repository -y ppa:cantera-team/cantera \
&& apt-get update \
&& apt-get install -y --no-install-recommends libcantera3.2 libcantera-dev \
&& CANTERA_LIB_DIR=/usr/lib/$(gcc -print-multiarch) \
&& CANTERA_SHARED_LIB=$(find "$CANTERA_LIB_DIR" -maxdepth 1 -type f -name 'libcantera.so.*' -print -quit) \
&& test -n "$CANTERA_SHARED_LIB" \
&& ln -s "$CANTERA_SHARED_LIB" /usr/local/lib/libcantera.so \
&& ldconfig \
&& rm -rf /var/lib/apt/lists/*

ENV CANTERA_INCLUDE_PATH=/usr/include

############## Build Sundials

WORKDIR /app/

RUN wget https://github.com/LLNL/sundials/releases/download/v7.9.0/sundials-7.9.0.tar.gz \
&&  tar -xvzf sundials-7.9.0.tar.gz \
&&  rm sundials-7.9.0.tar.gz \
&&  cd sundials-7.9.0 \
&&  mkdir build \
&&  cd build \
&&  cmake .. \
&&  make -j8 \
&&  make install \
&&  ldconfig \
&&  cd ../../ \
&&  rm -r sundials-7.9.0

############## Build bones

RUN git clone https://github.com/BYUignite/bones.git -b v1.0 --depth=1 \
&&  cd bones \
&&  mkdir build \
&&  cd build \
&&  cmake .. -DCMAKE_FIND_LIBRARY_SUFFIXES=.so \
&&  make -j \
&&  make install \
&&  cd ../
