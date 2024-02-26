import random # 乱数を使うためにインポート
import time # n秒間待つためにインポート
print("""                                       
石取りゲームのルール：
石の数が乱数で決まります（15〜22個）
先行、後攻もランダムに決まります。
プレイヤーとコンピューターが交互に1〜3個ずつ取ります。
最後の1個を取ることになった方の負けです。
残りが3個以下で全部取ってしまうと負けとします。
""") # ゲームの説明を出力("""でくくることで複数の行をprint()できる)

stone = random.randint(15, 22) # 石の数を乱数で決める
turn = random.randint(0, 1) # どちらの番か乱数で決める
take = 0 # 石を取った数を代入する変数

while stone>0: # 石が0より大きい間、繰り返す
  turn = 1 - turn # どちらの番かを変更
  print("-"*40) # 区切り線を40個分出力
  print("●"*stone, "石の数", stone)
  for i in range(stone): # for分で石の数だけ●を出力
    print("●", end="") # 19,20行はprint("●"*stone, "石の数", stone)で一行で記述可能
  print("石の数", stone) # stoneの値を出力
  if turn==0: # プレビューの番なら"あなたの番"と出力
    print("あなたの番")
    while True: # while,input(),ifでいくつ石を取るかを入力させる処理
      i = input("いくつ取りますか？") # 1〜3を入力した場合にtakeにその数を入れwhileを抜ける
      if i=="1" and stone>0: # それ以外の数を入力した場合はwhileを抜けずに再入力
        take = 1
        break
      if i=="2" and stone>1:
        take = 2
        break
      if i=="3" and stone>2:
        take = 3
        break
    print("あなたは", take, "取りました") # いくつ取ったかを出力
  else:
    print("コンピューターの番")
    take = (stone-1)%4 # 取る数を勝てる値とする
    if take==0: # その数が0になった場合は取る数を乱数で決める
        take = random.randint(1,3)
        if take>stone: take = stone # 石の残りの数より大きくしない
    time.sleep(1)
    print(take, "取りました")
  stone = stone - take
  time.sleep(1)

print("-------------- ゲーム終了 --------------")
if turn==1:
  print("あなたの勝ち！")
else:
  print("コンピューターの勝ち！")