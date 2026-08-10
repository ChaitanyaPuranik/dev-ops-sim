import streamlit as st

from dev_ops_sim.st_ui.styles import load_styles
from dev_ops_sim.st_ui.simulation import run_simulation

from dev_ops_sim.st_ui.components.configuration import (
    render_configuration,
)
from dev_ops_sim.st_ui.components.topology import (
    render_topology,
)
from dev_ops_sim.st_ui.components.metrics import (
    render_metrics,
)


# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="DevOps Sim",
    page_icon="⚙️",
    layout="wide",
)

load_styles()


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title("DevOps Sim")

st.caption(
    "Visual simulation of workload flow through "
    "application infrastructure."
)


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

config, run_button = render_configuration()


# ---------------------------------------------------------
# Execute Simulation
# ---------------------------------------------------------

if run_button:

    try:

        result = run_simulation(
            traffic_rate=config["traffic_rate"],
            traffic_pattern=config["traffic_pattern"],
            traffic_duration=config["traffic_duration"],
            server_capacity=config["server_capacity"],
            processing_time=config["processing_time"],
        )

        st.session_state["simulation_result"] = result

    except ValueError as error:

        st.error(str(error))


# ---------------------------------------------------------
# Results
# ---------------------------------------------------------

result = st.session_state.get(
    "simulation_result"
)

render_topology(
    config=config,
    result=result,
)

render_metrics(
    result=result,
)