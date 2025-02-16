from flask import Flask,render_template,request, request, jsonify
import json
import sqlite3
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os
from dotenv import load_dotenv

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main_page():
    return render_template("index.html")

@app.route("/home", methods=["GET","POST"])
def home_page():
    return render_template("home.html")
@app.route("/next", methods=["GET","POST"])
def next_page():
    return render_template("next.html")

## 実行
if __name__ == "__main__":
    app.run(debug=True)



load_dotenv()


# タグを受け取るエンドポイント
@app.route('/receive_tags/', methods=['GET', 'POST'])
def receive_tags():
    try:
        # フロントエンドからのデータを取得
        data = request.json
        tags = data.get("tags")

        # データをリスト型に変換
        tags_list = list(tags)  # setやdict_keysなどもリスト化可能
        ingredients = tags_list
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400
        
        
    #APIキーの設定
    api_key = os.getenv('API_KEY') 
    client = genai.Client(api_key=api_key)


        # 食材を英語に変換
    def translate_ingredients(ingredients):
        response = client.models.translate_text(
        model='translate-text-1.0',
        text=ingredients,
        source='ja',
        target='en'
    )



    # 質問内容　後で食材のところは変数に変更
    response = client.models.generate_images(
    model='imagen-3.0-generate-002',
    prompt="""Please make a image of a black pot with {ingredients}.""",
    config=types.GenerateImagesConfig(
        number_of_images= 1,
    )
)

    for generated_image in response.generated_images:
        image = Image.open(BytesIO(generated_image.image.image_bytes))
        
    