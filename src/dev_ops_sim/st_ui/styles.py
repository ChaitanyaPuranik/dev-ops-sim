import streamlit as st


STYLES = """
<style>

.simulation-topology {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 60px;
    margin-top: 40px;
    margin-bottom: 40px;
}

.simulation-node {
    width: 260px;
    padding: 30px;
    border: 1px solid rgba(128, 128, 128, 0.35);
    border-radius: 14px;
    text-align: center;
    background: rgba(128, 128, 128, 0.05);
}

.simulation-node h3 {
    margin-top: 12px;
    margin-bottom: 10px;
}

.simulation-node p {
    margin: 5px 0;
}

.node-icon {
    width: 70px;
    height: 70px;
    margin: auto;
}

.request-flow {
    width: 250px;
    text-align: center;
}

.request-flow-label {
    margin-bottom: 12px;
    font-size: 14px;
}

.flow-line {
    position: relative;
    height: 4px;
    background: rgba(128, 128, 128, 0.45);
    border-radius: 4px;
}

.flow-line::after {
    content: "";
    position: absolute;
    right: -2px;
    top: -6px;

    border-top: 8px solid transparent;
    border-bottom: 8px solid transparent;
    border-left: 12px solid rgba(128, 128, 128, 0.8);
}

.request-dot {
    position: absolute;
    top: -4px;

    width: 12px;
    height: 12px;

    border-radius: 50%;
    background: #ff4b4b;

    animation: requestFlow 1.6s linear infinite;
}

.request-dot:nth-child(2) {
    animation-delay: 0.5s;
}

.request-dot:nth-child(3) {
    animation-delay: 1s;
}

@keyframes requestFlow {
    from {
        left: 0%;
    }

    to {
        left: 96%;
    }
}

</style>
"""


def load_styles():
    st.html(STYLES)