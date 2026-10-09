import ipywidgets as widgets
from IPython.display import display, Javascript

def button(label, page):
    button = widgets.Button(description = f"{label}", layout = {"border":"solid 0.5px"})
    output = widgets.Output()
    
    def on_button_clicked(b):
        with output:
            display(Javascript(f"window.location.href = '{page}'"))
            
    button.on_click(on_button_clicked)
    return button