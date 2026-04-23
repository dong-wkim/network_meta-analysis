# ipywidgets

- ☒ Learn ipywidgets
- ☒ Create template functions (i.e., factories) for each widget
- ☐ Create key, value dictionary pairs for the custom widgets,
- ☐ Use factories to make interactive HTML forms using `ipyflex`
- ☐ Merge the HTML and Jupyter widgets into one web application.
- ☐ Use `voila` to create web application

<!-- 2026-04-24 I have no idea what the hell I'm doing but it seems to be working. Don't know much about software development at all, pretty much nothing, so will just keep breaking shit until it works. -->

%pip install -q ipywidgets


    def f(x):
        y = x + y
        print(y)

    def function_name(args):
        result = function
        return result

    function_name = lambda args: function
    print(function_name)

    from ipywidgets import interact, interactive, fixed, interact_manual
    import ipywidgets as widgets
    from ipyflex import FlexLayout
    from IPython.display import display
    from enum import Enum
    from ipywidgets import AppLayout, Button, Layout
    from ipywidgets import Button, Layout, jslink, IntText, IntSlider

    import ipywidgets as widgets

## Interact

    # there are two ways, the first is mine, the second is the tutorial's way of using interact

    function = lambda value = 7: value + 5
    interact(function)

    #-----

    def function(value = 7):
        result = value + 5
        return result
    interact(function)

    {"model_id":"83fe7acc62e94eb781e52fdc9c46427d","version_major":2,"version_minor":0}

    {"model_id":"8329c8f9507e4dc891a399408eea5f47","version_major":2,"version_minor":0}

    <function __main__.function(value=7)>

# Widgets

    import ipywidgets as widgets
    from IPython.display import display

### Basics

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

    {"model_id":"6380b93689e1409691ad5d1a6dcd91a9","version_major":2,"version_minor":0}

    {"model_id":"711157a8cb3e46c38018a0f080bb333e","version_major":2,"version_minor":0}

    {"model_id":"b0a03b134a03408da2cde45b7ec7ee3b","version_major":2,"version_minor":0}

    {"model_id":"e7e81aa5b8ea45868b2409139794bc94","version_major":2,"version_minor":0}

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

# Events

# List

## Numeric widgets

- Sliders
- Progress
- Text

### Sliders

#### IntSlider

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

    {"model_id":"a20f7d3767df4d16955cd85f3a31981b","version_major":2,"version_minor":0}

#### FloatSlider

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

    {"model_id":"a20f7d3767df4d16955cd85f3a31981b","version_major":2,"version_minor":0}

    {"model_id":"1812cf687a7443e2b7c44bf03c9ee209","version_major":2,"version_minor":0}

    {"model_id":"f1e53486932f4b5f848ff2f1f19301bf","version_major":2,"version_minor":0}

#### FloatLogitSlider

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

      Cell In[20], line 11
        c = floatLogitSlider(value = 0, label = "plogit",
                                                          ^
    SyntaxError: incomplete input

    logit = floatLogitSlider(label = "logit prop", value = 0.5)
    display(logit)

    {"model_id":"77fd81ddddd54c89b5dfcace95447d50","version_major":2,"version_minor":0}

#### IntRangeSlider

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

#### FloatRangeSlider

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

### Progress

#### IntProgress

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

#### FloatProgress

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

### Text

#### BoundedIntText

    def boundedIntText(label: 'Label for slider', value:  'Initial value'):
        return widgets.BoundedIntText(
            value = int(value),
            min=0,
            max=10,
            step=1,
            description= label,
            disabled=False
        )

#### BoundedFloatText


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

    Instrumental laxity, side-to-side difference in anteroposterior translation

    {"model_id":"f1bd379221b84b4cba87ec0b0d460f3c","version_major":2,"version_minor":0}

#### IntText

    def intText(label: 'Label for slider', value: 'Initial value'):
        return widgets.IntText(
            value = int(value),
            description= label,
            disabled=False
        )

#### FloatText

    def floatText(label: 'Label for slider', value: 'Initial value'):
        return widgets.FloatText(
            value = float(value),
            description= label,
            disabled =False
        )

## Boolean widgets

### ToggleButton


    def toggleButton(value: 'True/False', label: 'Label', icon:'fontawesome names without fa-'):
        return widgets.ToggleButton(
            value = value,
            description = label,
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Description',
            icon = icon # (FontAwesome names without the `fa-` prefix)
        )

    display(toggleButton(value = True, label = 'Full-text PDF', icon = 'file-pdf'))

    {"model_id":"f2051968ee2149908821acfef48878b3","version_major":2,"version_minor":0}

### Checkbox

    def checkbox(value: 'True/False', label: 'Label for checkbox'):
        return widgets.Checkbox(
            value=value,
            description=label,
            disabled=False,
            indent=False
    )

    display(checkbox(value = True, label = "Included"))

    {"model_id":"e016d2c8e1d64b1cad875292eb4e8893","version_major":2,"version_minor":0}

### Valid

    def valid(value: 'Initial value', label:'Label for valid'):
        return widgets.Valid(
            value=value,
            description=label,
    )

    o = valid(value = True, label = "PDF found")
    o.keys
    display(o)

    {"model_id":"b877303381d34240a15984157a37d6da","version_major":2,"version_minor":0}

## Selection widgets

### Dropdown

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

### RadioButtons

    def radio(value: 'Default value', options: 'List or (label,value) dict', label: 'Label'):
        return widgets.RadioButtons(
            options=options,
        #   value=value, # Defaults to 'pineapple'
        #   layout={'width': 'max-content'}, # If the items' names are long
            description=label,
            disabled=False
    )

*with dynamic layout and very long labels*


    def dynamicRadio(value: 'Default value', options: 'List or (label,value) dict', label: 'Label'):
        return widgets.Box([
            widgets.RadioButtons(
                options=options,
                value = value,
                description = label,
                layout={'width': 'max-content'})])

    authors = ['First', 'Second', 'Last']

    q = dynamicRadio(value = 'First', options =  ['First', 'Second', 'Last'], label = 'Authors: ')
    display(q)

    {"model_id":"70b4776b86504c2f95223a76941fd5e8","version_major":2,"version_minor":0}

### Select

    def select(value: 'Default', options: 'List or (label,value) dict', label: 'Label'):
        return widgets.Select(
            options=options,
            value=value,
            # rows=10,
            description=label,
            disabled=False
        )

    s = select(options = ["randomized controlled trial", "non-randomized controlled trial", "prospective cohort study (comparative)", "prospective cohort study (non-comparative)", "retrospective cohort study", "case-control study", "cross-sectional study", "longitudinal study", "case series", "case report"], value = "randomized controlled trial", label = "study design: ")
    display(s)

    {"model_id":"cadcd8c70e59404cb50d1a5a5667fd1d","version_major":2,"version_minor":0}

### SelectionSlider

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

    f = selectionSlider(value = 'Normal (0)', options =['Normal (0)', 'Glide (1)', 'Clunk (2)','Gross (3)'], label = "Pivot shift: ")
    display(f)

    {"model_id":"4391d99e370d4ca89d9eb1838cf50e61","version_major":2,"version_minor":0}

### SelectionRangeSlider

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

    f = selectionRangeSlider(a = 1, b = 8, year = 2026, label = "2026")
    display(f)

    {"model_id":"3d4d899e7ff849a1b5c1325bbad80f97","version_major":2,"version_minor":0}

### ToggleButtons

    def toggleButtons(options: 'List of options', label: 'Label for valid'):
        return widgets.ToggleButtons(
            options=options,
            description=label,
            disabled=False,
            button_style= '',# 'success', 'info', 'warning', 'danger' or ''
            tooltips=[],
            #icons=['file'] * 4
    )

    a = toggleButtons(options = ['A', 'B', 'C', 'D'], label = 'Endpoint grade')
    b = toggleButtons(options = ['0', '1+', '2+', '3+'], label = 'Translation grade')

    display(a, b)

    {"model_id":"ef76b01af6334c5dadf960f36c4fbec7","version_major":2,"version_minor":0}

    {"model_id":"c729efa040564e8e8b361dc0de5f2b86","version_major":2,"version_minor":0}

### SelectMultiple

    def selectMultiple(value: 'Initial value', options: 'List', label: 'Label for valid'):
        return widgets.SelectMultiple(
            options=options,
            value=value,
            #rows=10,
            description=label,
            disabled=False
        )

    m = selectMultiple(value = ["IKDC-SKF", "Pivot shift"], options = ["IKDC-SKF", "Lysholm", "Tegner", "Pivot shift", "Instrumental laxity", "Lachman", "Graft rupture"], label = "Outcome(s)")
    display(m)

    {"model_id":"66caf51c354847c99265df81a866265f","version_major":2,"version_minor":0}

## String widgets

Text Textarea Combobox Password Label HTML HTMLMatch Image Button Output
Play Tag widgets TagsInput ColorsInput Float and Integer Input widgets
Date picker Time picker DatetimePicker NaiveDatetimePicker ColorPicker
FileUpload

## Container/Layout widgets

Box HBox VBox GridBox Accordion Tabs Stack

## Layout templates

### AppLayout

from ipywidgets import AppLayout, Button, Layout

header\_button = create\_expanded\_button('Header', 'success')
left\_button = create\_expanded\_button('Left', 'info') center\_button =
create\_expanded\_button('Center', 'warning') right\_button =
create\_expanded\_button('Right', 'info') footer\_button =
create\_expanded\_button('Footer', 'success')

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

    {"model_id":"87acae2b48ad4d64becfa08600b93eff","version_major":2,"version_minor":0}

### 

### Styling

# ipyflex

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

    {"model_id":"8026053144264de49014d9d368f26368","version_major":2,"version_minor":0}
