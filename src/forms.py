import ipywidgets as widgets
from IPython.display import display, HTML, Javascript
import pandas as pd


def forms():
    reports = pd.read_csv("https://raw.githubusercontent.com/dong-wkim/network_meta-analysis/31a9070ff303d8df83f2ad164b4331f8465a7e6d/systematic_review/screening/pdf/pdf.csv", encoding = "utf-8")
    reports.head()
    reports["id"] = range(1, len(reports)+1)
    
    df = pd.DataFrame(columns = ["id", "study", "study_design", "level_evidence", "subgroup(s)", "outcome(s)", "arm(s)"])
    df["id"] = reports["id"]
    df["study"] = reports["study"]
    df = df.fillna("")
    df.head()

    a = widgets.BoundedIntText(description = "ID", layout = {"width":"50%"})
    b = widgets.HTML(description = "study", value = "")
    l = widgets.Dropdown(description = "study design", options = ["",
        "Randomized controlled trial", 
        "Non-randomized controlled trial",
        "Prospective cohort study",
        "Retrospective cohort study",
        "Case-control study",
        "Longitudinal study",
        "Cross-sectional study",
        "Case series",
        "Case report",
        "Review"], value = "",layout = {"width":"50%"})
    
    m = widgets.SelectMultiple(options = [
        'BPTB', 
        'HT', 
        'QT', 
        'PLT', 
        'AT', 
        'TA'], value = ["BPTB"], description = "subgroup(s)", layout = {"width": "50%"})
    
    
    n = widgets.Dropdown(options = [
        '',
        'single-arm',
        'two-arm',
        'multi-arm'], value = "", description = "arm(s)")
    
    o = widgets.SelectMultiple(options = [
        '',
        'IKDC subjective',
        'Lysholm',
        'Tegner',
        'Instrumental laxity',
        'Pivot shift',
        'Lachman',
        'Graft rupture'
    ], value = ("",), description = "outcome(s)")
                               
    
    save = widgets.Button(description="Save", button_style="info", icon = "save")
    out = widgets.Output()
    
    columns = ["study_design", "subgroup(s)", "outcome(s)", "arm(s)"]
    for col in columns:
        if col not in df.columns:
            df[col] = ""
    
    def save_values(change):    
        df.loc[df["id"] == a.value, "study"] = b.value
        df.loc[df["id"] == a.value, "study_design"] = l.value
        df.loc[df["id"] == a.value, "subgroup(s)"] = ", ".join(m.value)
        df.loc[df["id"] == a.value, "arm(s)"] = n.value
        df.loc[df["id"] == a.value, "outcome(s)"] = o.value
        df.loc[df["id"] == a.value, "level_evidence"] = p.value
    
        with out:
            out.clear_output()
            print(f"Saved values for ID {a.value}")
    
    
    display(
        a,
        b,
        l,
        m,
        n,
        o,
        save,
        out
    )
    
    def update_study(change):
        row = df.loc[df["id"] == a.value]
    
        if not row.empty:
            b.value = str(row["study"].iloc[0])
        else:
            b.value = ""
    
    l.observe(update_study, names="value")
    m.observe(update_study, names="value")
    n.observe(update_study, names="value")
    o.observe(update_study, names="value")
    p.observe(update_study, names="value")
    
    save.on_click(save_values)
    
if __name__ == "__main__":
    forms()