

def load_modules(): 
    import subprocess
    import sys
    import os
    import pandas as pd
    from Bio import Entrez, Medline
    import ssl
    import certifi
    import re
    from pathlib import Path

def load_folders():
    root = os.getcwd()
    folders = {
    "systematic_review": f"{root}/systematic_review",
        "protocol": f"{root}/systematic_review/protocol",
            "prospero": f"{root}/systematic_review/protocol/prospero",
            "cochrane": f"{root}/systematic_review/protocol/cochrane",
        "search_strategy": f"{root}/systematic_review/search_strategy",
            "search_strategy_pubmed": f"{root}/systematic_review/search_strategy/pubmed/",
            "search_strategy_embase": f"{root}/systematic_review/search_strategy/embase/",
            "search_strategy_wos": f"{root}/systematic_review/search_strategy/wos/",
        "search": f"{root}/systematic_review/search",
            "search_pubmed": f"{root}/systematic_review/search/pubmed/",
            "search_embase": f"{root}/systematic_review/search/embase/",
            "search_wos": f"{root}/systematic_review/search/wos/",
        "deduplication": f"{root}/systematic_review/deduplication/",
        "screening": f"{root}/systematic_review/screening/",
            "title_abstract": f"{root}/systematic_review/screening/title_abstract_screening", 
            "pdf": f"{root}/systematic_review/screening/PDF",
            "full_text": f"{root}/systematic_review/screening/full_text_screening", 
    "meta-analysis": f"{root}/meta-analysis",
    "manuscript": f"{root}/manuscript",    
    
    }
    
    for var, f in folders.items():
        directory = Path(f)
        globals()[f"{var}"] = directory
        os.makedirs(directory, exist_ok = True)