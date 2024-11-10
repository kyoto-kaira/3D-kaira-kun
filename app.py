import subprocess

import streamlit as st
from deep_translator import GoogleTranslator

MODEL_PATH = "./save/humanml_trans_enc_512_50steps/model000750000.pt"

# Page title
st.title("KaiRAくんを文章で動かそう！")

# Text input
prompt = st.text_input("プロンプトを入力", placeholder="例: 手を挙げる")

# Parameters
guidance_param = st.slider("Guidance Parameter", min_value=0.0, max_value=5.0, step=0.1, value=2.5)
motion_length = st.slider("Motion Length", min_value=1.0, max_value=9.8, step=0.1, value=6.0)

# Generate button
if st.button("生成"):
    if not prompt.strip():
        st.error("プロンプトを入力してください。")
    else:
        with st.status("生成中...", expanded=True) as status:
            translator = GoogleTranslator(source="auto", target="en")
            prompt_transleted = translator.translate(prompt)
            st.write(f"{prompt}\n--> {prompt_transleted}")

            st.write("[1/3] Text to motion...")
            cmd_text_to_motion = (
                "cd motion-diffusion-model"
                "&& python -m sample.generate"
                f" --model_path {MODEL_PATH}"
                " --output_dir ./results"
                f" --text_prompt '{prompt_transleted}'"
                " --num_repetitions 1"
                f" --guidance_param {guidance_param}"
                f" --motion_length {motion_length}"
            )
            subprocess.run(cmd_text_to_motion, shell=True)

            st.write("[2/3] Motion to BVH...")
            prompt_transleted = prompt_transleted.replace(" ", "_")
            cmd_npy_to_bvh = f"python npy_to_bvh.py --prompt '{prompt_transleted}'"
            subprocess.run(cmd_npy_to_bvh, shell=True)

            st.write("[3/3] BVH to MP4...")
            cmd_bvh_to_mp4 = (
                "cd AnimatedDrawings "
                "&& python export_mp4_example.py "
                "&& ffmpeg -i video.mp4 "
                "-c:v libx264 -crf 23 -preset veryfast output.mp4 -y"
            )
            subprocess.run(cmd_bvh_to_mp4, shell=True)

            status.update(
                label="生成が完了しました！",
                state="complete",
                expanded=False,
            )

        path_to_motion_mp4 = "motion-diffusion-model/results/sample00.mp4"
        left_column, right_column = st.columns(2)
        with left_column:
            st.video("AnimatedDrawings/output.mp4", autoplay=True, loop=True)
        with right_column:
            st.video(path_to_motion_mp4, autoplay=True, loop=True)
