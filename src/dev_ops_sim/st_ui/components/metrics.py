import streamlit as st


def render_metrics(
    result: dict | None,
):

    st.header("Simulation Metrics")

    if result is None:

        st.info(
            "Configure the nodes and run the simulation "
            "to generate metrics."
        )

        return

    metric_1, metric_2, metric_3 = st.columns(3)

    metric_1.metric(
        "Requests Generated",
        result["generated"],
    )

    metric_2.metric(
        "Requests Received",
        result["received"],
    )

    metric_3.metric(
        "Requests Completed",
        result["completed"],
    )

    metric_4, metric_5, metric_6 = st.columns(3)

    metric_4.metric(
        "Simulation Time",
        f"{result['simulation_time']:.2f} s",
    )

    metric_5.metric(
        "Average Throughput",
        f"{result['average_throughput']:.2f} req/s",
    )

    metric_6.metric(
        "Completion Rate",
        f"{result['completion_rate']:.1f}%",
    )

    st.metric(
        "Backlog Drain Time",
        f"{result['drain_time']:.2f} s",
        help=(
            "Additional simulated time required after "
            "traffic generation ended for the application "
            "server to finish processing requests."
        ),
    )

    st.subheader("Node Flow")

    flow_1, flow_2, flow_3 = st.columns(3)

    flow_1.metric(
        "Load Balancer Received",
        result["balancer_received"],
    )

    flow_2.metric(
        "Load Balancer Forwarded",
        result["balancer_forwarded"],
    )

    flow_3.metric(
        "Database Completed",
        result["database_completed"],
    )