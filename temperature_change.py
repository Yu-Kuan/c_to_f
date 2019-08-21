#攝氏('C')轉換成華氏('F')程式
cels = input('請輸入攝氏溫度: ')
cels = float(cels)
fahr = float(cels * (9 / 5) + 32)
print('攝氏轉換成華氏:%3.1f ', fahr)
