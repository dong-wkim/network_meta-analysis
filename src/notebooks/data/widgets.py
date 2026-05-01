import ipywidgets as widgets
from ipyflex import FlexLayout
from IPython.display import display

def Slider(value = 0, label = "", min = 0, max = 100, step = 0.1):
    return widgets.FloatSlider(
        value = float(value), 
        description = label,
        min = min, max = max, step = step)
    
def Progress(value = 0, label = "", min = 0, max = 100, step = 0.1, color = "green", orientation = "horizontal"):
    return widgets.FloatProgress(
        value = float(value), 
        description = label, 
        min = min, max = max, step = step,
        style={'bar_color': f"{color}"}, 
        orientation = orientation)

# ID = BoundedIntText
def Text(continuous_update
         description
         description_allow_html
         disabled
         layout
         max
         min
         step
         style
         tabbable
         tooltip
         value

t = widgets.BoundedIntText()
t.keys
print("\n".join(t.keys))



import ipywidgets as widgets
from IPython.display import display
import ipywidgets as widgets
from IPython.display import display

def IntSlider():
    a = widgets.IntSlider()
    display(a, widgets.Output())

def FloatSlider():
    b = widgets.FloatSlider()
    display(b, widgets.Output())

def FloatLogSlider():
    c = widgets.FloatLogSlider()
    display(c, widgets.Output())

def IntRangeSlider():
    e = widgets.IntRangeSlider()
    display(e, widgets.Output())

def FloatRangeSlider():
    f = widgets.FloatRangeSlider()
    display(f, widgets.Output())

def IntProgress():
    g = widgets.IntProgress()
    display(g, widgets.Output())

def FloatProgress():
    h = widgets.FloatProgress()
    display(h, widgets.Output())

def BoundedIntText():
    i = widgets.BoundedIntText()
    display(i, widgets.Output())

def BoundedFloatText():
    j = widgets.BoundedFloatText()
    display(j, widgets.Output())

def IntText():
    k = widgets.IntText()
    display(k, widgets.Output())

def FloatText():
    l = widgets.FloatText()
     display(l, widgets.Output())

def ToggleButton():
    m = widgets.ToggleButton()
    display(m, widgets.Output())

def Checkbox():
    n = widgets.Checkbox()
    display(n, widgets.Output())

def Valid():
    o = widgets.Valid()
    display(o, widgets.Output())

def Dropdown():
    p = widgets.Dropdown()
    display(p, widgets.Output())

def RadioButtons():
    q = widgets.RadioButtons()
    display(q, widgets.Output())

def Select():
    r = widgets.Select()
    isplay(r, widgets.Output())

def SelectionSlider():
    s = widgets.SelectionSlider()
    display(s, widgets.Output())
    
def SelectionRangeSlider():
    t = widgets.SelectionRangeSlider()
    display(t, widgets.Output())
    
def ToggleButtons():
    u = widgets.ToggleButtons()
    display(u, widgets.Output())
    
def SelectMultiple():
    v = widgets.SelectMultiple()
    display(v, widgets.Output())

",".join(a.keys)