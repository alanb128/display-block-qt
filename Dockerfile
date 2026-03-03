FROM python:3.10.18-bookworm

WORKDIR /usr/src/app

RUN apt update && apt install -y git nano libegl1 libxkbcommon0 qt6-wayland
RUN apt-get update && apt-get install -y libdbus-1-3 freeglut3-dev
RUN pip install PySide6

COPY *.py ./

CMD ["python", "qt-demo.py"]
