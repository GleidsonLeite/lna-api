FROM python:3

# Updating image
RUN apt -y update

# Upgrading image
RUN apt -y upgrade

# # Installing python
# RUN apt-get install -y python3
# RUN apt-get install -y python3-pip
# # Upgrading image
# RUN pip3 install --upgrade pip
WORKDIR /edatools

# Installing git
RUN apt install -y git

# Installing essentials
RUN apt-get install -y build-essential

# Installing ngspice
RUN git clone https://github.com/ngspice/ngspice
WORKDIR /edatools/ngspice

RUN apt-get install -y libreadline6-dev libx11-dev libice-dev libxext-dev libxmu-dev autoconf libtool automake bison byacc
RUN ./autogen.sh
RUN mkdir release
RUN ls
WORKDIR /edatools/ngspice/release
RUN ../configure --with-x --with-readline=yes --disable-debug --enable-openmp --with-ngshared --enable-cider --prefix=/usr/local
RUN make
RUN make install

RUN apt-get -y install libngspice0-dev
RUN apt-get -y install libngspice0

# Installing skywater
WORKDIR /edatools
RUN git clone https://github.com/google/skywater-pdk.git 

WORKDIR /edatools/skywater-pdk

RUN git submodule init

RUN git submodule update libraries/sky130_fd_pr/latest

WORKDIR /usr/app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

RUN pyspice-post-installation --check-install

COPY . .

EXPOSE 5000

ENV FLASK_APP="/usr/app/src/app.py"

CMD [ "flask", "--debug", "run", "--port=3333", "--host=0.0.0.0" ]