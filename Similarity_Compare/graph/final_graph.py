import matplotlib.pyplot as plt

# Dati di esempio per top-k, accuratezza e tempo (in secondi)
top_k = [3, 5, 7, 10, 15, 20, 25, 30, 50, 70, 100]
accuracy = [1,1,1,1,1,1,1,1,1,1,1]
number_paper = [3, 5, 7, 10, 15, 20, 25, 30, 50, 70, 100]


# Creazione della figura e degli assi
fig, ax1 = plt.subplots(figsize=(14, 7))

# Colori per i due assi
color1 = 'tab:blue'
color2 = 'tab:red'

# Tracciamento della curva per l'accuracy (asse sinistro)
ax1.set_xlabel('Top-k', fontsize=14, fontweight='bold')
ax1.set_ylabel('Accuracy', color=color1, fontsize=14, fontweight='bold')
ax1.plot(top_k, accuracy, color=color1, marker='o', linewidth=3, markersize=8, label="Accuracy")
ax1.tick_params(axis='y', labelcolor=color1, labelsize=12)
ax1.tick_params(axis='x', labelsize=12)
ax1.set_ylim([0.89, 1.02])

# Imposta i valori di top-k come ticks sull'asse x
ax1.set_xticks(top_k)

# Aggiunta delle etichette dei valori per Accuracy, con nuovo offset
for i, txt in enumerate(accuracy):
    ax1.annotate(f'{txt:.2f}', (top_k[i], accuracy[i]), fontsize=12, fontweight='bold', xytext=(-35, 10), textcoords='offset points')

# Creazione di un secondo asse per il tempo
ax2 = ax1.twinx()
ax2.set_ylabel('Number of paper', color=color2, fontsize=14, fontweight='bold')
ax2.plot(top_k, number_paper, color=color2, marker='o', linewidth=3, markersize=8, label="Time")
ax2.tick_params(axis='y', labelcolor=color2, labelsize=12)

# Aggiunta delle etichette dei valori per il tempo, con nuovo offset
for i, txt in enumerate(number_paper):
    ax2.annotate(f'{txt}', (top_k[i], number_paper[i]), fontsize=12, fontweight='bold', color=color2, xytext=(5, -10), textcoords='offset points')

# Titolo del grafico
plt.title('Accuracy and number of paper vs Top-k', fontsize=16, fontweight='bold')

# Mostrare il grafico
plt.show()
