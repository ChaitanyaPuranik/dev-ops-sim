import solara

@solara.component
def SimulationCanvas():
    with solara.Column(
        style={
            "height": "100%",
            "padding": "16px",
            "background-color": "#ffffff",
            "background-image": (
                "linear-gradient(#eeeeee 1px, transparent 1px), "
                "linear-gradient(90deg, #eeeeee 1px, transparent 1px)"
            ),
            "background-size": "24px 24px",
        }
    ):
        solara.Markdown("### Infrastructure Canvas")

        solara.Markdown(
            """
            Drag infrastructure nodes here.

            This area will later contain draggable nodes,
            connections, arrows, and topology controls.
            """
        )