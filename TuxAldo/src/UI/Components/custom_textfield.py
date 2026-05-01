import flet as ft

class CustomTextField(ft.TextField):
    # Agregamos 'password' (o el nombre que prefieras) al constructor
    def __init__(self, hiden_text, min_l, max_l, multiline=False, password=False):
        super().__init__()
        self.hint_text = hiden_text
        self.multiline = multiline
        self.expand = True
        self.min_lines = min_l
        self.max_lines = max_l
        
        # Configuración de estilo
        self.bgcolor = "#00021d"
        self.border_color = "#1B263B"
        self.focused_border_color = "#1B263B"
        self.color = ft.Colors.WHITE    
        self.height = 80
        self.border_radius = 10

        # Aplicamos las propiedades a la instancia de Flet
        self.can_reveal_password = password

class CustomTextFiNumber(CustomTextField):

    def __init__(self, hiden_text="0", min_l=1, max_l=1):
        super().__init__(        
            hiden_text=hiden_text,
            min_l=min_l,
            max_l=max_l
        )
        self.input_filter = ft.NumbersOnlyInputFilter()
        self.keyboard_type = ft.KeyboardType.NUMBER
        self.text_align = ft.TextAlign.LEFT