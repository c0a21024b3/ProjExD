import random
import datetime

select_num = 10 #対象文字数
delete_num = 3 #欠損文字数
max_continue = 3 #最大繰り返し数

def main(): #ゲームの実行
    start = datetime.datetime.now() #開始時間の保存
    count = 0
    while count < max_continue:
        count += 1
        strs = select_alphabet()
        ans = shutudai(strs)
        hantei = kaito(ans)
        if hantei == 1:
            break
    end = datetime.datetime.now() #終了時間の保存
    print(f"記録は{(end - start).seconds}秒です") #開始から終了までの時間を秒で表示

def select_alphabet(): #対象文字の指定
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    strs = random.sample(alphabet,select_num)
    return strs

def shutudai(strs): #欠損文字を指定して出題
    print(" ".join(strs))
    del_strs = [] #欠損文字のリスト
    for i in range(delete_num):
        random.shuffle(strs)
        del_str = strs.pop()
        del_strs.append(del_str)
    print(" ".join(strs))
    return del_strs

def kaito(ans): #解答の確認
    kaito1 = input("欠損文字は何文字でしょう:")
    if kaito1 == str(delete_num):
        print("正解です。では、欠けている文字を1つずつ入力してください。")
    else:
        print("不正解です。もう一度やり直してください。")
        print("-" * 30)
        return
    
    for i in range(delete_num):
        kaito2 = input(f"{i+1}文字目の欠損文字は?:")
        if kaito2 in ans:
            ans.remove(kaito2)
        else:
            print("不正解です。もう一度やり直してください。")
            return
    print("全問正解です。おめでとうございます。")
    return 1
    
if __name__ == "__main__":
    main()