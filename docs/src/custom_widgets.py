# flexbox custom widget for calling either VBox or Hbox with the layout dimensions and styling saved for consistency

# words = list of words to turn into buttons
# axis = either horizontal flex or vertical, then add option for staggering both for centering

def flexbox(words, axis = "row"):
    items_layout = widgets.Layout(width = "100%")
    box_layout = widgets.Layout(display = "flex",
                                flex_flow = axis,
                                align_items = "stretch", 
                                align_content = "stretch",
                                width = "100%")
    items = [widgets.Button(description = str(w), layout = items_layout, border = "solid") for w in words]
    box = widgets.Box(children = items, layout = box_layout)
    display(box)

def HBox(*pargs, **kwargs):
    box = widgets.Box(*pargs, **kwargs)
    box.layout.display = 'flex'
    box.layout.align_items = 'stretch'
    return box
                       
def VBox(*pargs, **kwargs):
    box = widgets.Box(*pargs, **kwargs)
    box.layout.display = "flex"
    box.layout.flex_flow = "column"
    box.layout.align_items = "stretch"
    return box

def Flexbox(*pargs, **kwargs):
    box = widgets.Box(*pargs, **kwargs)
    box.layout.display = "flex"
    box.layout.flex_flow = "center"
    return box
