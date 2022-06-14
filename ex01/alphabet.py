import random
import datetime
from xml.sax.handler import all_properties

select_num = 10
delete_num = 3
max_continue = 3

def main():
    start = datetime.datetime.now()
    count = 0
    while count < max_continue:
        count += 1
        strs = select_alphabet()
        ans = shutudai(strs)
        hantei = kaito(ans)
        if hantei == 1:
            break
    end = datetime.datetime.now()
    print(f"記録は{(end - start).seconds}秒です")

def select_alphabet():
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    strs = random.sample(alphabet,select_num)
    return strs

def shutudai(strs):
    print(" ".join(strs))
    del_strs = []
    for i in range(delete_num):
        random.shuffle(strs)
        del_str = strs.pop()
        del_strs.append(del_str)
    print(" ".join(strs))
    return del_strs

def kaito(ans):
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