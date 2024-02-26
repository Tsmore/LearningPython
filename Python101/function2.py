def life_check(val):
    if val>0:
      print("まだ戦えます")
    else:
      print("もう戦えません")

print("体力値１００で関数を実行")
life_check(100)
print("体力値０で関数を実行")
life_check(0)