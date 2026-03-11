import flet as ft
from typing import List, Union

class ScrollableCardList(ft.Container):
    """
    Una clase única para manejar cualquier tipo de lista desplazable de tarjetas.
    """
    def __init__(self,  cards: List[ft.Container] = None):
        super().__init__()
        self.expand = True
        self.padding = 0

        
        
        # El contenedor interno que realmente hace el scroll
        self.scroll_area = ft.Column(
            controls=cards if cards else [],
            scroll=ft.ScrollMode.HIDDEN,  # Scroll suave
            expand=True,
            spacing=5,  # Espacio consistente entre tarjetas
        )
        

        # Estructura visual de la lista
        self.content = ft.Column(
            controls=[
                ft.Divider(height=1, color="#1B263B"),
                self.scroll_area # Aquí viven las tarjetas
            ],
            expand=True
        )

    def add_card(self, card: ft.Container):
        """Añade una nueva tarjeta a la lista dinámicamente"""
        self.scroll_area.controls.append(card)
        self.scroll_area.update()

    def replace_cards(self, new_cards: List[ft.Container]):
        """Reemplaza todas las tarjetas actuales por un set nuevo"""
        self.scroll_area.controls = new_cards
        self.scroll_area.update()