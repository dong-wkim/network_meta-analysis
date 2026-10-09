def heading(text, level):
    reference = f"{text}".lower().replace(" ", "_")
    heading = f"""
<a id="{reference}"></a>
<h{level} align="center" style="font-family:Times New Roman;font-variant: small-caps;">{text}</h{level}>"""
    from IPython.display import display, HTML
    display(HTML(heading))