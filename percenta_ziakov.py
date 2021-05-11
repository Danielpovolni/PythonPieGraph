znamky=[5,3,4,5,5,2,5,5,3,4,2,5,5,5,3]
#kelko jesto z kazdej znamki
znamka5 = znamky.count(5)
znamka4 = znamky.count(4)
znamka3 = znamky.count(3)
znamka2 = znamky.count(2)
znamka1 = znamky.count(1)
#percenta pre kazdu znamku
celkovo = znamka5 + znamka4 +  znamka3 + znamka2 + znamka1
zpercenta = 100/celkovo
percenta_znamka5 = zpercenta * znamka5
percenta_znamka4 = zpercenta * znamka4
percenta_znamka3 = zpercenta * znamka3
percenta_znamka2 = zpercenta * znamka2
percenta_znamka1 = zpercenta * znamka1
#Pie diagram
import matplotlib.pyplot as plt
percenta=[percenta_znamka5,percenta_znamka4,percenta_znamka3,percenta_znamka2,percenta_znamka1]
znamki_labels=["znamka 5", "znamka 4", "znamka 3", "znamka 2", "znamka 1"]
e = [0,0,0.1,0,0]
plt.figure(figsize=(6,6))
plt.pie(percenta, labels=znamki_labels, explode=e )
plt.title("Percenta Ziakov po znamky")
plt.show()
plt.close()
