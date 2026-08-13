import solara

@solara.component
def MetricsPanel():
    with solara.Column(
        style={
            "width": "100%",
            "padding": "16px",
            "border-top": "1px solid #dcdcdc",
            "background": "#fafafa",
        }
    ):
        solara.Markdown("### Infrastructure Metrics")

        with solara.Row(
            style={
                "width": "100%",
                "gap": "24px",
            }
        ):
            solara.Markdown(
                """
                **Requests Generated**

                0
                """
            )

            solara.Markdown(
                """
                **Requests Completed**

                0
                """
            )

            solara.Markdown(
                """
                **Throughput**

                0 req/s
                """
            )

            solara.Markdown(
                """
                **Errors**

                0
                """
            )
