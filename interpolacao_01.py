import glfw 
from OpenGL.GL import * 

a = (-0.5,-0.5) #os ultimos três parâmetros se refere a cor do vértice, caso cor estática
b = (0.5, -0.5)
c = (0, 0.5)    

def init():
    glClearColor(1,1,1,1)#cor de fundo da janela

def render():
    glClear(GL_COLOR_BUFFER_BIT) #limpa o buffer de cor
    
    glPointSize(1)

    glBegin(GL_POINTS) #inicia a construção do triângulo através de pontos 
  
    interacao = 400 #Quantas vezes irá repetir para colorir o triângulo, parecido com geogebra
    
    for alfa in range(0, interacao):
        alfa /= interacao
        for beta in range(0, interacao):
            beta /= interacao
            #considerando que cada ponto possui x,y. (coordenadas 0,1)
            Q = (beta*alfa*b[0]+beta*(1-alfa)*a[0]+(1-beta)*c[0], beta*alfa*b[1]+beta*(1-alfa)*a[1]+(1-beta)*c[1]) #reta Q da interpolação linear entre os vértices a, b e c
            
            glVertex2f(Q[0], Q[1]) #desenha o ponto que irá colorir o triângulo
            
            glColor3f(beta*(1-alfa), alfa*beta, (1-beta)) #rgb dinâmico do triângulo
        
    glEnd() #finaliza a construção do triângulo

def main():
    glfw.init() #inicializa a biblioteca glfw
    window = glfw.create_window(800,600, "Interpolação de Triângulo no OpenGL/GLFW", None, None) #monitor e tela compartilhadas none
    glfw.make_context_current(window) #cria o contexto
    
    init()
    
    while not glfw.window_should_close(window): #roda enquanto não fecha a janela
        glfw.poll_events() #captura eventos
        render()

        glfw.swap_buffers(window) #trabalha com dois buffers
    glfw.terminate()

if __name__ == "__main__":
    main()