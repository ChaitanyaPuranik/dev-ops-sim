import solara

@solara.component
def ConfigurationPanel():
    with solara.Column(
        style={
            "height": "100%",
            "padding": "16px",
            "border-left": "1px solid #dcdcdc",
            "background": "#fafafa",
        }
    ):
        solara.Markdown("### Selected Node")

        solara.Markdown(
            "Select a node on the canvas to configure it."
        )

        solara.InputText(
            label="Node Name",
            value="",
        )

        solara.InputInt(
            label="Capacity",
            value=1,
        )
