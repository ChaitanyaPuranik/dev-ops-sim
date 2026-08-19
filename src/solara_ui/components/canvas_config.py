from collections.abc import Callable

from solara_ui.node_registry import (
    CanvasEdge,
    CanvasNode,
)


NODE_WIDTH = 190
NODE_BUTTON_HEIGHT = 72
NODE_SLOT_HEIGHT = 160

CANVAS_COLUMNS = 2

CANVAS_PADDING = 24
HORIZONTAL_GAP = 90
VERTICAL_GAP = 60


def node_position(index: int) -> tuple[int, int]:
    column = index % CANVAS_COLUMNS
    row = index // CANVAS_COLUMNS

    x = (
        CANVAS_PADDING
        + column * (
            NODE_WIDTH
            + HORIZONTAL_GAP
        )
    )

    y = (
        CANVAS_PADDING
        + row * (
            NODE_SLOT_HEIGHT
            + VERTICAL_GAP
        )
    )

    return x, y


def edge_coordinates(
    source_position: tuple[int, int],
    target_position: tuple[int, int],
) -> tuple[int, int, int, int]:
    """
    Calculate arrow endpoints on the boundary of
    source and target node boxes.
    """

    source_x, source_y = source_position
    target_x, target_y = target_position

    source_center_x = (
        source_x + NODE_WIDTH / 2
    )
    source_center_y = (
        source_y + NODE_BUTTON_HEIGHT / 2
    )

    target_center_x = (
        target_x + NODE_WIDTH / 2
    )
    target_center_y = (
        target_y + NODE_BUTTON_HEIGHT / 2
    )

    dx = target_center_x - source_center_x
    dy = target_center_y - source_center_y

    arrow_gap = 8

    # Primarily horizontal connection.
    if abs(dx) >= abs(dy):
        if dx >= 0:
            return (
                source_x + NODE_WIDTH,
                int(source_center_y),
                target_x - arrow_gap,
                int(target_center_y),
            )

        return (
            source_x,
            int(source_center_y),
            target_x + NODE_WIDTH + arrow_gap,
            int(target_center_y),
        )

    # Primarily vertical connection.
    if dy >= 0:
        return (
            int(source_center_x),
            source_y + NODE_BUTTON_HEIGHT,
            int(target_center_x),
            target_y - arrow_gap,
        )

    return (
        int(source_center_x),
        source_y,
        int(target_center_x),
        target_y + NODE_BUTTON_HEIGHT + arrow_gap,
    )


def build_svg(
    nodes: list[CanvasNode],
    edges: list[CanvasEdge],
    canvas_height: int,
) -> str:
    positions = {
        node.id: node_position(index)
        for index, node in enumerate(nodes)
    }

    lines = []

    for edge in edges:
        source_position = positions.get(
            edge.source_id
        )
        target_position = positions.get(
            edge.target_id
        )

        if (
            source_position is None
            or target_position is None
        ):
            continue

        x1, y1, x2, y2 = edge_coordinates(
            source_position,
            target_position,
        )

        lines.append(
            f"""
            <line
                x1="{x1}"
                y1="{y1}"
                x2="{x2}"
                y2="{y2}"
                stroke="#607d8b"
                stroke-width="2.5"
                marker-end="url(#arrowhead)"
            />
            """
        )

    return f"""
    <svg
        width="100%"
        height="{canvas_height}"
        xmlns="http://www.w3.org/2000/svg"
    >
        <defs>
            <marker
                id="arrowhead"
                markerWidth="10"
                markerHeight="10"
                refX="8"
                refY="3"
                orient="auto"
                markerUnits="strokeWidth"
            >
                <path
                    d="M0,0 L0,6 L9,3 z"
                    fill="#607d8b"
                />
            </marker>
        </defs>

        {''.join(lines)}
    </svg>
    """