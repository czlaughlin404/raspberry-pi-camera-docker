FROM resin/rpi-raspbian:latest

RUN apt-get update 
RUN apt-get install wget build-essential checkinstall
RUN apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

RUN cd /usr/src 
ADD https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz /usr/src/Python-3.6.0.tgz 
RUN cd /usr/src && tar xzf Python-3.6.0.tgz
RUN cd /usr/src/Python-3.6.0 && bash configure && make altinstall

RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip

RUN apt-get install git -y
RUN cd / && git clone --recursive https://github.com/waveform80/picamera  /picamera

RUN mkdir /picamera/build  #&& cmake
RUN cd /picamera && python3.6 setup.py install 

RUN apt-get update
RUN apt-get install --reinstall libraspberrypi0 libraspberrypi-dev libraspberrypi-doc libraspberrypi-bin

RUN pip3.6 install --upgrade pip
RUN pip3.6 install picamera

COPY /code/image_capture.py /code/image_capture.py

ENTRYPOINT [ "python3.6", "/code/image_capture.py" ]
