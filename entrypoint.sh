#!/bin/bash
Xvfb :99 -screen 0 1024x768x24 &
export DISPLAY=:99
exec streamlit run app.py --server.headless True
