import solara

@solara.component
def NodePalette():
    with solara.Column(
        style={
            "height": "100%",
            "padding": "16px",
            "border-right": "1px solid #dcdcdc",
            "background": "#fafafa",
        }
    ):
        solara.Markdown("### Nodes")

        solara.Button(
            label="Traffic Generator",
            block=True,
        )

        solara.Button(
            label="Load Balancer",
            block=True,
        )

        solara.Button(
            label="Application Server",
            block=True,
        )

        solara.Button(
            label="Database",
            block=True,
        )