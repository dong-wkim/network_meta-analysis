def requirements():
    requirements = f"""pandas
    numpy
    matplotlib
    seaborn
    biopython
    mermaid-py
    ipywidgets
    google-drive
    ipysheet
    ipydatagrid
    shinywidgets
    altair
    bokeh
    plotly 
    ipyleaflet 
    pydeck==0.8.0
    jupyterlite-pyodide-kernel
    jupyter-book>=2.0
    jupyter_server
    """
    
    with open("./requirements.txt", "w") as f:
        f.write(requirements)

def import_modules():
    import pandas as pd
    import numpy as np
    import matplotlib
    import seaborn as sns
    from Bio import Entrez, Medline
    import mermaid
    import ipywidgets as widgets
    from IPython.display import display
    from IPython.display import HTML
    from IPython.display import Javascript
    import subprocess
    import sys
    import os
    import ssl
    import certifi
    import re
    from pathlib import Path

def structure():
    import re
    root = f"G:/My Drive/network_meta-analysis"
    folders = {
        "systematic_review": f"{root}/systematic_review",
            "protocol": f"{root}/systematic_review/protocol",
                "prospero": f"{root}/systematic_review/protocol/prospero",
                "cochrane": f"{root}/systematic_review/protocol/cochrane",
            "search_strategy": f"{root}/systematic_review/search_strategy",
                "search_strategy_pubmed": f"{root}/systematic_review/search_strategy/pubmed",
                "search_strategy_embase": f"{root}/systematic_review/search_strategy/embase",
                "search_strategy_wos": f"{root}/systematic_review/search_strategy/wos",
            "search": f"{root}/systematic_review/search",
                "search_pubmed": f"{root}/systematic_review/search/pubmed",
                "search_embase": f"{root}/systematic_review/search/embase",
                "search_wos": f"{root}/systematic_review/search/wos",
            "deduplication": f"{root}/systematic_review/deduplication",
            "screening": f"{root}/systematic_review/screening",
                "title_abstract": f"{root}/systematic_review/screening/title_abstract_screening", 
                "pdf": f"{root}/systematic_review/screening/PDF",
                "full_text": f"{root}/systematic_review/screening/full_text_screening", 
        "meta-analysis": f"{root}/meta-analysis",
        "manuscript": f"{root}/manuscript"
    }

    for x, y in folders.items():
        filename = f"{x}"
        filename = filename.replace(r"[\s-]", "_", regex = True)
        path = Path(f"{y}")
        globals()[filename] = path
        #os.makedir(path, exist_ok = True)
        print(filename)

if __name__ == "__main__":
    requirements()
    import_modules()
    structure()