import ipywidgets as widgets
from IPython.display import display

def Nav(words):
    items_layout = widgets.Layout(width = "100%")
    box_layout = widgets.Layout(display = "flex",
                                flex_flow = "row",
                                align_items = "stretch", 
                                align_content = "stretch",
                                border = "solid",
                                width = "100%")
    items = [widgets.Button(description = str(w), layout = items_layout) for w in words]
    box = widgets.Box(children = items, layout = box_layout)
    display(box)
    return display(Nav(words = ["id"]))

    
