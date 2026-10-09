import pandas as pd
import os
from pathlib import Path

def csv2df(filename):
    import pandas as pd
    import os
    from pathlib import Path
    root = 'G:/My Drive/network_meta-analysis/'
    folders = {"systematic_review": f"{root}/systematic_review",
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
    "data": f"{root}/data",
    "meta-analysis": f"{root}/meta-analysis",
    "manuscript": f"{root}/manuscript"
    }
    
    filename = f"{filename}"
    for var, path in folders.items():
        file = f"{path}/{filename}.csv"
        df = pd.read_csv(file, encoding = "utf-8")
    globals()[f"{filename}"] = df
    df.head()

if __name__ == "__main__":
    csv2df(filename)




   
            