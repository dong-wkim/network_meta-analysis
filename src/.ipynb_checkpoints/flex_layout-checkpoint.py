from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from ipyflex import FlexLayout
from IPython.display import display
from enum import Enum

tabs = { "study information": widgets.HTML("<h1>Form 1</h1>"),
          "study arms": widgets.HTML("<h1>Form 2</h1>"),
          "study results": widgets.HTML("<h1>Form 3</h1>"),
          "risk of bias": widgets.HTML("<h1>Form 4</h1>")
        }

def floatSlider(label: 'Label for slider', value: 'Initial value'):
    return widgets.FloatSlider(value=float(value), description = label)



dashboard = FlexLayout(tabs,
                       template = 'saved.json',
                       style = {'height': '85vh', 'borderTop': '5px'},
                       header= True,
                       layout_config = {'borderLeft': True, 'borderRight': True, 'enableSection': True},
                       editable = True)
dashboard