import flet as ft


class CustomButton(ft.Container):
    def __init__(self, text, on_click=None, **kwargs):
        super().__init__(**kwargs)
        self._on_click_callback = on_click
        self.text = text
        self.bgcolor = "#1B263B"
        self.width = 100
        self.height = 40
        self.border_radius = 10
        self.padding = 10
        self.margin = ft.Margin.only(bottom=10)
        self.border = ft.Border.all(1, "#1B263B")
        self.ink = True
        self.shadow = ft.BoxShadow(
            blur_radius=5,
            color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK),
            offset=ft.Offset(0, 2)
        )
        self.content = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text(self.text, color=self.color_select(), size=14)
            ]
        )
        self.on_click = self.handle_click

    def color_select(self):
        if self.text == "Expense":
            return ft.Colors.RED_ACCENT_400
        return ft.Colors.GREEN_ACCENT_400

    def handle_click(self, e):
        if self._on_click_callback:
            self._on_click_callback(self.text)

    def set_active(self, is_active: bool):
        if is_active:
            self.border = ft.Border.all(2, self.color_select())
            self.bgcolor = "#2A3F5F"
        else:
            self.border = ft.Border.all(1, "#1B263B")
            self.bgcolor = "#1B263B"
        self.update()


class TypeSelector(ft.Row):
    def __init__(self, on_change=None, **kwargs):
        super().__init__(**kwargs)
        self._on_selection_change = on_change  # privado para evitar conflictos
        self.expense_button = CustomButton("Expense", on_click=self.handle_selection)
        self.income_button = CustomButton("Income", on_click=self.handle_selection)
        self.controls = [self.expense_button, self.income_button]  # no self.add()

    def handle_selection(self, selected_type):
        self.expense_button.set_active(selected_type == "Expense")
        self.income_button.set_active(selected_type == "Income")
        if self._on_selection_change:
            self._on_selection_change(selected_type)


class DropdownCategory(ft.Container):

    CATEGORIES = {
        "Income": [
            "Nómina / Salario",
            "Honorarios / Freelance",
            "Venta de Productos",
            "Rendimientos / Inversiones",
            "Transferencias Recibidas",
            "Bonos o Premios",
            "Reembolsos",
            "Ganancias Ocasionales",
        ],
        "Expense": [
            "Alquiler / Hipoteca",
            "Servicios Públicos",
            "Mercado",
            "Restaurantes",
            "Snacks",
            "Transporte Público / Plataformas",
            "Gasolina y Peajes",
            "Mantenimiento Vehicular",
            "Seguros y Salud",
            "Farmacia",
            "Suscripciones Digitales",
            "Educación y Cursos",
            "Ropa y Calzado",
            "Hogar (Limpieza y Decoración)",
            "Ocio y Entretenimiento",
            "Pagos de Deuda / Tarjetas",
            "Mascotas",
            "Imprevistos",
        ],
    }

    def __init__(self, on_change=None, **kwargs):
        super().__init__(**kwargs)
        self._on_change_callback = on_change  # privado
        self.bgcolor = "#04002B"
        self.expand = True
        self.border_radius = 20
        self.padding = 15
        self.margin = ft.Margin.only(bottom=10)
        self.border = ft.Border.all(1, "#1B263B")
        self.shadow = ft.BoxShadow(
            blur_radius=15,
            color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK),
            offset=ft.Offset(0, 4)
        )
        self.dropdown = ft.Dropdown(
            options=[],          # vacío hasta que TypeSelector elija un tipo
            expand=True,
            height=40,
            border_radius=10,
            border=ft.Border.all(1, "#1B263B"),
            bgcolor="#1B263B",
            color=ft.Colors.WHITE,
            on_change=self.handle_change  # correcto
        )
        self.content = self.dropdown

    def handle_change(self, e):
        """Se llama cuando el usuario elige una opción."""
        if self._on_change_callback:
            self._on_change_callback(self.dropdown.value)

    def update_categories(self, tipo: str):
        """TypeSelector llama este método cuando cambia el botón."""
        self.dropdown.options = [
            ft.dropdown.Option(cat) for cat in self.CATEGORIES[tipo]
        ]
        self.dropdown.value = None   # resetea a blanco
        self.dropdown.update()       # redibuja el dropdown