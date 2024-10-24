def calculate_change(total_amount, product_price):
    # お釣り計算
    change = total_amount - product_price
    if change < 0:
        print("支払金額が不足しています。")
        return

    print(f"お釣り: {change}円")

    # 硬貨記憶
    coins = [500, 100, 50, 10, 5, 1]
    change_dict = {}

    for coin in coins:
        count = change // coin
        change_dict[coin] = count
        change %= coin

    # 結果の表示
    for coin, count in change_dict.items():
        if count > 0:
            print(f"{coin}円硬貨: {count}枚")

if __name__ == "__main__":
    try:
        # 支払い金額と商品の金額入力
        total_amount = int(input("支払金額を入力してください（円）: "))
        product_price = int(input("商品の金額を入力してください（円）: "))
        
        # 計算
        calculate_change(total_amount, product_price)
    except ValueError:
        print("無効な入力です。整数を入力してください。")
