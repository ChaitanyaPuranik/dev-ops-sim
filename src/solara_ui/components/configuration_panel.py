from collections.abc import Callable
from dataclasses import fields
from typing import Any

import solara

from solara_ui.node_registry import CanvasNode


@solara.component
def ConfigurationPanel(
    node: CanvasNode | None,
    on_update_config: Callable[[str, str, Any], None],
):
    """
    Displays and edits the configuration of the currently
    selected infrastructure node.
    """

    errors = solara.use_reactive({})

    with solara.Column(
        gap="12px",
        style={
            "height": "100%",
            "padding": "16px",
            "border-left": "1px solid #dcdcdc",
            "background": "#fafafa",
        },
    ):
        solara.Markdown("### Node Configuration")

        if node is None:
            solara.Markdown(
                "Select a node on the canvas to configure it."
            )
            return

        # Selected node information
        solara.Markdown(
            f"""
            **{node.definition.label}**

            Instance: `{node.id[:8]}`
            """
        )

        config = node.config

        # Optional predefined field options stored in NodeDefinition.
        config_options = (
            node.definition.config_options or {}
        )

        def update_field(field_name: str):
            def callback(value):
                if value is None:
                    return

                try:
                    on_update_config(
                        node.id,
                        field_name,
                        value,
                    )

                    # Remove previous validation error.
                    if field_name in errors.value:
                        updated_errors = dict(errors.value)
                        updated_errors.pop(field_name)
                        errors.set(updated_errors)

                except ValueError as exc:
                    errors.set(
                        {
                            **errors.value,
                            field_name: str(exc),
                        }
                    )

            return callback

        for config_field in fields(config):
            field_name = config_field.name
            value = getattr(config, field_name)

            label = (
                field_name
                .replace("_", " ")
                .title()
            )

            options = config_options.get(field_name)

            # Fields with predefined choices
            if options is not None:
                solara.Select(
                    label=label,
                    values=list(options),
                    value=value,
                    on_value=update_field(field_name),
                    style={
                        "width": "100%",
                    },
                )

            # Boolean configuration
            elif isinstance(value, bool):
                solara.Switch(
                    label=label,
                    value=value,
                    on_value=update_field(field_name),
                )

            # Integer configuration
            elif isinstance(value, int):
                solara.InputInt(
                    label=label,
                    value=value,
                    on_value=update_field(field_name),           
                    style={
                        "width": "100%",
                    },
                ),
                if field_name in errors.value:
                    solara.Error(
                        label=errors.value[field_name],
                        dense=True,
                    )

            # Floating-point configuration
            elif isinstance(value, float):
                solara.InputFloat(
                    label=label,
                    value=value,
                    on_value=update_field(field_name),
                    style={
                        "width": "100%",
                    },
                ),
                if field_name in errors.value:
                    solara.Error(
                        label=errors.value[field_name],
                        dense=True,
                    )
                

            # Fallback string configuration
            else:
                solara.InputText(
                    label=label,
                    value=str(value),
                    on_value=update_field(field_name),
                    error=errors.value.get(
                        field_name,
                        False,
                    ),
                    style={
                        "width": "100%",
                    },
                )