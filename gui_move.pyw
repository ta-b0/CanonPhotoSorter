import os
import shutil
import tkinter as tk
from tkinter import filedialog

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def move_files(source_path):
    # フォルダ名を指定
    cr3_folder = "CR3"
    cr3_sub_folder = "CR3_sub"
    jpg_folder = "JPG"
    jpg_sub_folder = "JPG_sub"

    # フォルダを作成
    cr3_folder_path = os.path.join(source_path, cr3_folder)
    cr3_sub_folder_path = os.path.join(source_path, cr3_sub_folder)
    jpg_folder_path = os.path.join(source_path, jpg_folder)
    jpg_sub_folder_path = os.path.join(source_path, jpg_sub_folder)

    create_folder_if_not_exists(cr3_folder_path)
    create_folder_if_not_exists(cr3_sub_folder_path)
    create_folder_if_not_exists(jpg_folder_path)
    create_folder_if_not_exists(jpg_sub_folder_path)

    # ソースディレクトリ内のすべてのファイルを取得
    files = os.listdir(source_path)

    # ファイルごとに処理
    for file in files:
        file_path = os.path.join(source_path, file)
        if file.endswith("_1.CR3"):
            # "_1.CR3"で終わるファイルをCR3_subフォルダに移動
            shutil.move(file_path, os.path.join(cr3_sub_folder_path, file))
        elif file.endswith(".CR3"):
            # ".CR3"で終わるファイルをCR3フォルダに移動
            shutil.move(file_path, os.path.join(cr3_folder_path, file))
        elif file.endswith("_1.JPG"):
            # "_1.JPG"で終わるファイルをJPG_subフォルダに移動
            shutil.move(file_path, os.path.join(jpg_sub_folder_path, file))
        elif file.endswith(".JPG"):
            # ".JPG"で終わるファイルをJPGフォルダに移動
            shutil.move(file_path, os.path.join(jpg_folder_path, file))

def browse_directory():
    folder_path = filedialog.askdirectory()
    if folder_path:
        move_files(folder_path)
        result_label.config(text="ファイルが移動されました")

# GUIウィンドウの作成
root = tk.Tk()
root.title("ファイル移動プログラム")

# ウィンドウサイズの設定
root.geometry("400x200")

# ラベル
label = tk.Label(root, text="フォルダを選択してください")
label.pack(pady=10)

# フォルダ選択ボタン
browse_button = tk.Button(root, text="フォルダを選択", command=browse_directory)
browse_button.pack()

# 結果表示ラベル
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
