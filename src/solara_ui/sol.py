import solara
from solara_ui.components.configuration_panel import ConfigurationPanel
from solara_ui.components.canvas import SimulationCanvas
from solara_ui.components.metrics_panel import MetricsPanel
from solara_ui.components.node_palette import NodePalette
from solara_ui.components.header import Header

@solara.component
def Page():

    with solara.Column(
        gap="0px",
        style={
            "width": "100%",
            "height": "100vh",
            "overflow": "hidden",
        },
    ):

        # Header
        Header()

        # Main workspace
        with solara.Row(
            gap="0px",
            style={
                "width": "100%",
                "flex": "1",
                "min-height": "0",
            },
        ):

            # Left pane
            with solara.Column(
                style={
                    "width": "220px",
                    "min-width": "220px",
                    "height": "100%",
                }
            ):
                NodePalette()

            # Center canvas
            with solara.Column(
                style={
                    "flex": "1",
                    "height": "100%",
                }
            ):
                SimulationCanvas()

            # Right pane
            with solara.Column(
                style={
                    "width": "280px",
                    "min-width": "280px",
                    "height": "100%",
                }
            ):
                ConfigurationPanel()

        # Bottom metrics pane
        with solara.Column(
            style={
                "width": "100%",
                "min-height": "180px",
            }
        ):
            MetricsPanel()