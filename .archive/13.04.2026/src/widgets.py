import ipywidgets as widgets
from IPython.display import display
# from src.widgets import Slider, Progress
# import ipywidgets as widgets

def Slider(x = "float", value = 0, label = "", min = 0, max = 100, step = 0.1 ):
    return widgets.FloatSlider(
        value = float(value), 
        description = label,
        min = min, max = max, step = step)

def Progress(value = 0, label = "", min = 0, max = 100, step = 0.1, color = "green", orientation = "horizontal"):
    widgets.FloatProgress(
        value = float(value), 
        description = label, 
        min = min, max = max, step = step,
        style={'bar_color': f"{color}"}, 
        orientation = orientation)

def IntSlider():
    a = widgets.IntSlider()
    return display(a, widgets.Output())

def FloatSlider():
    b = widgets.FloatSlider()
    return display(b, widgets.Output())

def FloatLogSlider():
    c = widgets.FloatLogSlider()
    return display(c, widgets.Output())

def IntRangeSlider():
    e = widgets.IntRangeSlider()
    return display(e, widgets.Output())

def FloatRangeSlider():
    f = widgets.FloatRangeSlider()
    return display(f, widgets.Output())

def IntProgress():
    g = widgets.IntProgress()
    return display(g, widgets.Output())

def FloatProgress():
    h = widgets.FloatProgress()
    return display(h, widgets.Output())

def BoundedIntText():
    i = widgets.BoundedIntText()
    return display(i, widgets.Output())

def BoundedFloatText():
    j = widgets.BoundedFloatText()
    return display(j, widgets.Output())

def IntText():
    k = widgets.IntText()
    return display(k, widgets.Output())

def FloatText():
    l = widgets.FloatText()
    return display(l, widgets.Output())

def ToggleButton():
    m = widgets.ToggleButton()
    return display(m, widgets.Output())

def Checkbox():
    n = widgets.Checkbox()
    return display(n, widgets.Output())

def Valid():
    o = widgets.Valid()
    return display(o, widgets.Output())

def Dropdown():
    p = widgets.Dropdown()
    return display(p, widgets.Output())

def RadioButtons():
    q = widgets.RadioButtons()
    return display(q, widgets.Output())

def Select():
    r = widgets.Select()
    return display(r, widgets.Output())

def SelectionSlider():
    s = widgets.SelectionSlider()
    return display(s, widgets.Output())
    
def SelectionRangeSlider():
    t = widgets.SelectionRangeSlider()
    return display(t, widgets.Output())
    
def ToggleButtons():
    u = widgets.ToggleButtons()
    return display(u, widgets.Output())
    
def SelectMultiple():
    v = widgets.SelectMultiple()
    return display(v, widgets.Output())