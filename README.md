Descrição Geral
Este é um jogo clássico da cobrinha onde o jogador controla uma cobra que se move em um campo de 600x600 pixels. A cobra deve comer maçãs que aparecem aleatoriamente na tela, e cada vez que ela come uma maçã, seu tamanho aumenta. O jogo termina quando a cobra colide com as bordas da janela ou com ela mesma.

Dependências
O código requer a biblioteca Pygame e a biblioteca padrão do Python random

on_grid_random()
python
Copiar código
def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x // 10 * 10, y // 10 * 10)
Gera uma posição aleatória na grade de jogo que é um múltiplo de 10. Isso garante que a maçã apareça em uma posição válida dentro da janela de 600x600 pixels.

collision(c1, c2)
python
Copiar código
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])
Verifica se duas coordenadas c1 e c2 são iguais, ou seja, se houve uma colisão.

Variáveis Globais
UP, RIGHT, DOWN, LEFT: Constantes que representam as direções de movimento da cobra.
screen: A janela de exibição do jogo.
snake: Lista de tuplas representando as partes do corpo da cobra.
snake_skin: Superfície que representa visualmente uma parte da cobra.
my_direction: Variável que guarda a direção atual de movimento da cobra.
clock: Objeto que controla a taxa de atualização do jogo.
maçã_pos: Tupla que guarda a posição da maçã.
maçã: Superfície que representa visualmente a maçã.
Lógica do Jogo
Inicialização:

Inicializa o Pygame.
Configura a janela de exibição.
Cria a cobra e a maçã com suas posições iniciais.
Loop Principal:

Controla a taxa de atualização do jogo com clock.tick(5).
Processa os eventos, como fechar a janela ou pressionar teclas para mudar a direção da cobra.
Verifica a colisão entre a cobra e a maçã, aumentando o tamanho da cobra se necessário.
Atualiza a posição da cobra com base na direção atual.
Redesenha a tela com a nova posição da cobra e da maçã.
Atualiza a exibição.
Eventos de Teclado
K_UP: Muda a direção da cobra para cima.
K_DOWN: Muda a direção da cobra para baixo.
K_LEFT: Muda a direção da cobra para a esquerda.
K_RIGHT: Muda a direção da cobra para a direita.
