import streamlit as st

from dev_ops_sim.st_ui.icons import (
    TRAFFIC_GENERATOR_ICON,
    APPLICATION_SERVER_ICON,
)


def render_topology(
    config: dict,
    result: dict | None,
):

    st.header("Simulation")

    request_label = (
        f"{result['generated']} requests"
        if result
        else "Requests"
    )

    st.html(
        f"""
        <div class="simulation-topology">

            <div class="simulation-node">

                {TRAFFIC_GENERATOR_ICON}

                <h3>Traffic Generator</h3>

                <p>
                    <strong>Rate:</strong>
                    {config["traffic_rate"]:.2f} req/s
                </p>

                <p>
                    <strong>Pattern:</strong>
                    {config["traffic_pattern"]}
                </p>

                <p>
                    <strong>Duration:</strong>
                    {config["traffic_duration"]:.2f}s
                </p>

            </div>


            <div class="request-flow">

                <div class="request-flow-label">
                    {request_label}
                </div>

                <div class="flow-line">
                    <div class="request-dot"></div>
                    <div class="request-dot"></div>
                    <div class="request-dot"></div>
                </div>

            </div>


            <div class="simulation-node">

                {APPLICATION_SERVER_ICON}

                <h3>Application Server</h3>

                <p>
                    <strong>Capacity:</strong>
                    {config["server_capacity"]}
                </p>

                <p>
                    <strong>Processing Time:</strong>
                    {config["processing_time"]:.2f}s
                </p>

            </div>

        </div>
        """
    )

    st.caption(
        "The moving indicators show request direction. "
        "The simulation metrics are produced by the SimPy simulation."
    )