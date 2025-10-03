import random

def random_walk_inteiro(numero_de_passos):
    """
    Gera uma caminhada aleatória (random walk) unidimensional com passos inteiros.

    Args:
        numero_de_passos (int): O número total de passos a serem dados na caminhada.

    Returns:
        list: Uma lista de inteiros representando a posição a cada passo.
    """
    posicao = 0
    caminhada = [posicao]  # A lista 'caminhada' começa com a posição inicial

    for _ in range(numero_de_passos):
        # Escolhe aleatoriamente -1 ou 1
        passo = random.choice([-1, 1])
        
        # Atualiza a posição somando o passo
        posicao += passo
        
        # Adiciona a nova posição à lista da caminhada
        caminhada.append(posicao)
        
    return caminhada

# --- Exemplo de Uso ---
if __name__ == "__main__":
    # Define o número de passos para a simulação
    passos = 100
    
    # Gera a caminhada aleatória
    trajetoria = random_walk_inteiro(passos)
    
    print(f"Simulando uma caminhada aleatória de {passos} passos.")
    print("Trajetória:")
    print(trajetoria)

    # Para visualizar melhor, você pode instalar a biblioteca matplotlib:
    # pip install matplotlib
    try:
        import matplotlib.pyplot as plt
        
        plt.figure(figsize=(10, 6))
        plt.plot(trajetoria)
        plt.title(f'Random Walk de {passos} Passos')
        plt.xlabel('Número do Passo')
        plt.ylabel('Posição')
        plt.grid(True)
        plt.show()

    except ImportError:
        print("\nPara visualizar o gráfico da caminhada, instale a biblioteca matplotlib:")
        print("pip install matplotlib")