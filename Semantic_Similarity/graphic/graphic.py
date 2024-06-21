import matplotlib.pyplot as plt

# Dati
top_k = [3, 5, 7, 10, 15, 20, 25, 30, 50, 70, 100]
accuracy = [0.8908, 0.91379, 0.92528, 0.9425, 0.9540, 0.9597, 0.96551, 0.9712, 0.9712, 0.9827, 1]
time_seconds = [40, 60, 78, 111, 168, 225, 280, 328, 543, 764, 1087]

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

# Creare un secondo asse per il tempo
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Time (seconds)', color=color)
ax2.plot(top_k, time_seconds, color=color, marker='o', linestyle='-')
for i, txt in enumerate(time_seconds):
    ax2.annotate(f'{txt:.0f}', (top_k[i], time_seconds[i]), textcoords="offset points", xytext=(0,-15), ha='center')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title("Accuracy and Time vs. Top-k with Values")
plt.show()
