FROM python:3.9

# Updating image
RUN apt -y update

# Upgrading image
RUN apt -y upgrade

# Upgrading image
RUN pip3 install --upgrade pip

# Installing ngspice
RUN apt-get -y install ngspice
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

CMD ["flask", "run", "--host=0.0.0.0"]