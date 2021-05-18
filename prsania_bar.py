tyzden=[0,0,1,0,1,1,1]
dni= ["pondelok", "utorok", "sreda","stvrtok","piatok","sobota", "nedela"]
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.bar(dni,tyzden, label=dni)
plt.title("Kolko prsalo cez tyzdem")
plt.show()
plt.close()
