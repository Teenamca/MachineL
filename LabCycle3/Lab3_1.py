print("Name :Teena Tom")
print("Reg No : SJC21MCA-2043")
import matplotlib.pyplot as plt
x = [2001,2002,2003,2004,2005,2006,2007]
y = [24000,22500,19700,17500,14500,10000,5800]

plt.plot(x, y, color='red', linestyle='dashed', linewidth = 3,
         marker='*', markerfacecolor='green', markersize=20)
plt.xlabel('Year')
plt.ylabel('Car Value')
plt.title("Value Depreciation")

plt.show()
