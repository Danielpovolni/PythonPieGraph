import matplotlib.pyplot as plt
#1 tepla voda, 1 studena voda, 1 citronova stava, 3 cukor
percenta = 100/6
voda = percenta * 2
citronova_stava=percenta
cukor = percenta * 3
percenta=[voda,citronova_stava,cukor]
sastojci=["voda","citronova stava","cukor"]
e = [0,0,0.1]
plt.figure(figsize=(6,6))
plt.pie(percenta, labels=sastojci, explode=e )
plt.title("citronova stava sastojci v percentach")
plt.show()
plt.close()
