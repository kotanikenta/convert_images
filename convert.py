from PIL import Image

def convert_to_rgb(image_path, output_path):
    # 画像の読み込み
    image = Image.open(image_path)

    # チャンネルを調べる
    if image.mode == 'RGBA':
        # チャンネルが4チャンネル（RGBA）の場合、RGBに変換
        image = image.convert('RGB')

    # 変換後の画像を保存
    image.save(output_path)

# 使用例
input_image_path = 'cabbage-g5d22413f3_1280-removebg-preview.png'
output_image_path = 'cabbage.jpg'
convert_to_rgb(input_image_path, output_image_path)
