path = "input.csv"
csvreader = open(path, mode='r', encoding='UTF8')
txtwriter = open("00_buy_package_new.txt", mode='w', encoding='utf-8-sig')

c_line = csvreader.readline()[:-1]
popneed = c_line.split(',')

while True:
    c_line = csvreader.readline()[:-1]
    if not c_line:
        print("작업 완료")
        break

    popneed_by_wealth = c_line.split(',')

    txtwriter.writelines("wealth_" + str(popneed_by_wealth[0]) + " = {\n")
    txtwriter.writelines("\tpolitical_strength = " + str(popneed_by_wealth[1]) + "\n")
    txtwriter.writelines("\tgoods = {\n")
    for i in range(2, len(popneed)):
        if not popneed_by_wealth[i] == '0' and popneed_by_wealth[i]:
            txtwriter.writelines("\t\t" + popneed[i] + " = " + str(popneed_by_wealth[i]) + "\n")
    txtwriter.writelines("\t}\n")
    txtwriter.writelines("}\n")

txtwriter.close()
csvreader.close()