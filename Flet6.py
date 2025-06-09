import flet as ft
def main(page: ft.Page):
    page.bgcolor = ft.Colors.YELLOW_500
    page.title = " R o K e"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    texto1 = ft.Text("CONÓCETE A TI MISMO, Qué eres ?", size=40, color=ft.Colors.PINK_ACCENT) 
    page.add(texto1)
    texto = ft.Text("LA GRAN ENCICLOPEDIA DE ANIMALES", size=50, color=ft.Colors.LIGHT_GREEN)
    page.add(texto)
    def perro(e):
        texto.value="Un perro es un mamífero doméstico perteneciente a la especie Canis lupus familiaris. Es una subespecie del lobo y ha sido domesticado por los seres humanos desde hace miles de años."
        texto.color=ft.Colors.GREEN_ACCENT
        page.update()
    boton = ft.FilledButton(text="perro", on_click=perro)
    
    def gato(e):
        texto.value="Un gato es un mamífero carnívoro domesticado perteneciente a la especie Felis catus. Es uno de los animales de compañía más comunes del mundo, conocido por su comportamiento independiente, agilidad y ternura."
        texto.color=ft.Colors.DEEP_PURPLE_ACCENT_700
        page.update()
    boton1=ft.ElevatedButton(text="gato",on_click=gato)
    
    def loro(e):
        texto.value="Un loro es un ave tropical o subtropical perteneciente al orden Psittaciformes, conocida por su inteligencia, colores vivos y, en muchas especies, su capacidad para imitar sonidos y palabras humanas."
        texto.color=ft.Colors.DEEP_ORANGE_ACCENT_700
        page.update()
    btn=ft.ElevatedButton("loro", on_click=loro)
    def ardilla(e):
        texto.value="Una ardilla es un mamífero roedor perteneciente a la familia Sciuridae, conocido por su agilidad, su cola esponjosa y su costumbre de recolectar nueces y semillas."
        texto.color=ft.Colors.CYAN_800
        page.update()
    btn1=ft.ElevatedButton("ardilla",on_click=ardilla)
    def pato(e):
        texto.value="Un pato es un ave acuática con pico ancho, patas con membranas para nadar y plumas impermeables. Vive cerca del agua, se alimenta de plantas e insectos, y es buen nadador y volador."
        texto.color=ft.Colors.BLUE_GREY_300
        page.update()
    btn2=ft.FilledButton("pato",on_click=pato)
    def delfin(e):
        texto.value="Un delfín es un mamífero marino inteligente, perteneciente a la familia de los cetáceos. Vive en océanos y algunos ríos, respira aire por un orificio en la cabeza (espiráculo), y se comunica mediante sonidos y silbidos. Son sociables, rápidos nadadores y se alimentan de peces y calamares."
        texto.color=ft.Colors.PINK_700
        page.update()
    btn3=ft.FilledButton("delfin", on_click=delfin)
    def puerco (e):
        texto.value="Un puerco (también llamado cerdo) es un mamífero doméstico de cuerpo robusto, piel gruesa y hocico alargado, criado principalmente para el consumo de su carne (como el cerdo, jamón o tocino). Es omnívoro, inteligente y muy adaptable. Su nombre científico es Sus scrofa domestica."
        texto.color=ft.Colors.PURPLE_300
        page.update()
    btn4=ft.ElevatedButton("cerdo",on_click=puerco)
    def tiñosa(e):
        texto.value="Una tiñosa es un nombre común para algunas aves de la familia de las golondrinas o aviones, especialmente en América Latina. Son aves pequeñas, ágiles y de vuelo rápido, que suelen vivir cerca del agua o en áreas abiertas, donde cazan insectos en el aire."
        texto.color=ft.Colors.ORANGE_500
        page.update()
    btn5=ft.ElevatedButton("tiñosa",on_click=tiñosa)
    def camello(e):
        texto.value="Un camello es un mamífero grande adaptado a vivir en el desierto. Tiene jorobas en la espalda donde almacena grasa, que le sirve como reserva de energía. Es capaz de aguantar mucho tiempo sin agua y soportar altas temperaturas. Se usa como animal de carga y transporte en zonas áridas."
        texto.color=ft.Colors.LIGHT_BLUE_ACCENT_100
        page.update()
    btn6=ft.ElevatedButton("camello", on_click=camello)
    def caballo(e):
        texto.value="Un caballo es un mamífero herbívoro domesticado, conocido por su fuerza, velocidad y elegancia. Tiene cuatro patas, crin, cola larga y cascos. Ha sido usado por el ser humano para transporte, trabajo y deporte. Su nombre científico es Equus ferus caballus."
        texto.color=ft.Colors.BLUE_GREY_900
        page.update()
    btn7=ft.FilledButton("caballo",on_click=caballo)

    una_columna = ft.Row(
        controls=[boton, boton1, btn, btn1, btn2],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15)
    otra_columna = ft.Row(
        controls=[btn3, btn4, btn5, btn6, btn7],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15)
    page.add(una_columna, otra_columna)
    txt = ft.Text("Y UDS LO QUE QUIEREN ES !!!", size=60, color=ft.Colors.BLUE_ACCENT_700,
    opacity = 0,
    animate_opacity = 300,
    animate_size = 300
    )
    
    def der(e):
        txt.value="un gato voladorrrrrrr"
        txt.opacity = 1
        txt.size = 130
        txt.color=ft.Colors.ORANGE_800
        
        page.update()
    btn10=ft.FilledButton("que soy?", on_click=der, style=ft.ButtonStyle(text_style=ft.TextStyle(size=50)))
    page.add(btn10, txt)
    def der1(e):
        txt.value="soy una ola y mi amor llegó a tu vida......como una ola ;)"
        txt.opacity=1
        txt.size=100
        txt.color=ft.Colors.BLUE_ACCENT_700
        page.update()
    btn11=ft.FilledButton("y también !?", on_click=der1, style=ft.ButtonStyle(text_style=ft.TextStyle(size=40)))
    page.add(btn11)
        
    
    
    
ft.app(target=main)



    