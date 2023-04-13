num = int(input())
for i in range(num):
    cash = int(input())
    quarter = cash//25
    cash %= 25
    dime = cash // 10
    cash %= 10
    nickel = cash // 5
    cash %= 5
    penny = cash // 1
    cash %= 1
    print(quarter,dime,nickel,penny)