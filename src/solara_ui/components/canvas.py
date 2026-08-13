import solara
from collections.abc import Callable
from solara_ui.node_registry import CanvasNode


@solara.component
def SimulationCanvas(
    nodes: list[CanvasNode],
    selected_node_id: str | None,
    on_select_node: Callable[[str], None],
    on_delete_node: Callable[[str], None],

):
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

        if not nodes:
            solara.Markdown(
                """
                Select an infrastructure node from the palette
                to add it to the canvas.
                """
            )
            return

        with solara.Row(
            style={
                "flex-wrap": "wrap",
                "align-content": "flex-start",
                "gap": "16px",
            }
        ):
            for node in nodes:
                is_selected = node.id == selected_node_id

                with solara.Column(
                    style={
                        "width": "190px",
                        "gap": "4px",
                    }
                ):
                    # Node button
                    solara.Button(
                        label=(
                            f"{node.definition.label} "
                            f"#{node.id[:6]}"
                        ),
                        on_click=lambda node_id=node.id: (
                            on_select_node(node_id)
                        ),
                        outlined=not is_selected,
                        color="primary" if is_selected else None,
                        style={
                            "width": "190px",
                            "height": "72px",
                            "text-transform": "none",
                        },
                    )

                    # Delete button
                    solara.Button(
                        label="Delete",
                        on_click=lambda node_id=node.id: (
                            on_delete_node(node_id)
                        ),
                        style={
                            "width": "190px",
                            "text-transform": "none",
                        },
                    )