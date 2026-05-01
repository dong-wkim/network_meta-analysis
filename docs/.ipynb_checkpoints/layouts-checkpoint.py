import ipywidgets as widgets
from IPython.display import display

def Nav(words):
    items_layout = widgets.Layout(width = "100%",
                                 border = "solid 0.5px")
    box_layout = widgets.Layout(display = "flex",
                                flex_flow = "column",
                                align_items = "stretch", 
                                align_content = "stretch",
                                width = "100%")
    items = [widgets.Button(description = str(w), layout = items_layout) for w in words]
    w = widgets.HBox(children = items, layout = box_layout)
    out = widgets.Output()
    box = display(w, out)
    return box

a = Nav(words = ['Systematic Review', 'Data Collection', 'Meta-Analysis', 'Manuscript'])