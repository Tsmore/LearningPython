def damage(strength, defense):
    d = strength - defense
    return d

d = damage(100, 20)
print("相手の攻撃力100、自分の防御力20の時、ダメージは", d)
print("相手の攻撃力50、自分の防御力30の時、ダメージは", damage(50, 30))