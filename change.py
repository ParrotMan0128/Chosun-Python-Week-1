price = int(input("물건 값을 입력 하십시오."));

note = int(input("1000원 지폐 개수"));
coin500 = int(input("500원 동전 개수"));
coin100 = int(input("100원 동전 개수"));

change = note * 1000 + coin500 * 500 + coin100 * 100 - price;

nCoin500 = change // 500;
change = change % 500;

nCoin100 = change // 100;
change = change % 100;

nCoin50 = change // 50;
change = change % 50;

nCoin10 = change // 10;
change = change % 10;

nCoin1 = change;

print("500원: " + str(nCoin500) + "개 | 100원: " + str(nCoin100) + "개 | 50원: " + str(nCoin50) + "개 | 10원: " + str(nCoin10) + "개 | 1원: " + str(nCoin1) + "개");

