::: {#9cda1c25-a201-4b1a-ae10-b67bc93c7609 .cell .markdown}
# ipywidgets

- [x] Learn ipywidgets
- [x] Create template functions (i.e., factories) for each widget
- [ ] Create key, value dictionary pairs for the custom widgets,
- [ ] Use factories to make interactive HTML forms using `ipyflex`
- [ ] Merge the HTML and Jupyter widgets into one web application.
- [ ] Use `voila` to create web application

<!-- 2026-04-24 I have no idea what the hell I'm doing but it seems to be working. Don't know much about software development at all, pretty much nothing, so will just keep breaking shit until it works. -->
:::

::: {#ce318b0a-b780-49c2-ac47-50cc30772948 .cell .markdown}
%pip install -q ipywidgets

``` python

def f(x):
    y = x + y
    print(y)

def function_name(args):
    result = function
    return result

function_name = lambda args: function
print(function_name)
```
:::

::: {#8fc4b7cc-9cce-4489-a57c-a45020792170 .cell .code}
``` python
```
:::

::: {#e4854b4c-7fd1-4238-9958-b491eee5af9b .cell .code execution_count="21"}
``` python
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from ipyflex import FlexLayout
from IPython.display import display
from enum import Enum
from ipywidgets import AppLayout, Button, Layout
from ipywidgets import Button, Layout, jslink, IntText, IntSlider
```
:::

::: {#58f1e397-1b1c-42e7-a8c2-ba11142eb470 .cell .code execution_count="22"}
``` python
import ipywidgets as widgets
```
:::

::: {#bc056d8a-ca4b-4b0d-a15d-d02deb393181 .cell .markdown}
## Interact
:::

:::::: {#8b38a7f3-7bd8-48f4-8e57-62f4e5c1eb7f .cell .code execution_count="23"}
``` python
# there are two ways, the first is mine, the second is the tutorial's way of using interact

function = lambda value = 7: value + 5
interact(function)

#-----

def function(value = 7):
    result = value + 5
    return result
interact(function)
```

::: {.output .display_data}
``` json
{"model_id":"83fe7acc62e94eb781e52fdc9c46427d","version_major":2,"version_minor":0}
```
:::

::: {.output .display_data}
``` json
{"model_id":"8329c8f9507e4dc891a399408eea5f47","version_major":2,"version_minor":0}
```
:::

::: {.output .execute_result execution_count="23"}
    <function __main__.function(value=7)>
:::
::::::

::: {#d0a2d477-15f9-46d1-8b4c-fb3384c5ca86 .cell .markdown}
# Widgets
:::

::: {#1691d23d-0581-43d7-8b07-3a4ad2d7ef1f .cell .code execution_count="24"}
``` python
import ipywidgets as widgets
from IPython.display import display
```
:::

::: {#e97c2a0a-a27f-4663-9488-f346adbf200e .cell .markdown}
### Basics
:::

:::::::: {#4193bd32-c9a9-4147-b66b-819c530800a4 .cell .code execution_count="25" scrolled="true"}
``` python
a = widgets.IntSlider()
display(a)
#a.close()

a.value = 100
a.keys

b = widgets.Text()
display(b)
b.value = "Enter the search strategy"
b.keys

c = widgets.FloatText()
d = widgets.FloatSlider()
c.step = 0.1
c.readout_format = '0.1f'
d.step = 0.1
d.readout_format = '0.1f'
display(c, d)
mylink = widgets.jslink((a, 'value'), (b, 'value'))
mylink = widgets.jslink((c, 'value'), (d, 'value'))
c.keys
```

::: {.output .display_data}
``` json
{"model_id":"6380b93689e1409691ad5d1a6dcd91a9","version_major":2,"version_minor":0}
```
:::

::: {.output .display_data}
``` json
{"model_id":"711157a8cb3e46c38018a0f080bb333e","version_major":2,"version_minor":0}
```
:::

::: {.output .display_data}
``` json
{"model_id":"b0a03b134a03408da2cde45b7ec7ee3b","version_major":2,"version_minor":0}
```
:::

::: {.output .display_data}
``` json
{"model_id":"e7e81aa5b8ea45868b2409139794bc94","version_major":2,"version_minor":0}
```
:::

::: {.output .execute_result execution_count="25"}
    ['_dom_classes',
     '_model_module',
     '_model_module_version',
     '_model_name',
     '_view_count',
     '_view_module',
     '_view_module_version',
     '_view_name',
     'continuous_update',
     'description',
     'description_allow_html',
     'disabled',
     'layout',
     'step',
     'style',
     'tabbable',
     'tooltip',
     'value']
:::
::::::::

::: {#795c3e2a-6bfc-4a94-8ed7-226fa5a4242f .cell .markdown}
# Events
:::

::: {#29d02a05-d676-4cb2-9134-a19bcef471fd .cell .markdown}
# List
:::

::: {#4128d764-d946-4bd4-a7cd-f68b4ee0b5bc .cell .markdown}
## Numeric widgets
:::

::: {#92987b10-ec0c-47fa-9e8b-7d4438acc0d0 .cell .markdown}
- Sliders
- Progress
- Text
:::

::: {#efed6bc9-4b35-414e-9dec-7c558cd9d18e .cell .markdown}
### Sliders
:::

::: {#09c68f47-bf6b-46c3-90eb-e559a533247f .cell .markdown}
#### IntSlider
:::

:::: {#72e69ab9-6620-47f8-a5c8-4d4755153e7e .cell .code execution_count="5"}
``` python
def intSlider(label: 'Label for slider', value: 'Initial value'):
    return widgets.IntSlider(value=float(value), description = label)

a = widgets.IntSlider()
a.label = "integer slider"
a.value = 0.5
a.max = 100
a.min = 0
a.step = 1
readout=True
readout_format = ".1f"
display(a)
```

::: {.output .display_data}
``` json
{"model_id":"a20f7d3767df4d16955cd85f3a31981b","version_major":2,"version_minor":0}
```
:::
::::

::: {#c2a759ff-39b3-479d-82a7-351ba76c3d7b .cell .markdown}
#### FloatSlider
:::

:::::: {#41f290ea-d5bc-4065-ae15-1d6ff1699b42 .cell .code execution_count="14"}
``` python
def floatSlider(label: 'Label for slider', value: 'Initial value'):
    return widgets.FloatSlider(value=float(value), description = label)

b = widgets.FloatSlider()
b.label = "continuous data"
b.value = 0.50
b.max = 100.00
b.step = 0.01
a.value = 100 * b.value
a.label = "raw mean"
a.description = a.label
display(a)
b.description = "transformed"
display(b)

mean = widgets.jslink((a, 'value'),(b, 'value'))

def floatSlider(value, label, a, b, step):
    return widgets.FloatSlider(
        value = value,
        description = label, 
        min = a,
        max = b,
        step = step)


b = floatSlider(value = 0, label = "mean", a = 0, b = 100, step = 0.1)
c = 
```

::: {.output .display_data}
``` json
{"model_id":"a20f7d3767df4d16955cd85f3a31981b","version_major":2,"version_minor":0}
```
:::

::: {.output .display_data}
``` json
{"model_id":"1812cf687a7443e2b7c44bf03c9ee209","version_major":2,"version_minor":0}
```
:::

::: {.output .display_data}
``` json
{"model_id":"f1e53486932f4b5f848ff2f1f19301bf","version_major":2,"version_minor":0}
```
:::
::::::

::: {#7437cd0c-3398-4b88-9529-fce09a99d762 .cell .markdown}
#### FloatLogitSlider
:::

:::: {#5df3f3cf-5394-4024-a32a-e332eed71b9f .cell .code execution_count="20"}
``` python
def floatLogitSlider(label: 'Label for slider', value: 'Initial value'):
    return widgets.FloatLogSlider(
            value=value,
            base=2.71828,
            min=0, # min exponent of base
            max=1.0, # max exponent of base
            step=0.01, # exponent step
            description= label
        )

c = floatLogitSlider(value = 0, label = "plogit", 
```

::: {.output .error ename="SyntaxError" evalue="incomplete input (1110283165.py, line 11)"}
      Cell In[20], line 11
        c = floatLogitSlider(value = 0, label = "plogit",
                                                          ^
    SyntaxError: incomplete input
:::
::::

:::: {#750d6958-413f-42a2-aba6-10521a7bfa5f .cell .code execution_count="119"}
``` python
logit = floatLogitSlider(label = "logit prop", value = 0.5)
display(logit)
```

::: {.output .display_data}
``` json
{"model_id":"77fd81ddddd54c89b5dfcace95447d50","version_major":2,"version_minor":0}
```
:::
::::

::: {#8b6532a2-84d2-476d-8531-031422ccf56b .cell .markdown}
#### IntRangeSlider
:::

::: {#c7feae85-e011-4f07-b735-f541cbe72b35 .cell .code execution_count="120"}
``` python
def intRangeSlider(label: 'Label for slider', a = 'Min', b = 'Max'):
    return widgets.IntRangeSlider(
        value=[int(a), int(b)],
        min=0,
        max=10,
        step=1,
        description='Test:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d',
    )
```
:::

::: {#684e2a0a-7eeb-4f6e-b599-3c2d287e9c53 .cell .markdown}
#### FloatRangeSlider
:::

::: {#40142a20-c83f-49e8-9a57-3ceb9b5aaefe .cell .code execution_count="121"}
``` python
def floatRangeSlider(label: 'Label for slider', a = "Min", b = "Max"):
    return widgets.FloatRangeSlider(
        value=[float(a), float(b)],
        min=0,
        max=10.0,
        step=0.1,
        description= label,
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
    )
```
:::

::: {#42c8f55c-c122-4577-bbb3-1f0b1a8a52fe .cell .markdown}
### Progress
:::

::: {#c0c175ad-9fc0-49d0-9389-a21f12355c3f .cell .markdown}
#### IntProgress
:::

::: {#e6a0890c-9a84-40cc-8f1b-cf2f80ca001c .cell .code execution_count="122"}
``` python
def intProgress(label: 'Label for slider', value: 'Initial value'):
    return widgets.IntProgress(
        value = int(value),
        min=0,
        max=10,
        description= label,
        bar_style='', # 'success', 'info', 'warning', 'danger' or ''
        style={'bar_color': 'maroon'},
        orientation='horizontal'
    )
```
:::

::: {#22fcafba-a8ff-42a2-b268-ada10009ab18 .cell .markdown}
#### FloatProgress
:::

::: {#890950f7-12d0-43c6-8fb1-c7717c007e60 .cell .code execution_count="123"}
``` python
def floatProgress(label: 'Label for progress', value: 'Initial value'):
    return widgets.FloatProgress(
        value = float(value),
        min=0,
        max=10.0,
        description= label,
        bar_style='info',
        style={'bar_color': '#ffff00'},
        orientation='horizontal'
    )
```
:::

::: {#25982533-c222-4e6c-9eb0-06ca75e8f76a .cell .markdown}
### Text
:::

::: {#e75021fa-bfd6-4c35-b5e1-7e69e05fab0a .cell .markdown}
#### BoundedIntText
:::

::: {#0633ce53-4f3d-49ed-8d3d-20d5b5ab741e .cell .code execution_count="124"}
``` python
def boundedIntText(label: 'Label for slider', value:  'Initial value'):
    return widgets.BoundedIntText(
        value = int(value),
        min=0,
        max=10,
        step=1,
        description= label,
        disabled=False
    )
```
:::

::: {#36eb1b3a-6e82-4323-a939-c8b602623be3 .cell .markdown}
#### BoundedFloatText
:::

::::: {#5a7a5589-2d57-4629-a162-ec7c3570bb62 .cell .code execution_count="35"}
``` python

def boundedFloatText(label: 'Label for slider', value: 'Initial value', a: 'Min', b: 'Max', step):
    return widgets.BoundedFloatText(
        value = float(value),
        min = a,
        max = b,
        step = step,
        description= label,
        disabled=False,
        layout={'width': 'max-content'}
    )

print("Instrumental laxity, side-to-side difference in anteroposterior translation")
bftext = boundedFloatText(value = 0, label = "SSD, mm", a = -10, b = 10, step = 0.01)
display(bftext)
```

::: {.output .stream .stdout}
    Instrumental laxity, side-to-side difference in anteroposterior translation
:::

::: {.output .display_data}
``` json
{"model_id":"f1bd379221b84b4cba87ec0b0d460f3c","version_major":2,"version_minor":0}
```
:::
:::::

::: {#3fb0e0ab-c483-4bb6-a3eb-bc198fce216b .cell .markdown}
#### IntText
:::

::: {#1de26e88-b8da-4f0c-bef4-3abf79543f3c .cell .code execution_count="125"}
``` python
def intText(label: 'Label for slider', value: 'Initial value'):
    return widgets.IntText(
        value = int(value),
        description= label,
        disabled=False
    )
```
:::

::: {#f74c193b-9940-455b-9558-f2f18e60eddc .cell .markdown}
#### FloatText
:::

::: {#58f4fe27-0638-44d6-ab5c-f2f5b92fd35d .cell .code execution_count="126"}
``` python
def floatText(label: 'Label for slider', value: 'Initial value'):
    return widgets.FloatText(
        value = float(value),
        description= label,
        disabled =False
    )

```
:::

::: {#fe102d4c-4bfb-4bb4-91af-1041f1036718 .cell .markdown}
## Boolean widgets
:::

::: {#d9ac168b-c4de-4141-8353-80befb7df78d .cell .markdown}
### ToggleButton
:::

::: {#7ffdd06a-5761-43d4-ba48-ca08354dce7f .cell .code execution_count="127"}
``` python

def toggleButton(value: 'True/False', label: 'Label', icon:'fontawesome names without fa-'):
    return widgets.ToggleButton(
        value = value,
        description = label,
        disabled=False,
        button_style='', # 'success', 'info', 'warning', 'danger' or ''
        tooltip='Description',
        icon = icon # (FontAwesome names without the `fa-` prefix)
    )
```
:::

:::: {#a7b1c354-85d0-4284-8ef5-8e5fb625b8cd .cell .code execution_count="128"}
``` python
display(toggleButton(value = True, label = 'Full-text PDF', icon = 'file-pdf'))
```

::: {.output .display_data}
``` json
{"model_id":"f2051968ee2149908821acfef48878b3","version_major":2,"version_minor":0}
```
:::
::::

::: {#7955c017-8729-4256-882c-1e8b99b6c62a .cell .markdown}
### Checkbox
:::

::: {#b1f105c5-570c-4d74-b5a1-63cf2be64c98 .cell .code execution_count="129"}
``` python
def checkbox(value: 'True/False', label: 'Label for checkbox'):
    return widgets.Checkbox(
        value=value,
        description=label,
        disabled=False,
        indent=False
)
```
:::

:::: {#d7d50359-06d9-4482-b78f-cbb8f049c00d .cell .code execution_count="130"}
``` python
display(checkbox(value = True, label = "Included"))
```

::: {.output .display_data}
``` json
{"model_id":"e016d2c8e1d64b1cad875292eb4e8893","version_major":2,"version_minor":0}
```
:::
::::

::: {#1f2f8bbb-c01d-4df1-a31b-84a2d1ad11e3 .cell .markdown}
### Valid
:::

::: {#b47122e4-f993-4909-8d27-313d2a03c901 .cell .code execution_count="131"}
``` python
def valid(value: 'Initial value', label:'Label for valid'):
    return widgets.Valid(
        value=value,
        description=label,
)
```
:::

:::: {#93030e2d-0b08-4e7d-97a9-f13e579a0fe3 .cell .code execution_count="132"}
``` python
o = valid(value = True, label = "PDF found")
o.keys
display(o)
```

::: {.output .display_data}
``` json
{"model_id":"b877303381d34240a15984157a37d6da","version_major":2,"version_minor":0}
```
:::
::::

::: {#b210508d-d99c-4955-aec8-49ea75fdafa3 .cell .markdown}
## Selection widgets
:::

::: {#42ea2b52-3fcf-4beb-ab07-989ea4a1b795 .cell .markdown}
### Dropdown
:::

::: {#e717838e-57af-49ea-b950-31c0e7287d75 .cell .code execution_count="133"}
``` python
# dropdown of numbers
def dropdown(options: 'List or (label,value) dict', label: 'Label'):
    return widgets.Dropdown(
        options = options,
        value = '2',
        description = label,
        disabled=False
)

# dropdown of words representing numbers 

def dropdown(options: 'List or (label,value) dict', label: 'Label'):
    return widgets.Dropdown(
        options=options,
        value=2,
        description=label
)
```
:::

::: {#e67e1338-4419-4b8d-b91e-72b2cc8e1980 .cell .markdown}
### RadioButtons
:::

::: {#8e3d267c-64f4-4896-b02b-48e2bcaa4d94 .cell .code execution_count="134"}
``` python
def radio(value: 'Default value', options: 'List or (label,value) dict', label: 'Label'):
    return widgets.RadioButtons(
        options=options,
    #   value=value, # Defaults to 'pineapple'
    #   layout={'width': 'max-content'}, # If the items' names are long
        description=label,
        disabled=False
)
```
:::

::: {#8d80ba4d-8bd9-44ff-9ede-e11d7b2f4ca2 .cell .markdown}
*with dynamic layout and very long labels*
:::

::: {#cc54cf51-5685-4e4f-becb-91c5c5a7d725 .cell .code execution_count="135"}
``` python

def dynamicRadio(value: 'Default value', options: 'List or (label,value) dict', label: 'Label'):
    return widgets.Box([
        widgets.RadioButtons(
            options=options,
            value = value,
            description = label,
            layout={'width': 'max-content'})])
```
:::

:::: {#74b2ba00-4634-4c47-b3f4-1297095b40e7 .cell .code execution_count="136"}
``` python
authors = ['First', 'Second', 'Last']

q = dynamicRadio(value = 'First', options =  ['First', 'Second', 'Last'], label = 'Authors: ')
display(q)
```

::: {.output .display_data}
``` json
{"model_id":"70b4776b86504c2f95223a76941fd5e8","version_major":2,"version_minor":0}
```
:::
::::

::: {#cc67d97d-63b9-4baf-950b-3852b29b0bd8 .cell .markdown}
### Select
:::

::: {#073f4f1b-7f7f-4ca4-9d04-34be347167ae .cell .code execution_count="137"}
``` python
def select(value: 'Default', options: 'List or (label,value) dict', label: 'Label'):
    return widgets.Select(
        options=options,
        value=value,
        # rows=10,
        description=label,
        disabled=False
    )
```
:::

:::: {#0d3e7483-ef61-4abc-aebf-8118f516cdb8 .cell .code execution_count="138"}
``` python
s = select(options = ["randomized controlled trial", "non-randomized controlled trial", "prospective cohort study (comparative)", "prospective cohort study (non-comparative)", "retrospective cohort study", "case-control study", "cross-sectional study", "longitudinal study", "case series", "case report"], value = "randomized controlled trial", label = "study design: ")
display(s)
```

::: {.output .display_data}
``` json
{"model_id":"cadcd8c70e59404cb50d1a5a5667fd1d","version_major":2,"version_minor":0}
```
:::
::::

::: {#8c63ff48-eada-4fcd-a30e-4e7b254e298c .cell .markdown}
### SelectionSlider
:::

::: {#8dc18c6c-e24c-473e-bff9-828f361c3874 .cell .code execution_count="139"}
``` python
def selectionSlider(options: 'List or (label,value) dict', value: 'Initial value', label: 'Label'):
    return widgets.SelectionSlider(
        options=options,
        value=value,
        description=label,
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        layout={'height': 'max-content'},
        readout=True
)
```
:::

:::: {#b6b55f35-fabd-4faf-9dad-093c7bf6492c .cell .code execution_count="140"}
``` python
f = selectionSlider(value = 'Normal (0)', options =['Normal (0)', 'Glide (1)', 'Clunk (2)','Gross (3)'], label = "Pivot shift: ")
display(f)
```

::: {.output .display_data}
``` json
{"model_id":"4391d99e370d4ca89d9eb1838cf50e61","version_major":2,"version_minor":0}
```
:::
::::

::: {#fdb58058-c659-4fb1-908b-0bb7365a8648 .cell .markdown}
### SelectionRangeSlider
:::

::: {#7dfef670-eb47-4c5b-82a8-30c863d5ab12 .cell .code execution_count="141"}
``` python
def selectionRangeSlider(a: int, b: int, label='', year=2024):
    import datetime
    dates = [datetime.date(year, i, 1) for i in range(a, b + 1)]
    options = [(i.strftime('%b'), i) for i in dates]
    return widgets.SelectionRangeSlider(
        options=options,
        index=(0, len(options) - 1),
        description=label,
        disabled=False,
    )
```
:::

:::: {#97748980-931b-4a18-ac59-488d8cac4071 .cell .code execution_count="142"}
``` python
f = selectionRangeSlider(a = 1, b = 8, year = 2026, label = "2026")
display(f)
```

::: {.output .display_data}
``` json
{"model_id":"3d4d899e7ff849a1b5c1325bbad80f97","version_major":2,"version_minor":0}
```
:::
::::

::: {#b9a0d2ec-11e2-48ed-8901-127a6761dbfa .cell .markdown}
### ToggleButtons
:::

::: {#0767860c-89a6-4587-8b08-8bea89313375 .cell .code execution_count="143"}
``` python
def toggleButtons(options: 'List of options', label: 'Label for valid'):
    return widgets.ToggleButtons(
        options=options,
        description=label,
        disabled=False,
        button_style= '',# 'success', 'info', 'warning', 'danger' or ''
        tooltips=[],
        #icons=['file'] * 4
)
```
:::

::::: {#8d4ef0b7-0eb3-4440-b865-97fa9db561c5 .cell .code execution_count="144"}
``` python
a = toggleButtons(options = ['A', 'B', 'C', 'D'], label = 'Endpoint grade')
b = toggleButtons(options = ['0', '1+', '2+', '3+'], label = 'Translation grade')

display(a, b)
```

::: {.output .display_data}
``` json
{"model_id":"ef76b01af6334c5dadf960f36c4fbec7","version_major":2,"version_minor":0}
```
:::

::: {.output .display_data}
``` json
{"model_id":"c729efa040564e8e8b361dc0de5f2b86","version_major":2,"version_minor":0}
```
:::
:::::

::: {#d7427cf9-6df2-4782-b29a-fae966db4896 .cell .markdown}
### SelectMultiple
:::

::: {#de0d87b8-a2ea-4301-ad50-0cad5ae36eae .cell .code execution_count="145"}
``` python
def selectMultiple(value: 'Initial value', options: 'List', label: 'Label for valid'):
    return widgets.SelectMultiple(
        options=options,
        value=value,
        #rows=10,
        description=label,
        disabled=False
    )
```
:::

:::: {#74fc8d76-b056-416d-80bf-c3e52f6499d7 .cell .code execution_count="146"}
``` python
m = selectMultiple(value = ["IKDC-SKF", "Pivot shift"], options = ["IKDC-SKF", "Lysholm", "Tegner", "Pivot shift", "Instrumental laxity", "Lachman", "Graft rupture"], label = "Outcome(s)")
display(m)
```

::: {.output .display_data}
``` json
{"model_id":"66caf51c354847c99265df81a866265f","version_major":2,"version_minor":0}
```
:::
::::

::: {#b3e8bb9e-7c22-4ae3-9183-3cad1e613907 .cell .markdown}
## String widgets

Text Textarea Combobox Password Label HTML HTMLMatch Image Button Output
Play Tag widgets TagsInput ColorsInput Float and Integer Input widgets
Date picker Time picker DatetimePicker NaiveDatetimePicker ColorPicker
FileUpload
:::

::: {#9e1c3f99-d57c-48a6-b19c-c6812fed0536 .cell .markdown}
## Container/Layout widgets

Box HBox VBox GridBox Accordion Tabs Stack

## Layout templates

### AppLayout
:::

::: {#89c8e893-1b18-4cda-8e2c-21db85224b61 .cell .markdown}
from ipywidgets import AppLayout, Button, Layout

header_button = create_expanded_button(\'Header\', \'success\')
left_button = create_expanded_button(\'Left\', \'info\') center_button =
create_expanded_button(\'Center\', \'warning\') right_button =
create_expanded_button(\'Right\', \'info\') footer_button =
create_expanded_button(\'Footer\', \'success\')
:::

:::: {#2b8d513b-1353-475c-8a2a-ede46310fe09 .cell .code execution_count="147"}
``` python
def create_expanded_button(description, button_style):
    return Button(description=description, button_style=button_style, layout=Layout(height='100%', width='100%'))

header_button = create_expanded_button('nav', '')
nav_button = create_expanded_button('nav', '')
left_button = create_expanded_button('Left', '')
center_button = create_expanded_button('section', 'info')
right_button = create_expanded_button('aside', '')
footer_button = create_expanded_button('footer', '')

AppLayout(header=header_button,
          nav = nav_button,
          left_sidebar=left_button,
          center=center_button,
          right_sidebar=right_button,
          footer=footer_button)
```

::: {.output .execute_result execution_count="147"}
``` json
{"model_id":"87acae2b48ad4d64becfa08600b93eff","version_major":2,"version_minor":0}
```
:::
::::

::: {#5dcc26bd-03d6-4ab9-9318-c5d793646f7f .cell .markdown}
### 
:::

::: {#ad0a9568-b2d4-4dcc-acfe-fffee0297445 .cell .markdown}
### Styling
:::

::: {#fe772f69-00c5-4df2-a467-f04f2e7a84de .cell .code}
``` python
```
:::

::: {#da615e5e-ca6e-4031-870a-144a0bb28ac6 .cell .markdown}
# ipyflex
:::

:::: {#e29ec9ce-e4de-4a02-87f4-a5891a602a97 .cell .code execution_count="148"}
``` python
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


factories = {"toggleButton": toggleButtons,
             "floatSlider": floatSlider,
            "selectMultiple": selectMultiple,
             "select": select}


dashboard = FlexLayout(tabs,
                       template = 'saved.json',
                       style = {'height': '85vh', 'borderTop': '5px'},
                       header= True,
                       layout_config = {'borderLeft': True, 'borderRight': True, 'enableSection': True},
                       editable = True,
                       factories = factories)

dashboard
```

::: {.output .execute_result execution_count="148"}
``` json
{"model_id":"8026053144264de49014d9d368f26368","version_major":2,"version_minor":0}
```
:::
::::

::: {#4b424096-522e-442a-9d2b-60f06058bd0a .cell .code}
``` python
```
:::
