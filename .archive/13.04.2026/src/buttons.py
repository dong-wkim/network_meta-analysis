import ipywidgets as widgets
from IPython.display import display
from IPython.display import HTML

def Button(label, page):
    return widgets.HTML(value = f"<a href='{page}' style='display:inline-block; border: solid 0.5px gray; padding: 6px 10px; margin: 3px; text-decoration: none; color: black; border-radius: 4px; background-color: #f7f7f7;'>{label}</a>")


if __name__ == "__main__":
    Button()