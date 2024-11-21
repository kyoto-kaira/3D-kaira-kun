FROM python:3.9-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:0.4.21 /uv /uvx /bin/

WORKDIR /app
COPY AnimatedDrawings AnimatedDrawings
COPY Motion Motion
COPY motion-diffusion-model motion-diffusion-model
COPY app.py .
COPY entrypoint.sh .
COPY npy_to_bvh.py .
COPY requirements.txt .
RUN chmod +x ./entrypoint.sh

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

CMD ["./entrypoint.sh"]
