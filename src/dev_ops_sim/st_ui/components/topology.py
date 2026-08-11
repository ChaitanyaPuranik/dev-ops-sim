import streamlit as st

from dev_ops_sim.st_ui.icons import (
    TRAFFIC_GENERATOR_ICON,
    LOAD_BALANCER_ICON,
    APPLICATION_SERVER_ICON,
    DATABASE_ICON,
)


def render_topology(
    config: dict,
    result: dict | None,
):

    st.header("Simulation")

    traffic_to_balancer = (
        f"{result['generated']} requests"
        if result
        else "Requests"
    )

    balancer_to_server = (
        f"{result['balancer_forwarded']} forwarded"
        if result
        else "Forwarded"
    )

    server_to_database = (
        f"{result['completed']} processed"
        if result
        else "Processed"
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
                    {traffic_to_balancer}
                </div>

                <div class="flow-line">
                    <div class="request-dot"></div>
                    <div class="request-dot"></div>
                    <div class="request-dot"></div>
                </div>

            </div>


            <div class="simulation-node">

                {LOAD_BALANCER_ICON}

                <h3>Load Balancer</h3>

                <p>
                    <strong>Algorithm:</strong>
                    {config["load_balancer_algorithm"]}
                </p>

                <p>
                    <strong>Received:</strong>
                    {result["balancer_received"] if result else "-"}
                </p>

                <p>
                    <strong>Forwarded:</strong>
                    {result["balancer_forwarded"] if result else "-"}
                </p>

            </div>


            <div class="request-flow">

                <div class="request-flow-label">
                    {balancer_to_server}
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


            <div class="request-flow">

                <div class="request-flow-label">
                    {server_to_database}
                </div>

                <div class="flow-line">
                    <div class="request-dot"></div>
                    <div class="request-dot"></div>
                    <div class="request-dot"></div>
                </div>

            </div>


            <div class="simulation-node">

                {DATABASE_ICON}

                <h3>Database</h3>

                <p>
                    <strong>Capacity:</strong>
                    {config["database_capacity"]}
                </p>

                <p>
                    <strong>Query Time:</strong>
                    {config["database_query_time"]:.2f}s
                </p>

                <p>
                    <strong>Completed:</strong>
                    {result["database_completed"] if result else "-"}
                </p>

            </div>

        </div>
        """
    )

    st.caption(
        "The moving indicators show request direction. "
        "The simulation metrics are produced by the SimPy simulation."
    )