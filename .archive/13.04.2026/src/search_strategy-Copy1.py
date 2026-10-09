import ipywidgets as widgets
from IPython.display import display, clear_output

def search_strategy():
    
    entries = []
    
    term_input = widgets.Text(
        placeholder="Search term",
        layout = {"width":"65%"})
    
    field_tag = widgets.Dropdown(
        options=[
            ("MeSH term", "mh"),
            ("Title", "ti"),
            ("Title / Abstract", "tiab"),
            ("Publication Type", "pt"),
        ],
        value="mh",
        layout=widgets.Layout(width="20%")
    )
    
    boolean = widgets.Dropdown(
        options=["OR", "AND", "NOT", ""],
        value="",
        layout=widgets.Layout(width="10%")
    )
    
    filename_input = widgets.Text(
        placeholder="File name",
        layout=widgets.Layout(width="15%")
    )
    
    add_button = widgets.Button(description="Add", button_style = "success")
    delete_button = widgets.Button(description="Delete", button_style = "danger")
    clear_button = widgets.Button(description="Clear", button_style = "warning")
    save_button = widgets.Button(description = "Save", button_style = "info", layout = {"width":"15%"})
    
    output = widgets.Output()
    
    def build_query(entries):
        parts = []
        current_or_group = []
    
        for entry in entries:
            term = entry["term"].strip()
            field = entry["field"]
            op = entry["boolean"]
    
            if not term:
                continue
    
            current_or_group.append(f'"{term}"[{field}]')
    
            if op == "OR":
                continue
    
            parts.append("(" + " OR ".join(current_or_group) + ")")
            current_or_group = []
    
            if op in ("AND", "NOT"):
                parts.append(op)
    
        if current_or_group:
            parts.append("(" + " OR ".join(current_or_group) + ")")
    
        return " ".join(parts)
    
    def refresh_output(message=""):
        with output:
            clear_output()
            if message:
                print(message)
                print()
    
            print("Entries:")
            if entries:
                for i, entry in enumerate(entries, start=1):
                    op_label = entry["boolean"] if entry["boolean"] != "" else "END"
                    #print(f'{i}. "{entry["term"]}" [{entry["field"]}] -> {op_label}')
            else:
                print("[none]")
    
            print("\nCurrent query:")
            query = build_query(entries)
            print(query if query else "[empty]")
    
    def add_entry(_):
        term = term_input.value.strip()
        field = field_tag.value
        op = boolean.value
    
        if not term:
            refresh_output("Please enter a term.")
            return
    
        entries.append({
            "term": term,
            "field": field,
            "boolean": op
        })
    
        term_input.value = ""
        refresh_output(f'Added: "{term}"[{field}] -> {op if op else "END"}')
    
    def delete_last_entry(_):
        if not entries:
            refresh_output("Nothing to delete.")
            return
    
        removed = entries.pop()
        refresh_output(
            f'Removed: "{removed["term"]}"[{removed["field"]}] -> {removed["boolean"] if removed["boolean"] else "END"}'
        )

    def clear_all_entries(_):
        entries.clear()
        refresh_output("Cleared all entries.")
    
    def save_query(_):
        query = build_query(entries)
        filename = filename_input.value.strip() or "default_strategy"
        filepath = f"./data/{filename}.txt"
    
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(query)
    
        #refresh_output(f"Saved query to {filepath}")
    
    
    add_button.on_click(add_entry)
    delete_button.on_click(delete_last_entry)
    clear_button.on_click(clear_all_entries)
    save_button.on_click(save_query)
    
    entry_row = widgets.HBox(
        [filename_input, term_input, field_tag, boolean],
        layout=widgets.Layout(align_items="center", gap="10px")
    )
    
    controls = widgets.VBox([
        entry_row,
        widgets.HBox([add_button, delete_button, clear_button, save_button]),
        output
    ])
    display(controls)

if __name__ == "__main__":
    search_strategy()