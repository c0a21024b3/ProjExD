import random
import datetime

def main():
    ans = shutudai()
    kaito(ans)

def shutudai():
    q = [["サザエの旦那の名前は？",["マスオ","ますお"]],
         ["カツオの妹の名前は？",["ワカメ","わかめ"]],
         ["タラオはカツオから見てどんな関係？",["甥","おい","甥っ子","おいっこ"]]]
    n = random.randint(0,2)
    ans = q[n][1]
    print("問題:")
    print(q[n][0])
    return ans

def kaito(ans):
    uans = input("解答してください:")
    if uans in ans:
        print("正解")
    else:
        print("不正解")
    

if __name__ == "__main__":
    main()
