import math
from collections.abc import Callable

import solara

from solara_ui.node_registry import (
    CanvasEdge,
    CanvasNode,
)

from solara_ui.components.canvas_config import (
    build_svg, node_position, CANVAS_COLUMNS, 
    CANVAS_PADDING, NODE_SLOT_HEIGHT, VERTICAL_GAP, 
    NODE_WIDTH, NODE_BUTTON_HEIGHT
)


@solara.component
def SimulationCanvas(
    nodes: list[CanvasNode],
    edges: list[CanvasEdge],
    selected_node_id: str | None,
    connecting_from_id: str | None,
    on_select_node: Callable[[str], None],
    on_delete_node: Callable[[str], None],
    on_start_connection: Callable[[str], None],
    on_complete_connection: Callable[[str], None],
    on_cancel_connection: Callable[[], None],
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
            "overflow": "auto",
        }
    ):
        solara.Markdown(
            "### Infrastructure Canvas"
        )

        if not nodes:
            solara.Markdown(
                """
                Select an infrastructure node from the palette
                to add it to the canvas.
                """
            )
            return

        if connecting_from_id is not None:
            source_node = next(
                (
                    node
                    for node in nodes
                    if node.id == connecting_from_id
                ),
                None,
            )

            if source_node is not None:
                solara.Markdown(
                    f"""
                    Connecting from
                    **{source_node.definition.label} #{source_node.id[:6]}**.

                    Select **Connect here** on the destination node.
                    """
                )

        row_count = math.ceil(
            len(nodes) / CANVAS_COLUMNS
        )

        canvas_height = max(
            300,
            (
                CANVAS_PADDING * 2
                + row_count * NODE_SLOT_HEIGHT
                + max(
                    0,
                    row_count - 1,
                ) * VERTICAL_GAP
            ),
        )

        with solara.Column(
            style={
                "position": "relative",
                "height": f"{canvas_height}px",
                "min-width": "520px",
            }
        ):
            # Arrow layer
            svg = build_svg(
                nodes,
                edges,
                canvas_height,
            )

            solara.HTML(
                tag="div",
                unsafe_innerHTML=svg,
                style=(
                    "position:absolute;"
                    "left:0;"
                    "top:0;"
                    "width:100%;"
                    f"height:{canvas_height}px;"
                    "pointer-events:none;"
                    "z-index:0;"
                ),
            )

            # Node layer
            for index, node in enumerate(nodes):
                x, y = node_position(index)

                is_selected = (
                    node.id == selected_node_id
                )

                with solara.Column(
                    gap="4px",
                    style={
                        "position": "absolute",
                        "left": f"{x}px",
                        "top": f"{y}px",
                        "width": f"{NODE_WIDTH}px",
                        "z-index": "1",
                    },
                ):
                    solara.Button(
                        label=(
                            f"{node.definition.label} "
                            f"#{node.id[:6]}"
                        ),
                        on_click=lambda node_id=node.id: (
                            on_select_node(node_id)
                        ),
                        outlined=not is_selected,
                        color=(
                            "primary"
                            if is_selected
                            else None
                        ),
                        style={
                            "width": f"{NODE_WIDTH}px",
                            "height": (
                                f"{NODE_BUTTON_HEIGHT}px"
                            ),
                            "text-transform": "none",
                        },
                    )

                    if connecting_from_id is None:
                        solara.Button(
                            label="Connect from",
                            on_click=(
                                lambda node_id=node.id:
                                on_start_connection(
                                    node_id
                                )
                            ),
                            outlined=True,
                            style={
                                "width": (
                                    f"{NODE_WIDTH}px"
                                ),
                                "text-transform": "none",
                            },
                        )

                    elif connecting_from_id == node.id:
                        solara.Button(
                            label="Cancel connection",
                            on_click=on_cancel_connection,
                            outlined=True,
                            style={
                                "width": (
                                    f"{NODE_WIDTH}px"
                                ),
                                "text-transform": "none",
                            },
                        )

                    else:
                        solara.Button(
                            label="Connect here",
                            on_click=(
                                lambda node_id=node.id:
                                on_complete_connection(
                                    node_id
                                )
                            ),
                            color="primary",
                            style={
                                "width": (
                                    f"{NODE_WIDTH}px"
                                ),
                                "text-transform": "none",
                            },
                        )

                    solara.Button(
                        label="Delete",
                        on_click=(
                            lambda node_id=node.id:
                            on_delete_node(node_id)
                        ),
                        style={
                            "width": f"{NODE_WIDTH}px",
                            "text-transform": "none",
                        },
                    )