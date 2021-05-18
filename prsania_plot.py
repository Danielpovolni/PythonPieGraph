
tyzden=[0,0,1,0,1,1,1]

prsalo = round(tyzden.count(1))
neprsalo = round(tyzden.count(0))

#Pie diagram
import matplotlib.pyplot as plt
dazd=[prsalo, neprsalo]
labels=["prsalo", "neprsalo"]
plt.figure(figsize=(6,6))
plt.pie(dazd, labels=labels)
plt.title("kolko fni prsalo")
plt.show()
plt.close()
