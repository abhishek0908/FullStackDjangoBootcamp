from datetime import datetime
today = datetime.today()
d1 = today.strftime("%d/%m/%Y")
t1 = today.strftime("%H:%M:%S")
print("d1 =", d1)
print("t1=",t1)