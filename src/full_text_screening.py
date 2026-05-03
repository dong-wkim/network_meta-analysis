import ipywidgets as widgets
from IPython.display import display

def full_text_screening():
    included = widgets.Button(
        value = "included", 
        description = "Included", 
        icon = "check", 
        button_style = "success")
    
    excluded = widgets.Button(
        value = "excluded", 
        description = "Excluded", 
        icon = "times", 
        button_style = "danger")
    
    save = widgets.Button(
        value = "Save", 
        description = "Save", 
        icon = "floppy-o",
        button_style = "info")
    
    out = widgets.Output()
    
    reason = widgets.Text(
        value = "",
        placeholder = "Reason for Exclusion",
        layout = {"width":"90%"})
    
    hbox = widgets.HBox([included, excluded, save], layout = {"width":"91%"})
    w = widgets.VBox([hbox, reason])
    display(w)

if __name__ == "__main__":
    full_text_screening()