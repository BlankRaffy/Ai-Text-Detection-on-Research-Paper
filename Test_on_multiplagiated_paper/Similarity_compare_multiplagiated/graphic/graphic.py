import matplotlib.pyplot as plt

# Dati
top_k = [3, 5, 7, 10, 15, 20, 25, 30, 50, 70, 100, 120]
accuracy = [0.9367, 0.9367, 0.94, 0.9425, 0.9770, 0.9885, 0.9885, 0.9885, 0.9885, 0.9942, 0.9942, 0.9942]

# Creare il grafico con i punti
fig, ax1 = plt.subplots()

# Grafico per l'accuratezza
color = 'tab:blue'
ax1.set_xlabel('Top-k')
ax1.set_ylabel('Accuracy', color=color)
ax1.plot(top_k, accuracy, color=color, marker='o', linestyle='-')
for i, txt in enumerate(accuracy):
    ax1.annotate(f'{txt:.4f}', (top_k[i], accuracy[i]), textcoords="offset points", xytext=(0,10), ha='center')
ax1.tick_params(axis='y', labelcolor=color)

# Etichette specifiche per i tick sull'asse x
ax1.set_xticks(top_k)
ax1.set_xticklabels(top_k)

fig.tight_layout()
plt.title("Accuracy vs. Top-k with Values for conclusion")
plt.show()
