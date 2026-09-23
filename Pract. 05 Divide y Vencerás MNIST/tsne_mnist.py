import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE


df = pd.read_csv("mnist_train.csv")
print("Base de datos cargada correctamente.")
print("Tamaño de la base de datos:", df.shape)
print("\nPrimeras filas:")
print(df.head())

y = df["label"]
X = df.drop("label", axis=1)

print("\nCaracterísticas X:", X.shape)
print("Etiquetas y:", y.shape)
print("\nAplicando t-SNE...")

tsne = TSNE(
    n_components=2,
    random_state=42
)

X_tsne = tsne.fit_transform(X)

print("t-SNE terminado.")
print("Nuevo tamaño:", X_tsne.shape)

plt.figure(figsize=(10, 8))

scatter = plt.scatter(
    X_tsne[:, 0],
    X_tsne[:, 1],
    c=y,
    cmap="tab10",
    s=5
)

plt.colorbar(scatter, label="Dígito")
plt.title("t-SNE aplicado al conjunto MNIST")
plt.xlabel("Componente 1")
plt.ylabel("Componente 2")
plt.show()


df_7 = df[df["label"] == 7]

print("\nCantidad de imágenes del dígito 7:", len(df_7))


X_7 = df_7.drop("label", axis=1)


print("\nAplicando t-SNE al dígito 7...")

tsne_7 = TSNE(
    n_components=2,
    random_state=42
)

X_tsne_7 = tsne_7.fit_transform(X_7)

print("t-SNE del dígito 7 terminado.")

plt.figure(figsize=(10, 8))
plt.scatter(
    X_tsne_7[:, 0],
    X_tsne_7[:, 1],
    s=5
)

plt.title("t-SNE del dígito 7")
plt.xlabel("Componente 1")
plt.ylabel("Componente 2")
plt.show()
