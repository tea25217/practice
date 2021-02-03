# coding: utf-8
import tkinter
import event
from tkinter import messagebox


# ボタンがクリックされたら実行
def onButtonClick():
    word = inputBox.get().encode("utf_8")
    if event.main(word):
        messagebox.showinfo("検索結果を取得しました。(result.csv)")
    else:
        messagebox.showinfo("検索結果の取得に失敗しました")


# ウインドウの作成
root = tkinter.Tk()
root.title("Python GUI")
root.geometry("360x240")

# 入力欄の作成
inputBox = tkinter.Entry(width=40)
inputBox.place(x=10, y=100)

# ラベルの作成
inputLabel = tkinter.Label(text="検索ワード")
inputLabel.place(x=10, y=70)

# ボタンの作成
button = tkinter.Button(text="取得", command=onButtonClick)
button.place(x=10, y=130)

# ウインドウの描画
root.mainloop()
