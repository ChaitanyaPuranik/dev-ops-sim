import solara
from collections.abc import Callable
from solara_ui.node_registry import NODE_DEFINITIONS


@solara.component
def NodePalette(
    on_add_node: Callable[[str], None],
):
    with solara.Column(
        gap="8px",
        style={
            "height": "100%",
            "padding": "16px",
            "border-right": "1px solid #dcdcdc",
            "background": "#fafafa",
        },
    ):
        solara.Markdown("### Nodes")

        for node_type, definition in NODE_DEFINITIONS.items():
            solara.Button(
                label=definition.label,
                block=True,
                outlined=True,
                on_click=lambda node_type=node_type: on_add_node(node_type),
                style={
                    "justify-content": "flex-start",
                    "text-transform": "none",
                },
            )