FROM python:3.9-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:0.4.21 /uv /uvx /bin/

WORKDIR /app
COPY requirements.txt .
COPY AnimatedDrawings AnimatedDrawings

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libgl1 \
    libgl1-mesa-glx \
    libglib2.0-0 \
    xvfb \
    git \
    curl \
    tar \
    && curl -O https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz \
    && tar -xJf ffmpeg-release-amd64-static.tar.xz \
    && mv ffmpeg-*/ffmpeg /usr/local/bin/ \
    && mv ffmpeg-*/ffprobe /usr/local/bin/ \
    && rm -rf ffmpeg-* \
    && rm -rf /var/lib/apt/lists/*

RUN uv pip install -r requirements.txt --system

# Xvfb :99 -screen 0 1024x768x24 &
# export DISPLAY=:99
# streamlit run app.py

COPY entrypoint.sh .
RUN chmod +x ./entrypoint.sh

CMD ["./entrypoint.sh"]
