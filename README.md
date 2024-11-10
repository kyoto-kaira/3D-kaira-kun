# moving-kaira-kun

## Environment setup

```bash
uv venv -p 3.9
source ./venv/bin/activate
uv pip install setuptools
uv pip install -e AnimatedDrawings/.
uv pip install spacy
uv pip install smplx
uv pip install matplotlib==3.3.4
uv pip install streamlit
uv pip install deep-translator
uv pip install git+https://github.com/openai/CLIP.git
uv pip install git+https://github.com/nico-von-huene/chumpy.git
# python -m spacy download en_core_web_sm
```

## Running the code

```bash
# Text to motion(npy)
cd motion-diffusion-model
python -m sample.generate --model_path ./save/humanml_trans_enc_512_50steps/model000750000.pt --text_prompt "move violently" --num_repetitions 1
# Motion(npy) to Motion(bvh)
cd ..
python npy_to_bvh.py --prompt "move violently"
# Motion(bvh) to Animation(mp4)
cd AnimatedDrawings
python export_mp4_example.py
```
