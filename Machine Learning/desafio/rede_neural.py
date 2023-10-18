import numpy as np
import torch
import torch.nn.functional as F
import torchvision
import matplotlib.pyplot as plt
from time import time
from torchvision import datasets, transforms
from torch import nn, optim

# site com os dataset -> yann.lecun.com/exdb/mnist/
transform = transforms.ToTensor() # Definindo a conversão de imagem para tensor

trainset = datasets.MNIST('./MNIST_data', download=True, train=True, transform=transform) # Carrega a parte de treino do dataset
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True) # Cria um buffer para pegar os dados por partes

valset = datasets.MNIST('./MNIST_data', download=True, train=False, transform=transform) # Carrega a parte de validação do dataset
valloader = torch.utils.data.DataLoader(valset, batch_size=64, shuffle=True) # Cria um buffer para pegar os dados por partes

dataiter = iter(trainloader)
imagens, etiquetas = dataiter.__next__()
plt.imshow(imagens[0].numpy().squeeze(), cmap='gray_r')

# Conferir o tamanho do tensor que representa cada imagem
print(imagens[0].shape)
# Verificar a dimensão do tensor de cada etiqueta
print(etiquetas[0].shape)


# keras => Inception V3 -> Estrutura da rede do Facebook
class Modelo(nn.Module):
    def __init__(self):
        super(Modelo, self).__init__()
        self.linear1 = nn.Linear(28*28, 128) # Camada de entrada, 784 Neurônios que se ligam a 128
        self.linear2 = nn.Linear(128, 64) # Camada interna 1, 128 Neurônios que se ligam a 64
        self.linear3 = nn.Linear(64, 10) # Camada inerna 2, 64 Neurônios que se ligam a 10
        # Para a camada de saida não é necessário definir pois só precisamos pegar o output da camada interna 2

    def forward(self, X):
        X = F.relu(self.linear1(X)) # Função de ativação da camada de entrada para a camada interna 1
        X = F.relu(self.linear2(X)) # Função de ativação da camada interna 1 para a camada interna 2
        X = self.linear3(X) # Função de ativação da camada interna 2 para a camada de saída, nesse caso, f(x) = x
        return F.log_softmax(X, dim=1) # Dados utilizados para calcular a perda
    
def treino(modelo, trainloader, device):
    otimizador = optim.SGD(modelo.parameters(), lr=0.01, momentum=0.5) # define a politíca dos pesos e da bias
    inicio = time()

    criterio = nn.NLLLoss() # definindo o criterio para calcular a perda
    EPOCHS = 10 # numero de epochs que o algoritimo rodara
    modelo.train() # ativando o modo de treinamento do modelo

    for epoch in range(EPOCHS):
        perda_acumulada = 0 # inicialização da perda acumulada da epoch em questão

        for imagens, etiquetas in trainloader:
            imagens = imagens.view(imagens.shape[0], -1) # convertendo a imagem para vetores de 28 * 28
            otimizador.zero_grad() # zerando os gradientes por conta do ciclo anterior

            output = modelo(imagens.to(device)) # colocando os dados no modelo
            perda_instantanea = criterio(output, etiquetas.to(device)) # calculando a perda da epoch em questão

            perda_instantanea.backward() # back propagation a partir da perda

            otimizador.step() # atualizando os pesos e a bias

            perda_acumulada += perda_instantanea.item() # atualização da perda acumulada
        
        else:
            print("Epoch {} - Perda resultante: {}".format(epoch+1, perda_acumulada/len(trainloader)))

    print("\nTempo de treino em minutos = ",(time()-inicio)/60)
        
def validacao(modelo, valloader, device):
    contas_corretas, conta_todas = 0, 0
    for imagens, etiquetas in valloader:
        for i in range(len(etiquetas)):
            img = imagens[i].view(1, 784)
            # desativar o autograd para acelerar a validação. Grafos computacionais dinâmicos tem um custo alto de processamento
            with torch.no_grad():
                logps = modelo(img.to(device)) # output do modelo em escala logatitmica

            ps = torch.exp(logps) # converte o output para a escala normal (lembrando que é um tensor)
            probab = list(ps.cpu().numpy()[0])
            etiqueta_pred = probab.index(max(probab)) # converte o tensor em um número, no caso, o número que o modelo previu
            etiqueta_certa = etiquetas.numpy()[i]

            # Compara a previsão com o valor correto
            if (etiqueta_certa == etiqueta_pred):
                contas_corretas += 1

            conta_todas += 1

    print("Total de imagens testadas = ", conta_todas)
    print("\nPrecisão do modelo = {}%".format(contas_corretas*100/conta_todas))

# Chamando o modelo
modelo = Modelo()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
modelo.to(device)

# Chamar o treino
Modelo(
    (linear1): Linear(in_features=784, out_features=128, bias=True)
    (linear2): Linear(in_features=128, out_features=64, bias=True)
    (linear3): Linear(in_features=64, out_features=10, bias=True)
)