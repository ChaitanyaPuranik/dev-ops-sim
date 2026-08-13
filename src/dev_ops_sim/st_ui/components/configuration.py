import streamlit as st


def render_configuration():

    st.header("Node Configuration")

    with st.form("simulation_configuration"):

        traffic_column, balancer_column = st.columns(
            2,
            gap="large",
        )

        with traffic_column:

            st.subheader("Traffic Generator")

            traffic_rate = st.number_input(
                "Request Rate (requests/second)",
                min_value=0.1,
                value=10.0,
                step=1.0,
            )

            traffic_pattern = st.selectbox(
                "Traffic Pattern",
                options=["constant"],
            )

            traffic_duration = st.number_input(
                "Traffic Duration (seconds)",
                min_value=0.1,
                value=10.0,
                step=1.0,
            )

            expected_requests = int(
                traffic_rate * traffic_duration
            )

            st.caption(
                f"Requests to generate: {expected_requests}"
            )

        with balancer_column:

            st.subheader("Load Balancer")

            load_balancer_algorithm = st.selectbox(
                "Algorithm",
                options=["round_robin", "random"],
            )

            st.caption(
                "Distributes requests from traffic "
                "generator to application server."
            )

        server_column, database_column = st.columns(
            2,
            gap="large",
        )

        with server_column:

            st.subheader("Application Server")

            server_capacity = st.number_input(
                "Concurrent Request Capacity",
                min_value=1,
                value=5,
                step=1,
            )

            processing_time = st.number_input(
                "Processing Time (seconds/request)",
                min_value=0.01,
                value=0.2,
                step=0.05,
                format="%.2f",
            )

            theoretical_capacity = (
                server_capacity / processing_time
            )

            st.caption(
                "Maximum configured processing rate: "
                f"{theoretical_capacity:.2f} requests/second"
            )

        with database_column:

            st.subheader("Database")

            database_capacity = st.number_input(
                "Concurrent Query Capacity",
                min_value=1,
                value=4,
                step=1,
            )

            database_query_time = st.number_input(
                "Query Time (seconds/request)",
                min_value=0.01,
                value=0.1,
                step=0.05,
                format="%.2f",
            )

            theoretical_query_rate = (
                database_capacity / database_query_time
            )

            st.caption(
                "Maximum configured query rate: "
                f"{theoretical_query_rate:.2f} requests/second"
            )

        run_button = st.form_submit_button(
            "Run Simulation",
            type="primary",
            use_container_width=True,
        )

    config = {
        "traffic_rate": traffic_rate,
        "traffic_pattern": traffic_pattern,
        "traffic_duration": traffic_duration,
        "load_balancer_algorithm": load_balancer_algorithm,
        "server_capacity": server_capacity,
        "processing_time": processing_time,
        "database_capacity": database_capacity,
        "database_query_time": database_query_time,
    }

    return config, run_button