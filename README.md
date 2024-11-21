# 動くKaiRAくん

- 最初の実行だけ時間がかかります。(CLIPのモデルをダウンロードするため)

## Dockerでの実行方法

```
git clone --recurse-submodules https://github.com/kyoto-kaira/moving-kaira-kun.git
cd moving-kaira-kun
docker build -t moving-kaira-kun .
docker run -p 8501:8501 moving-kaira-kun
# ブラウザで http://localhost:8501 にアクセス
```

## 仮想環境での動かし方

- ffmpegが必要です。

```
git clone --recurse-submodules https://github.com/kyoto-kaira/moving-kaira-kun.git
cd moving-kaira-kun
uv venv -p 3.9.6
source ./venv/bin/activate
uv pip install -r requirements.txt
streamlit run app.py
```

