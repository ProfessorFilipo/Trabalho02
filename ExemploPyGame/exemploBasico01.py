import pygame
import sys

# Inicializa todos os módulos integrados do PyGame
pygame.init()

# -----------------------------------------------------------------------------
# CONFIGURAÇÕES DA JANELA E CONSTANTES
# -----------------------------------------------------------------------------
LARGURA_TELA = 800
ALTURA_TELA = 600
TITULO = "Python Crash - Introdução ao PyGame"
FPS = 60  # Taxa de atualização (quadros por segundo)

# Definição de cores básicas usando tuplas (Red, Green, Blue)
COR_FUNDO = (30, 41, 59)  # Um tom de azul bem escuro (Slate 800)
COR_RETANGULO = (55, 118, 171)  # Azul clássico da logo do Python

# Cria a janela do jogo com as dimensões especificadas
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption(TITULO)

# Objeto responsável por gerenciar o tempo e limitar a taxa de FPS
relogio = pygame.time.Clock()

# -----------------------------------------------------------------------------
# ESTADO DO PERSONAGEM (VARIÁVEIS DE CONTROLE)
# -----------------------------------------------------------------------------
# Tamanho do nosso quadrado/personagem (largura e altura)
tam_personagem = 50

# Posição inicial centralizada na tela
pos_x = (LARGURA_TELA - tam_personagem) // 2
pos_y = (ALTURA_TELA - tam_personagem) // 2

# Velocidade de movimento (pixels que ele percorrerá por frame)
velocidade = 5

# -----------------------------------------------------------------------------
# CARREGAMENTO DA IMAGEM (COM FALLBACK SE O ARQUIVO NÃO EXISTIR)
# -----------------------------------------------------------------------------
imagem_personagem = None
usa_imagem = False

try:
    # Tentativa de carregar a imagem do disco
    # IMPORTANTE: Os alunos devem colocar um arquivo chamado 'personagem.png' na mesma pasta deste script!
    imagem_original = pygame.image.load("personagem.png")

    # Redimensiona a imagem para que se ajuste perfeitamente ao tamanho do nosso personagem
    imagem_personagem = pygame.transform.scale(imagem_original, (tam_personagem, tam_personagem))
    usa_imagem = True
    print("[INFO] Imagem 'personagem.png' carregada com sucesso!")

except FileNotFoundError:
    # Se a imagem não for encontrada, criamos uma imagem customizada em memória
    # para que o programa continue rodando sem quebrar. Excelente prática de tratamento de erros!
    print("[Aviso] Imagem 'personagem.png' não encontrada. Criando uma textura alternativa em memória...")

    # Criamos uma superfície vazia de tamanho tam_personagem x tam_personagem
    imagem_personagem = pygame.Surface((tam_personagem, tam_personagem), pygame.SRCALPHA)

    # Desenhamos uma bolinha amarela e olhos nela para simular uma carinha simples (pixel-art improvisado)
    pygame.draw.circle(imagem_personagem, (254, 240, 138), (tam_personagem // 2, tam_personagem // 2),
                       tam_personagem // 2)
    pygame.draw.circle(imagem_personagem, (15, 23, 42), (tam_personagem // 3, tam_personagem // 3), 4)  # Olho Esquerdo
    pygame.draw.circle(imagem_personagem, (15, 23, 42), (2 * tam_personagem // 3, tam_personagem // 3),
                       4)  # Olho Direito
    pygame.draw.arc(imagem_personagem, (15, 23, 42),
                    (tam_personagem // 4, tam_personagem // 3, tam_personagem // 2, tam_personagem // 3), 3.14, 0,
                    2)  # Sorriso

    usa_imagem = True

# -----------------------------------------------------------------------------
# LAÇO PRINCIPAL DO JOGO (GAME LOOP)
# -----------------------------------------------------------------------------
rodando = True
while rodando:
    # 1. PROCESSAMENTO DE EVENTOS (Entradas do Usuário de clique único)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # 2. CAPTURA DE TECLAS PRESSIONADAS (Para movimentação contínua e suave)
    teclas = pygame.key.get_pressed()

    # Atualiza a posição com base nas teclas de seta ou WASD
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        pos_x -= velocidade
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        pos_x += velocidade
    if teclas[pygame.K_UP] or teclas[pygame.K_w]:
        pos_y -= velocidade
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        pos_y += velocidade

    # 3. COLISÃO COM AS BORDAS DA TELA (Restringe o jogador dentro dos limites)
    # Impede que o personagem saia pela esquerda ou pela direita
    if pos_x < 0:
        pos_x = 0
    elif pos_x > LARGURA_TELA - tam_personagem:
        pos_x = LARGURA_TELA - tam_personagem

    # Impede que o personagem saia pelo topo ou pela base
    if pos_y < 0:
        pos_y = 0
    elif pos_y > ALTURA_TELA - tam_personagem:
        pos_y = ALTURA_TELA - tam_personagem

    # 4. RENDERIZAÇÃO (Desenho dos elementos na tela)
    # Primeiro, limpamos a tela desenhando uma cor sólida por cima de tudo
    tela.fill(COR_FUNDO)

    # Decidimos o que desenhar com base na presença da imagem
    if usa_imagem:
        # blit desenha uma superfície (imagem_personagem) em uma coordenada (pos_x, pos_y)
        tela.blit(imagem_personagem, (pos_x, pos_y))
    else:
        # Se por algum motivo falhar, desenha o retângulo azul puro padrão
        pygame.draw.rect(tela, COR_RETANGULO, (pos_x, pos_y, tam_personagem, tam_personagem))

    # Atualiza o display da tela física para exibir o que desenhamos na memória
    pygame.display.flip()

    # Controla o tempo de execução do laço para cravar nos 60 FPS desejados
    relogio.tick(FPS)

# Finaliza o PyGame de forma segura e encerra o interpretador do Python
pygame.quit()
sys.exit()