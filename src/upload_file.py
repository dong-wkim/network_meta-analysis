import ipywidgets as widgets
from IPython.display import display, clear_output

def upload_file():
    uploader = widgets.FileUpload(layout = {"width":"40%"})
    out = widgets.Output()
    
    submit = widgets.Button(description = "Submit", button_style = "info", layout = {"width":"30%"})
    
    hbox = widgets.HBox(children = [uploader, submit])
    #text = widgets.Text(layout = {"width":"70.5%"}, 
    #                    placeholder = "Enter the full search query")
    display(hbox, out)
    
    def read_file():
        import codecs
        uploaded_file = uploader.value[0]
        uploaded_file.content.tobytes()
        inputcodecs.decode(uploaded_file.content, encoding = "utf-8")
    
    submit.on_click(read_file)

if __name__ == "__main__":
    upload_file()