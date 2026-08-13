import solara

@solara.component
def Header():
    with solara.Row(
        style={
            "width": "100%",
            "align-items": "center",
            "justify-content": "space-between",
            "padding": "12px 16px",
            "border-bottom": "1px solid #dcdcdc",
        }
    ):
        solara.Markdown("## DevOps-Sim")

        solara.Button(
            label="Run Simulation",
            color="primary",
        )
