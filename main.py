import flet as ft
def app (page: ft.Page):
    plain_text = ft.Text(value= 'hello world')
   
        
    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK 
    icon_button = ft.IconButton(icon=ft.Icons.SMART_BUTTON,on_click=change_theme)
    def change (e):
        txt = user_input.value.strip()
        user_input.value = ''

        if txt:
            plain_text.color = None
            plain_text.value = f'hello {txt}'

        else:
            plain_text.value = 'enter corect name' 
            plain_text.color = ft.Colors.RED
              
                  
        

    btn = ft.TextButton('otpravit',on_click=change)
    user_input = ft.TextField(label = 'enter name',on_submit=change)
    page.add(plain_text
             ,user_input
             ,btn,
             icon_button)
ft.app(app)
        

