import os
from PIL import Image, ImageEnhance

def adjust_brightness(input_folder, output_folder, brightness_factor):
    # 出力フォルダが存在しない場合は作成
    os.makedirs(output_folder, exist_ok=True)
    
    processed_count = 0
    error_count = 0

    print(f"Input folder: {input_folder}")
    print(f"Output folder: {output_folder}")
    print(f"Brightness factor: {brightness_factor}")

    # input_folder内のファイル・フォルダを再帰的に処理
    for root, dirs, files in os.walk(input_folder):
        print(f"Checking directory: {root}")
        print(f"Files found: {files}")
        for file in files:
            # 画像ファイルか確認
            if file.lower().endswith((".png", ".jpg", ".jpeg")):
                try:
                    # 入力画像と出力画像のパスを作成
                    input_image_path = os.path.join(root, file)
                    relative_path = os.path.relpath(root, input_folder)
                    output_image_dir = os.path.join(output_folder, relative_path)
                    output_image_path = os.path.join(output_image_dir, file)

                    print(f"Processing: {input_image_path}")
                    print(f"Output path: {output_image_path}")

                    # 出力先のフォルダが存在しない場合は作成
                    os.makedirs(output_image_dir, exist_ok=True)
                    
                    # 画像の明るさを調整
                    with Image.open(input_image_path) as img:
                        enhancer = ImageEnhance.Brightness(img)
                        img_brightened = enhancer.enhance(brightness_factor)
                        
                        # 調整後の画像を保存
                        img_brightened.save(output_image_path)
                    
                    processed_count += 1
                    print(f"Processed and saved: {output_image_path}")
                except Exception as e:
                    error_count += 1
                    print(f"エラーが発生しました: {input_image_path}: {str(e)}")
            else:
                print(f"非画像ファイル: {file}")

    print(f"処理完了: {processed_count}の画像処理が完了しました。, {error_count}件のエラーが発生しました。")

if __name__ == "__main__":
    input_folder = input("処理する画像フォルダのパスを入力してください: ")
    brightness_factor = float(input("明るさを調整する倍率を入力してください (例: 1.2 で 20% 明るくなります): "))
    output_folder = input("出力フォルダのパスを入力してください (Enter でデフォルト: brightness_<倍率>): ")
    
    if not output_folder:
        output_folder = f"brightness_{brightness_factor}"
    
    adjust_brightness(input_folder, output_folder, brightness_factor)
