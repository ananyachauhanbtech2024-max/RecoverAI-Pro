
import streamlit as st
import pandas as pd
import plotly.express as px
from agent_engine import RecoveryAgent

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="RecoverAI",
    page_icon="💰",
    layout="wide"
)

# DASHBOARD



# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>
#MainMenu, footer, header { visibility: hidden; }

.stApp {
    background:
        radial-gradient(circle at 10% 0%, rgba(59,130,246,.10), transparent 28%),
        radial-gradient(circle at 90% 10%, rgba(124,58,237,.08), transparent 25%),
        linear-gradient(135deg, #f7faff 0%, #eef4ff 52%, #ffffff 100%);
}

.block-container {
    max-width: 1480px;
    padding-top: 1.8rem;
    padding-bottom: 4rem;
}

section[data-testid="stSidebar"] {
    background: rgba(255,255,255,.94);
    border-right: 1px solid #e5e7eb;
}

.brand-card {
    padding: 18px 16px;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    background: linear-gradient(135deg,#ffffff,#f6f9ff);
    box-shadow: 0 8px 28px rgba(15,23,42,.06);
    margin-bottom: 18px;
}

.brand-name { font-size: 24px; font-weight: 800; color: #111827; }
.brand-tag { font-size: 12px; color: #667085; margin-top: 4px; }

.hero {
    padding: 30px 34px;
    border-radius: 24px;
    background: linear-gradient(135deg, #ffffff 0%, #f1f6ff 100%);
    border: 1px solid #dfe7f5;
    box-shadow: 0 14px 40px rgba(15,23,42,.07);
    margin-bottom: 26px;
}

.hero-kicker {
    display: inline-block;
    padding: 6px 11px;
    border-radius: 999px;
    background: #e8f1ff;
    color: #2563eb;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: .4px;
}

.hero-title {
    font-size: 46px;
    line-height: 1.05;
    font-weight: 850;
    letter-spacing: -1.8px;
    color: #0f172a;
    margin-top: 10px;
}

.hero-subtitle {
    color: #667085;
    font-size: 17px;
    line-height: 1.6;
    max-width: 850px;
}

.hero-flow {
    margin-top: 18px;
    font-size: 13px;
    font-weight: 750;
    color: #475467;
}

h1, h2, h3 {
    color: #0f172a;
    font-weight: 800 !important;
}

div[data-testid="stMetric"] {
    background: rgba(255,255,255,.94);
    border: 1px solid #e4e7ec;
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0 7px 24px rgba(15,23,42,.055);
}

div[data-testid="stMetricLabel"] {
    color: #667085;
    font-size: 13px;
    font-weight: 700;
}

div[data-testid="stMetricValue"] {
    color: #101828;
    font-size: 28px;
    font-weight: 800;
}

.stButton > button {
    border-radius: 12px;
    min-height: 44px;
    font-weight: 750;
    border: 1px solid #d0d5dd;
}

button[kind="primary"] {
    border: none !important;
    background: linear-gradient(135deg,#2563eb,#4f46e5) !important;
}

div[data-baseweb="select"] > div,
div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input {
    border-radius: 11px;
}

div[data-testid="stDataFrame"] {
    border: 1px solid #e4e7ec;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 5px 18px rgba(15,23,42,.04);
}

div[data-testid="stAlert"] { border-radius: 14px; }

.info-card {
    background: rgba(255,255,255,.90);
    border: 1px solid #e4e7ec;
    border-radius: 18px;
    padding: 16px 20px;
    box-shadow: 0 6px 20px rgba(15,23,42,.045);
}

.pill {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 999px;
    background: #eef2ff;
    color: #4338ca;
    font-size: 12px;
    font-weight: 800;
}

hr {
    margin-top: 28px;
    margin-bottom: 28px;
    border: 0;
    border-top: 1px solid #e4e7ec;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div class="brand-card">
        <div class="brand-name">💰 RecoverAI</div>
        <div class="brand-tag">Autonomous Revenue Recovery</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("### Control Center")
    st.caption("AI-driven revenue recovery workspace")
    st.markdown("---")
    st.markdown("**CORE MODULES**")
    st.markdown("• Revenue Risk")
    st.markdown("• Recovery Intelligence")
    st.markdown("• Autonomous Agent")
    st.markdown("• Recovery War Room")
    st.markdown("---")
    st.markdown("**AI SYSTEMS**")
    st.markdown("• What-If Simulator")
    st.markdown("• Explainable AI")
    st.markdown("• ROI Optimizer")
    st.markdown("• A/B Experiment")
    st.markdown("• Recovery Memory")
    st.markdown("• Guardrails & Approval")
    st.markdown("---")
    st.caption("Prototype • Simulated recovery outcomes")

st.markdown("""
<div class="hero">
    <div class="hero-kicker">AUTONOMOUS REVENUE RECOVERY PLATFORM</div>
    <div class="hero-title">RecoverAI</div>
    <div class="hero-subtitle">
        Detect revenue leakage, prioritize the customers worth saving,
        choose the next-best recovery action, enforce safety rules,
        and learn from every recovery attempt.
    </div>
    <div class="hero-flow">
        OBSERVE → ANALYZE → DECIDE → GUARDRAIL → ACT → LEARN
    </div>
</div>
""", unsafe_allow_html=True)
# -----------------------------------
# TITLE
# -----------------------------------

st.markdown(
    '<div class="title">💰 RecoverAI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI Revenue Recovery Dashboard — Find revenue that is slipping away and win it back.'
    '</div>',
    unsafe_allow_html=True
)

# -----------------------------------
# LOAD DATA
# -----------------------------------

try:
    df = pd.read_csv("recoverai_data.csv")

except FileNotFoundError:

    st.error(
        "recoverai_data.csv was not found. "
        "Please make sure it is in the same folder as app.py."
    )

    st.stop()
# -----------------------------------
# BASIC CLEANING
# -----------------------------------

df["total_spent"] = pd.to_numeric(
    df["total_spent"],
    errors="coerce"
).fillna(0)

df["expected_recovery"] = pd.to_numeric(
    df["expected_recovery"],
    errors="coerce"
).fillna(0)

df["recovery_probability"] = pd.to_numeric(
    df["recovery_probability"],
    errors="coerce"
).fillna(0)

df["risk_score"] = pd.to_numeric(
    df["risk_score"],
    errors="coerce"
).fillna(0)

# -----------------------------------
# METRICS
# -----------------------------------

# Only customers with a recovery event
at_risk = df[
    df["recovery_event"] != "successful"
].copy()

revenue_at_risk = at_risk["total_spent"].sum()

expected_recovery = at_risk["expected_recovery"].sum()

high_risk = len(
    at_risk[at_risk["risk_level"] == "HIGH"]
)

total_customers = len(df)

# -----------------------------------
# SYSTEM STATUS
# -----------------------------------
st.markdown("""
<div class="info-card">
    <span class="pill">● SYSTEM ONLINE</span>
    &nbsp;&nbsp; Risk scoring ready
    &nbsp;•&nbsp; Recovery engine ready
    &nbsp;•&nbsp; Guardrails enabled
</div>
""", unsafe_allow_html=True)

# -----------------------------------
# TOP METRICS
# -----------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Revenue At Risk",
        f"£{revenue_at_risk:,.0f}"
    )

with col2:
    st.metric(
        "Expected Recovery",
        f"£{expected_recovery:,.0f}"
    )

with col3:
    st.metric(
        "High Risk",
        f"{high_risk:,}"
    )

with col4:
    st.metric(
        "Customers",
        f"{total_customers:,}"
    )

st.divider()

# -----------------------------------
# SIDEBAR FILTER
# -----------------------------------

st.sidebar.header("Recovery Filters")

risk_filter = st.sidebar.multiselect(
    "Risk Level",
    options=["HIGH", "MEDIUM", "LOW"],
    default=["HIGH", "MEDIUM"]
)

event_filter = st.sidebar.multiselect(
    "Recovery Event",
    options=sorted(
        at_risk["recovery_event"].unique()
    ),
    default=sorted(
        at_risk["recovery_event"].unique()
    )
)

filtered_df = at_risk[
    at_risk["risk_level"].isin(risk_filter)
    &
    at_risk["recovery_event"].isin(event_filter)
]

# -----------------------------------
# RECOVERY OPPORTUNITIES
# -----------------------------------

st.header("Revenue Recovery Opportunities")

st.write(
    f"Showing **{len(filtered_df):,}** customers requiring attention."
)

display_df = filtered_df[
    [
        "CustomerID",
        "total_spent",
        "total_orders",
        "days_since_purchase",
        "recovery_event",
        "failure_reason",
        "risk_score",
        "risk_level",
        "recovery_probability",
        "expected_recovery",
        "recommended_action"
    ]
].copy()

display_df.columns = [
    "Customer",
    "Revenue",
    "Orders",
    "Days Since Purchase",
    "Event",
    "Failure Reason",
    "Risk Score",
    "Risk",
    "Recovery Probability",
    "Expected Recovery",
    "Recommended Action"
]

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)

# -----------------------------------
# CHARTS
# -----------------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("Revenue At Risk by Customer")

    top_risk = filtered_df.sort_values(
        "total_spent",
        ascending=False
    ).head(10)

    fig1 = px.bar(
        top_risk,
        x="CustomerID",
        y="total_spent",
        title="Top Revenue-at-Risk Customers",
        labels={
            "CustomerID": "Customer",
            "total_spent": "Revenue (£)"
        }
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with col2:

    st.subheader("Recovery Opportunity")

    event_data = (
        filtered_df
        .groupby("recovery_event")["expected_recovery"]
        .sum()
        .reset_index()
    )

    fig2 = px.pie(
        event_data,
        names="recovery_event",
        values="expected_recovery",
        title="Expected Recovery by Event"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# -----------------------------------
# BEST RECOVERY OPPORTUNITIES
# -----------------------------------

st.header(" Best Recovery Opportunities")

best = filtered_df.sort_values(
    "expected_recovery",
    ascending=False
).head(10)

for _, row in best.iterrows():

    with st.container():

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.write(
                f"**Customer {int(row['CustomerID'])}**"
            )

        with col2:
            st.write(
                f"Revenue: **£{row['total_spent']:,.0f}**"
            )

        with col3:
            st.write(
                f"Recovery Probability: "
                f"**{row['recovery_probability']:.1f}%**"
            )

        with col4:
            st.write(
                f"Expected: "
                f"**£{row['expected_recovery']:,.0f}**"
            )

        st.caption(
            f"Reason: {row['failure_reason']}  |  "
            f"Recommended Action: {row['recommended_action']}"
        )

        st.divider()

# -----------------------------------
# RECOVERY SUMMARY
# -----------------------------------

st.header("Recovery Summary")

summary_col1, summary_col2 = st.columns(2)

with summary_col1:

    st.metric(
        "Customers Needing Recovery",
        f"{len(at_risk):,}"
    )

    st.metric(
        "Potential Revenue",
        f"£{revenue_at_risk:,.0f}"
    )

with summary_col2:

    recovery_rate = (
        expected_recovery / revenue_at_risk * 100
        if revenue_at_risk > 0
        else 0
    )

    st.metric(
        "Expected Recovery Rate",
        f"{recovery_rate:.1f}%"
    )

    st.metric(
        "Potential Money Recovered",
        f"£{expected_recovery:,.0f}"
    )

# -----------------------------------
# DATA NOTE
# -----------------------------------

st.divider()

st.caption(
    "Data source: Public Online Retail transaction dataset. "
    "Recovery events and recovery outcomes are simulated for this prototype."
)
# -----------------------------------
# AI RECOVERY AGENT
# -----------------------------------

st.divider()

st.header("AI Recovery Agent")

st.write(
    "Select a customer and let RecoverAI determine the best recovery action."
)

if len(filtered_df) > 0:

    customer_ids = filtered_df["CustomerID"].astype(int).tolist()

    selected_customer = st.selectbox(
        "Select Customer",
        customer_ids,
        key="main_customer_selector",
        format_func=lambda x: f"Customer {x}"
    )

    customer = filtered_df[
        filtered_df["CustomerID"] == selected_customer
    ].iloc[0]

    # Customer information
    st.subheader(" Customer Analysis")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Revenue at Risk",
            f"£{customer['total_spent']:,.2f}"
        )

    with col2:
        st.metric(
            "Risk Score",
            f"{customer['risk_score']:.0f}/100"
        )

    with col3:
        st.metric(
            "Recovery Probability",
            f"{customer['recovery_probability']:.1f}%"
        )

    with col4:
        st.metric(
            "Expected Recovery",
            f"£{customer['expected_recovery']:,.2f}"
        )

    # AI diagnosis
    st.subheader("AI Diagnosis")

    st.info(
        f"""
        **Risk Level:** {customer['risk_level']}

        **Revenue Risk Reason:** {customer['failure_reason']}

        **Recovery Event:** {customer['recovery_event']}

        **Days Since Purchase:** {customer['days_since_purchase']} days

        **AI Recommended Action:** 
        {customer['recommended_action']}
        """
    )

    # Recovery action
    st.subheader("Execute Recovery")

    action = customer["recommended_action"]

    st.write(
        f"RecoverAI recommends: **{action}**"
    )

    if st.button(
        " Recover Now",
        type="primary"
    ):

        # Simulated recovery
        recovered_amount = customer["expected_recovery"]

        st.success(
            f"Recovery action executed successfully!"
        )

        st.metric(
            "Simulated Money Recovered",
            f"£{recovered_amount:,.2f}"
        )

        st.write(
            f"**Action executed:** {action}"
        )

        st.write(
            f"**Customer:** {int(customer['CustomerID'])}"
        )

        st.write(
            "Recovery workflow completed with bounded action."
        )

        # Audit trail
        st.subheader("Recovery Audit Trail")

        audit = pd.DataFrame({
            "Step": [
                "Risk Detected",
                "Customer Analyzed",
                "Recovery Action Selected",
                "Recovery Executed"
            ],
            "Status": [
                "Completed",
                "Completed",
                "Completed",
                "Completed"
            ],
            "Details": [
                f"Risk score = {customer['risk_score']:.0f}",
                f"Event = {customer['recovery_event']}",
                action,
                f"£{recovered_amount:,.2f} simulated recovery"
            ]
        })

        st.dataframe(
            audit,
            use_container_width=True,
            hide_index=True
        )

else:

    st.warning(
        "No customers match the selected filters."
    )
    # ==========================================
# RECOVERY INTELLIGENCE
# ==========================================

st.divider()

st.header("" \
" Recovery Intelligence")

st.write(
    "RecoverAI prioritizes customers based on risk, recovery probability "
    "and expected recovery value."
)

# Create a copy for analysis
intelligence_df = filtered_df.copy()

if len(intelligence_df) > 0:

    # ------------------------------------------
    # Recovery Priority Score
    # ------------------------------------------

    intelligence_df["priority_score"] = (
        intelligence_df["risk_score"] * 0.4
        + intelligence_df["recovery_probability"] * 0.3
        + (
            intelligence_df["expected_recovery"]
            / intelligence_df["expected_recovery"].max()
            * 100
        ) * 0.3
    )

    # Sort highest priority first
    intelligence_df = intelligence_df.sort_values(
        "priority_score",
        ascending=False
    )

    # ------------------------------------------
    # TOP RECOVERY OPPORTUNITY
    # ------------------------------------------

    top_customer = intelligence_df.iloc[0]

    st.subheader("Top Recovery Opportunity")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Customer",
            int(top_customer["CustomerID"])
        )

    with col2:
        st.metric(
            "Risk Score",
            f"{top_customer['risk_score']:.0f}/100"
        )

    with col3:
        st.metric(
            "Recovery Probability",
            f"{top_customer['recovery_probability']:.1f}%"
        )

    with col4:
        st.metric(
            "Expected Recovery",
            f"£{top_customer['expected_recovery']:,.2f}"
        )

    # ------------------------------------------
    # AI DECISION
    # ------------------------------------------

    st.subheader("AI Decision")

    if top_customer["priority_score"] >= 70:

        st.error(
            "HIGH PRIORITY — Recover immediately"
        )

    elif top_customer["priority_score"] >= 40:

        st.warning(
            "⚠️ MEDIUM PRIORITY — Recovery recommended"
        )

    else:

        st.success(
            "LOW PRIORITY — Monitor customer"
        )

    st.write(
        f"""
        **Customer:** {int(top_customer['CustomerID'])}

        **Priority Score:** {top_customer['priority_score']:.1f}/100

        **Recommended Action:** 
        {top_customer['recommended_action']}

        **Expected Recovery:** 
        £{top_customer['expected_recovery']:,.2f}
        """
    )

    # ------------------------------------------
    # RECOVERY RANKING
    # ------------------------------------------

    st.subheader("Recovery Priority Ranking")

    ranking_df = intelligence_df[
        [
            "CustomerID",
            "risk_score",
            "recovery_probability",
            "expected_recovery",
            "priority_score",
            "recommended_action"
        ]
    ].head(10).copy()

    ranking_df.columns = [
        "Customer",
        "Risk Score",
        "Recovery Probability",
        "Expected Recovery",
        "Priority Score",
        "Recommended Action"
    ]

    st.dataframe(
        ranking_df,
        use_container_width=True,
        hide_index=True
    )

    # ------------------------------------------
    # TOTAL RECOVERY OPPORTUNITY
    # ------------------------------------------

    st.subheader("Recovery Opportunity")

    total_expected = intelligence_df[
        "expected_recovery"
    ].sum()

    high_priority = len(
        intelligence_df[
            intelligence_df["priority_score"] >= 70
        ]
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Total Expected Recovery",
            f"£{total_expected:,.2f}"
        )

    with col2:

        st.metric(
            "High Priority Customers",
            high_priority
        )

else:

    st.warning(
        "No customers available for recovery intelligence."
    )
    # ==========================================
# SMART STOPPING RULES
# ==========================================

st.divider()

st.header(" Smart Recovery Stopping Rules")

st.write(
    "RecoverAI prevents repeated recovery attempts and stops "
    "when recovery is successful or the retry limit is reached."
)

col1, col2, col3 = st.columns(3)

with col1:
    max_attempts = st.number_input(
        "Maximum Recovery Attempts",
        min_value=1,
        max_value=5,
        value=2
    )

with col2:
    current_attempts = st.number_input(
        "Attempts Already Made",
        min_value=0,
        max_value=5,
        value=0
    )

with col3:
    recovery_success = st.checkbox(
        "Recovery Successful?"
    )

st.subheader(" Agent Decision")

if recovery_success:

    st.success(
        " Recovery successful — STOP further actions."
    )

    st.write(
        "Stopping Rule Triggered: Revenue recovered successfully."
    )

elif current_attempts >= max_attempts:

    st.error(
        " Retry limit reached — STOP and escalate."
    )

    st.write(
        f"Stopping Rule Triggered: Maximum {max_attempts} attempts reached."
    )

else:

    remaining = max_attempts - current_attempts

    st.warning(
        f" Recovery not successful — {remaining} retry attempt(s) remaining."
    )

    st.write(
        "Agent may attempt the next bounded recovery action."
    )

# ------------------------------------------
# RECOVERY POLICY
# ------------------------------------------

st.subheader(" Recovery Policy")

policy = pd.DataFrame({
    "Condition": [
        "Recovery successful",
        "Retry limit reached",
        "Recovery unsuccessful"
    ],
    "Agent Action": [
        "STOP",
        "STOP + Escalate",
        "Retry bounded action"
    ]
})

st.dataframe(
    policy,
    use_container_width=True,
    hide_index=True
)
# ==========================================
# RECOVERY WAR ROOM
# ==========================================

st.divider()

st.header(" Recovery War Room")

st.write(
    "A real-time command center for identifying and prioritizing "
    "revenue recovery opportunities."
)

# ------------------------------------------
# WAR ROOM METRICS
# ------------------------------------------

total_revenue_risk = intelligence_df["total_spent"].sum()

expected_recovery = intelligence_df["expected_recovery"].sum()

customers_at_risk = len(intelligence_df)

high_risk_customers = len(
    intelligence_df[
        intelligence_df["risk_score"] >= 70
    ]
)

recovery_rate = (
    expected_recovery / total_revenue_risk * 100
    if total_revenue_risk > 0
    else 0
)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        " Revenue at Risk",
        f"£{total_revenue_risk:,.0f}"
    )

with col2:
    st.metric(
        " Expected Recovery",
        f"£{expected_recovery:,.0f}"
    )

with col3:
    st.metric(
        "👥 Customers at Risk",
        customers_at_risk
    )

with col4:
    st.metric(
        " High Risk",
        high_risk_customers
    )

with col5:
    st.metric(
        " Recovery Rate",
        f"{recovery_rate:.1f}%"
    )

# ------------------------------------------
# RECOVERY CHART
# ------------------------------------------

st.subheader("Revenue Recovery Potential")

chart_data = pd.DataFrame({
    "Category": [
        "Revenue at Risk",
        "Expected Recovery"
    ],
    "Amount": [
        total_revenue_risk,
        expected_recovery
    ]
})

st.bar_chart(
    chart_data.set_index("Category")
)

# ------------------------------------------
# TOP RECOVERY CUSTOMERS
# ------------------------------------------

st.subheader("Top Recovery Targets")

war_room_table = intelligence_df[
    [
        "CustomerID",
        "risk_score",
        "recovery_probability",
        "expected_recovery",
        "priority_score",
        "recommended_action"
    ]
].head(10).copy()

war_room_table.columns = [
    "Customer",
    "Risk Score",
    "Recovery Probability",
    "Expected Recovery",
    "Priority Score",
    "Recommended Action"
]

st.dataframe(
    war_room_table,
    use_container_width=True,
    hide_index=True
)

# ------------------------------------------
# WAR ROOM STATUS
# ------------------------------------------

st.subheader(" AI War Room Status")

if high_risk_customers > 0:

    st.error(
        f" {high_risk_customers} high-risk customer(s) "
        "require immediate recovery attention."
    )

elif customers_at_risk > 0:

    st.warning(
        "⚠️ Revenue recovery opportunities detected. "
        "Monitor and prioritize actions."
    )

else:

    st.success(
        " No significant recovery opportunities detected."
    )
    # ==========================================
# WHAT-IF REVENUE SIMULATOR
# ==========================================

st.divider()

st.header(" What-If Revenue Simulator")

st.write(
    "Simulate how changes in recovery success rate can impact "
    "expected revenue recovery."
)

# Current recovery rate
current_rate = recovery_rate

# User chooses target recovery rate
target_rate = st.slider(
    "Target Recovery Rate (%)",
    min_value=10,
    max_value=100,
    value=int(current_rate),
    step=5
)

# Calculate simulated recovery
simulated_recovery = (
    total_revenue_risk * target_rate / 100
)

additional_recovery = (
    simulated_recovery - expected_recovery
)

# Display results
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Current Recovery",
        f"£{expected_recovery:,.0f}"
    )

with col2:
    st.metric(
        "Simulated Recovery",
        f"£{simulated_recovery:,.0f}"
    )

with col3:
    st.metric(
        "Additional Revenue",
        f"£{additional_recovery:,.0f}"
    )

# AI interpretation
st.subheader(" AI Scenario Analysis")

if additional_recovery > 0:

    st.success(
        f"""
        Increasing recovery effectiveness to **{target_rate}%**
        could generate approximately **£{additional_recovery:,.0f}**
        in additional expected recovery.
        """
    )

elif additional_recovery < 0:

    st.warning(
        f"""
        At a recovery rate of **{target_rate}%**, expected recovery
        would decrease by approximately
        **£{abs(additional_recovery):,.0f}**.
        """
    )

else:

    st.info(
        "This scenario matches the current expected recovery."
    )
    # ==========================================
# EXPLAINABLE AI
# ==========================================

st.divider()

st.header("Why Did AI Choose This Action?")

if len(intelligence_df) > 0:

    explain_customer = st.selectbox(
        "Select customer for AI explanation",
        intelligence_df["CustomerID"].astype(int).tolist(),
        key="explain_customer"
    )

    explain_data = intelligence_df[
        intelligence_df["CustomerID"] == explain_customer
    ].iloc[0]

    risk_score = explain_data["risk_score"]
    recovery_probability = explain_data["recovery_probability"]
    days_inactive = explain_data["days_since_purchase"]

    st.subheader(" AI Decision Breakdown")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Risk Score",
            f"{risk_score:.0f}/100"
        )

    with col2:
        st.metric(
            "Recovery Probability",
            f"{recovery_probability:.1f}%"
        )

    with col3:
        st.metric(
            "Days Inactive",
            f"{days_inactive}"
        )

    st.subheader("Decision Factors")

    factors = []

    if risk_score >= 70:
        factors.append(
            "High revenue risk detected"
        )
    elif risk_score >= 40:
        factors.append(
            "⚠️ Moderate revenue risk detected"
        )
    else:
        factors.append(
            " Low revenue risk detected"
        )

    if days_inactive > 90:
        factors.append(
            " Customer has been inactive for a long period"
        )

    if recovery_probability >= 60:
        factors.append(
            "High probability of successful recovery"
        )
    elif recovery_probability >= 30:
        factors.append(
            "Moderate probability of successful recovery"
        )
    else:
        factors.append(
            "Low probability of successful recovery"
        )

    for factor in factors:
        st.write(factor)

    st.subheader("AI Recommendation")

    st.success(
        f"""
        **Recommended Action:** 
        {explain_data["recommended_action"]}

        **Reason:** 
        The customer has a risk score of {risk_score:.0f}/100
        with a recovery probability of {recovery_probability:.1f}%.
        The AI selected the recovery action based on these risk
        and recovery signals.
        """
    )

else:
    st.info("No customers available for explanation.")

    # ==========================================
# ROI OPTIMIZER
# ==========================================

st.divider()

st.header("Recovery ROI Optimizer")

st.write(
    "RecoverAI compares recovery actions using expected revenue, "
    "intervention cost and net recovery."
)

if len(intelligence_df) > 0:

    roi_customer = st.selectbox(
        "Select customer",
        intelligence_df["CustomerID"].astype(int).tolist(),
        key="roi_customer"
    )

    roi_data = intelligence_df[
        intelligence_df["CustomerID"] == roi_customer
    ].iloc[0]

    expected_value = float(roi_data["expected_recovery"])

    st.subheader(" Recovery Action Assumptions")

    col1, col2, col3 = st.columns(3)

    with col1:
        email_cost = st.number_input(
            "Email Cost (£)",
            min_value=0.0,
            value=2.0,
            step=1.0
        )

    with col2:
        sms_cost = st.number_input(
            "SMS Cost (£)",
            min_value=0.0,
            value=5.0,
            step=1.0
        )

    with col3:
        discount_percent = st.slider(
            "Discount (%)",
            min_value=0,
            max_value=30,
            value=10
        )

    # Action calculations

    email_recovery = expected_value
    email_net = email_recovery - email_cost

    sms_recovery = expected_value * 1.05
    sms_net = sms_recovery - sms_cost

    discount_cost = expected_value * discount_percent / 100

    discount_recovery = expected_value * 1.15
    discount_net = discount_recovery - discount_cost

    # ------------------------------------------
    # Compare actions
    # ------------------------------------------

    roi_table = pd.DataFrame({
        "Action": [
            "Email Reminder",
            "SMS Reminder",
            "Discount Offer"
        ],
        "Expected Recovery": [
            email_recovery,
            sms_recovery,
            discount_recovery
        ],
        "Intervention Cost": [
            email_cost,
            sms_cost,
            discount_cost
        ],
        "Net Recovery": [
            email_net,
            sms_net,
            discount_net
        ]
    })

    roi_table["ROI"] = (
        roi_table["Net Recovery"]
        / roi_table["Intervention Cost"].replace(0, 0.01)
    )

    # ------------------------------------------
    # Best action
    # ------------------------------------------

    best_action = roi_table.loc[
        roi_table["Net Recovery"].idxmax()
    ]

    st.subheader("Action Comparison")

    display_table = roi_table.copy()

    display_table["Expected Recovery"] = (
        display_table["Expected Recovery"]
        .map(lambda x: f"£{x:,.2f}")
    )

    display_table["Intervention Cost"] = (
        display_table["Intervention Cost"]
        .map(lambda x: f"£{x:,.2f}")
    )

    display_table["Net Recovery"] = (
        display_table["Net Recovery"]
        .map(lambda x: f"£{x:,.2f}")
    )

    display_table["ROI"] = (
        display_table["ROI"]
        .map(lambda x: f"{x:,.1f}x")
    )

    st.dataframe(
        display_table,
        use_container_width=True,
        hide_index=True
    )

    # ------------------------------------------
    # AI recommendation
    # ------------------------------------------

    st.subheader("AI ROI Recommendation")

    st.success(
        f"""
         **Best Action: {best_action["Action"]}**

        Expected Recovery: **£{best_action["Expected Recovery"]:,.2f}**

        Intervention Cost: **£{best_action["Intervention Cost"]:,.2f}**

        Net Recovery: **£{best_action["Net Recovery"]:,.2f}**

        ROI: **{best_action["ROI"]:.1f}x**

        RecoverAI selects the action with the highest expected
        net recovery rather than simply choosing the action
        with the highest gross recovery.
        """
    )

else:

    st.info("No customers available for ROI analysis.")
# ==========================================
# A/B RECOVERY EXPERIMENT
# ==========================================

st.divider()

st.header(" A/B Recovery Experiment")

st.write(
    "RecoverAI compares different recovery interventions "
    "to identify the most effective strategy."
)

if len(intelligence_df) > 0:

    ab_customer = st.selectbox(
        "Select customer for experiment",
        intelligence_df["CustomerID"].astype(int).tolist(),
        key="ab_customer"
    )

    ab_data = intelligence_df[
        intelligence_df["CustomerID"] == ab_customer
    ].iloc[0]

    base_probability = float(
        ab_data["recovery_probability"]
    )

    expected_value = float(
        ab_data["expected_recovery"]
    )

    # Simulated intervention performance
    email_probability = min(base_probability * 0.90, 100)
    sms_probability = min(base_probability * 1.05, 100)
    discount_probability = min(base_probability * 1.15, 100)

    email_recovery = expected_value * email_probability / base_probability
    sms_recovery = expected_value * sms_probability / base_probability
    discount_recovery = expected_value * discount_probability / base_probability

    experiment = pd.DataFrame({
        "Intervention": [
            "Email Reminder",
            "SMS Reminder",
            "Discount Offer"
        ],
        "Predicted Success": [
            email_probability,
            sms_probability,
            discount_probability
        ],
        "Expected Recovery": [
            email_recovery,
            sms_recovery,
            discount_recovery
        ]
    })

    # Find winner
    winner = experiment.loc[
        experiment["Expected Recovery"].idxmax()
    ]

    st.subheader(" Experiment Results")

    display_experiment = experiment.copy()

    display_experiment["Predicted Success"] = (
        display_experiment["Predicted Success"]
        .map(lambda x: f"{x:.1f}%")
    )

    display_experiment["Expected Recovery"] = (
        display_experiment["Expected Recovery"]
        .map(lambda x: f"£{x:,.2f}")
    )

    st.dataframe(
        display_experiment,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Winning Intervention")

    st.success(
        f"""
        **{winner["Intervention"]}**

        Predicted Success: **{winner["Predicted Success"]:.1f}%**

        Expected Recovery: **£{winner["Expected Recovery"]:,.2f}**

        RecoverAI recommends the intervention with the
        highest predicted recovery potential.
        """
    )

else:

    st.info("No customers available for A/B experiment.")

    # ==========================================
# RECOVERY MEMORY
# ==========================================

st.divider()

st.header(" Recovery Memory")

st.write(
    "RecoverAI learns from previous recovery attempts "
    "and uses customer history to improve future decisions."
)

if len(intelligence_df) > 0:

    memory_customer = st.selectbox(
        "Select customer",
        intelligence_df["CustomerID"].astype(int).tolist(),
        key="memory_customer"
    )

    memory_data = intelligence_df[
        intelligence_df["CustomerID"] == memory_customer
    ].iloc[0]

    st.subheader(" Customer Recovery History")

    # Simulated historical memory
    memory_data_table = pd.DataFrame({
        "Previous Action": [
            "Email Reminder",
            "SMS Reminder",
            "Discount Offer"
        ],
        "Result": [
            "Failed ",
            "Successful ",
            "Not Used"
        ],
        "Learning": [
            "Low response",
            "High response",
            "Available option"
        ]
    })

    st.dataframe(
        memory_data_table,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("AI Learned Preference")

    st.info(
        """
        **Customer behaviour detected:**

        Previous SMS intervention showed the strongest
        simulated response.

        RecoverAI will prioritize SMS-based recovery
        for the next intervention.
        """
    )

    st.subheader("Next Recommended Action")

    st.success(
        "SMS Reminder — prioritized using recovery memory"
    )

else:

    st.info("No customer data available for recovery memory.")
    # ==========================================
# AI GUARDRAILS + HUMAN APPROVAL
# ==========================================

st.divider()

st.header(" AI Guardrails & Human Approval")

st.write(
    "RecoverAI uses safety rules to keep automated recovery "
    "actions within approved business limits."
)

if len(intelligence_df) > 0:

    guard_customer = st.selectbox(
        "Select customer",
        intelligence_df["CustomerID"].astype(int).tolist(),
        key="guard_customer"
    )

    guard_data = intelligence_df[
        intelligence_df["CustomerID"] == guard_customer
    ].iloc[0]

    st.subheader("Recovery Policy")

    col1, col2 = st.columns(2)

    with col1:
        max_discount = st.slider(
            "Maximum Allowed Discount (%)",
            min_value=0,
            max_value=30,
            value=15,
            step=5
        )

    with col2:
        requested_discount = st.slider(
            "AI Requested Discount (%)",
            min_value=0,
            max_value=30,
            value=10,
            step=5
        )

    st.subheader("Guardrail Check")

    # Guardrail 1: Discount limit
    if requested_discount > max_discount:

        st.error(
            f" Guardrail Triggered: "
            f"AI requested {requested_discount}% discount, "
            f"but the maximum allowed is {max_discount}%."
        )

        approval_required = True

    else:

        st.success(
            f" Discount request of {requested_discount}% "
            f"is within the allowed {max_discount}% limit."
        )

        approval_required = False

    # Guardrail 2: High-risk action
    risk_score = float(guard_data["risk_score"])

    if risk_score >= 80:

        st.warning(
            "⚠️ High-risk customer detected. "
            "Human review is recommended before execution."
        )

        approval_required = True

    # ------------------------------------------
    # HUMAN APPROVAL
    # ------------------------------------------

    st.subheader(" Human Approval")

    if approval_required:

        st.warning(
            " Human approval is required before this "
            "recovery action can be executed."
        )

        approved = st.checkbox(
            "I approve this recovery action",
            key="human_approval"
        )

        if approved:

            st.success(
                "Human approval received. "
                "Recovery action is authorized."
            )

            if st.button(
                "Execute Approved Recovery",
                key="approved_recovery"
            ):

                st.success(
                    "Recovery action executed successfully."
                )

                st.info(
                    "Audit Trail: Human-approved recovery action recorded."
                )

        else:

            st.info(
                " Action paused until human approval is provided."
            )

    else:

        st.success(
            " Action is within AI guardrails. "
            "No additional approval is required."
        )

        if st.button(
            "Execute Recovery",
            key="normal_recovery"
        ):

            st.success(
                "Recovery action executed successfully."
            )

            st.info(
                "Audit Trail: Guardrail-compliant action recorded."
            )

    # ------------------------------------------
    # POLICY SUMMARY
    # ------------------------------------------

    st.subheader("Active AI Safety Policy")

    policy_guardrails = pd.DataFrame({
        "Guardrail": [
            "Maximum Discount",
            "High Risk Customer",
            "Human Approval",
            "Audit Trail"
        ],
        "Rule": [
            f"≤ {max_discount}%",
            "Risk Score ≥ 80",
            "Required when guardrail triggered",
            "Every approved action recorded"
        ],
        "Purpose": [
            "Prevent excessive discounts",
            "Protect high-value decisions",
            "Maintain human oversight",
            "Maintain accountability"
        ]
    })

    st.dataframe(
        policy_guardrails,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No customer data available for guardrail analysis.")

    # ==========================================
# REVENUE LEAKAGE HEATMAP
# ==========================================

st.divider()

st.header(" Revenue Leakage Heatmap")

st.write(
    "Identify regions with the highest revenue-at-risk "
    "and recovery opportunities."
)

if len(intelligence_df) > 0:

    # ------------------------------------------
    # Create region data
    # ------------------------------------------

    region_data = intelligence_df.copy()

    # Use country column if available
    if "Country" in region_data.columns:

        region_summary = (
            region_data
            .groupby("Country")
            .agg(
                Customers=("CustomerID", "count"),
                Revenue_at_Risk=("total_spent", "sum"),
                Expected_Recovery=("expected_recovery", "sum")
            )
            .reset_index()
        )

    else:

        # Fallback if Country is not available
        region_data["Region"] = (
            region_data["CustomerID"] % 5
        )

        region_summary = (
            region_data
            .groupby("Region")
            .agg(
                Customers=("CustomerID", "count"),
                Revenue_at_Risk=("total_spent", "sum"),
                Expected_Recovery=("expected_recovery", "sum")
            )
            .reset_index()
        )

        region_summary["Country"] = (
            "Region " +
            region_summary["Region"].astype(str)
        )

    # ------------------------------------------
    # Calculate leakage
    # ------------------------------------------

    region_summary["Revenue_Leakage"] = (
        region_summary["Revenue_at_Risk"]
        - region_summary["Expected_Recovery"]
    )

    region_summary = region_summary.sort_values(
        "Revenue_Leakage",
        ascending=False
    )

    # ------------------------------------------
    # Top leakage region
    # ------------------------------------------

    top_region = region_summary.iloc[0]

    st.subheader("Highest Revenue Leakage Region")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Region",
            top_region["Country"]
        )

    with col2:
        st.metric(
            "Revenue at Risk",
            f"£{top_region['Revenue_at_Risk']:,.0f}"
        )

    with col3:
        st.metric(
            "Revenue Leakage",
            f"£{top_region['Revenue_Leakage']:,.0f}"
        )

    # ------------------------------------------
    # Leakage ranking
    # ------------------------------------------

    st.subheader("Regional Revenue Leakage")

    display_region = region_summary[
        [
            "Country",
            "Customers",
            "Revenue_at_Risk",
            "Expected_Recovery",
            "Revenue_Leakage"
        ]
    ].copy()

    display_region.columns = [
        "Region",
        "Customers",
        "Revenue at Risk",
        "Expected Recovery",
        "Revenue Leakage"
    ]

    st.dataframe(
        display_region,
        use_container_width=True,
        hide_index=True
    )

    # ------------------------------------------
    # Visual chart
    # ------------------------------------------

    st.subheader("Revenue Leakage by Region")

    chart_data = display_region.set_index(
        "Region"
    )[["Revenue Leakage"]]

    st.bar_chart(
        chart_data
    )

    # ------------------------------------------
    # AI insight
    # ------------------------------------------

    st.subheader("AI Regional Insight")

    st.info(
        f"""
        **Highest leakage detected in: {top_region['Country']}**

        Revenue at Risk:
        **£{top_region['Revenue_at_Risk']:,.0f}**

        Expected Recovery:
        **£{top_region['Expected_Recovery']:,.0f}**

        Estimated Revenue Leakage:
        **£{top_region['Revenue_Leakage']:,.0f}**

        RecoverAI recommends prioritizing recovery efforts
        in this region.
        """
    )

else:

    st.info(
        "No customer data available for leakage analysis."
    )
   # ============================================================
# 🤖 AUTONOMOUS AI RECOVERY AGENT
# ============================================================

st.divider()

st.header(" Autonomous AI Recovery Agent")

st.write(
    "RecoverAI observes customer risk, analyzes recovery probability, "
    "selects the best action, checks AI guardrails, executes recovery "
    "and learns from the result."
)

# ------------------------------------------------------------
# CUSTOMER SELECTION
# ------------------------------------------------------------

agent_customer_ids = (
    filtered_df["CustomerID"]
    .dropna()
    .astype(int)
    .unique()
    .tolist()
)

selected_agent_customer = st.selectbox(
    " Select customer for Autonomous Agent",
    agent_customer_ids,
    key="agent_customer_selector"
)

# ------------------------------------------------------------
# SELECT CUSTOMER DATA
# ------------------------------------------------------------

agent_customer = filtered_df[
    filtered_df["CustomerID"].astype(int)
    == int(selected_agent_customer)
].iloc[0]

risk_score = float(agent_customer["risk_score"])
recovery_probability = float(
    agent_customer["recovery_probability"]
)
expected_recovery = float(
    agent_customer["expected_recovery"]
)

# ------------------------------------------------------------
# AGENT OBSERVATION
# ------------------------------------------------------------

st.subheader("Agent Observation")

obs1, obs2, obs3 = st.columns(3)

with obs1:
    st.metric(
        "Risk Score",
        f"{risk_score:.0f}/100"
    )

with obs2:
    st.metric(
        "Recovery Probability",
        f"{recovery_probability:.1f}%"
    )

with obs3:
    st.metric(
        "Expected Recovery",
        f"£{expected_recovery:,.0f}"
    )

# ------------------------------------------------------------
# AI DECISION PREVIEW
# ------------------------------------------------------------

st.subheader(" AI Decision")

# Create temporary agent to calculate decision
preview_agent = RecoveryAgent(
    customer_id=int(selected_agent_customer),
    risk_score=risk_score,
    recovery_probability=recovery_probability,
    expected_recovery=expected_recovery
)

preview_action = preview_agent.decide()
preview_analysis = preview_agent.analyze_customer()
# ============================================================
# AI DECISION PREVIEW
# ============================================================

preview_action = preview_agent.decide()

# Generate explanation directly from customer data
if preview_agent.risk_score >= 70:
    preview_risk = "HIGH"
elif preview_agent.risk_score >= 40:
    preview_risk = "MEDIUM"
else:
    preview_risk = "LOW"

if preview_agent.recovery_probability >= 70:
    preview_reason = (
        f"Recovery probability is high at "
        f"{preview_agent.recovery_probability:.1f}%. "
        f"The AI agent recommends {preview_action}."
    )

elif preview_agent.recovery_probability >= 50:
    preview_reason = (
        f"Customer has {preview_risk} risk with "
        f"{preview_agent.recovery_probability:.1f}% recovery probability. "
        f"The AI agent selected {preview_action} as the next recovery action."
    )

else:
    preview_reason = (
        f"Recovery probability is relatively low at "
        f"{preview_agent.recovery_probability:.1f}%. "
        f"The AI agent is taking a conservative approach using {preview_action}."
    )

st.markdown("### 🤖 AI Agent Decision")

st.info(
    f"**Selected Action:** {preview_action}"
)

st.write(
    f"**Reason:** {preview_reason}"
)

st.write(
    f"**Risk Level:** {preview_risk}"
)
# ------------------------------------------------------------
# AI GUARDRAIL PREVIEW
# ------------------------------------------------------------

st.subheader(" AI Guardrail Check")

allowed, guardrail_message = preview_agent.guardrail_check(
    preview_action
)

if allowed:

    st.success(
        f"✅ Guardrail Passed — {guardrail_message}"
    )

else:

    st.warning(
        f"⚠️ Guardrail Triggered — {guardrail_message}"
    )

# ------------------------------------------------------------
# HUMAN APPROVAL
# ------------------------------------------------------------

if (
    preview_action == "Payment Recovery Link"
    and risk_score >= 90
):

    st.warning(
        "Human approval is required before this "
        "high-risk recovery action can execute."
    )

    approval = st.checkbox(
        "👤 I approve this recovery action",
        key=f"approval_{selected_agent_customer}"
    )

else:

    approval = True

# ------------------------------------------------------------
# RUN AGENT
# ------------------------------------------------------------

run_agent = st.button(
    "⚡ Run Autonomous Recovery Agent",
    use_container_width=True,
    type="primary"
)

if run_agent:

    if not approval:

        st.error(
            "❌ Recovery blocked. Human approval is required."
        )

    else:

        # Create actual autonomous agent
        agent = RecoveryAgent(
            customer_id=int(selected_agent_customer),
            risk_score=risk_score,
            recovery_probability=recovery_probability,
            expected_recovery=expected_recovery
        )

        # Run autonomous loop
        history = agent.run_agent()

        # Save results in session
        st.session_state["agent_history"] = history
        st.session_state["agent_memory"] = agent.get_memory()
        st.session_state["agent_summary"] = agent.get_summary()

        st.success(
            "Autonomous Recovery Agent completed its workflow!"
        )

# ============================================================
# DISPLAY AGENT RESULTS
# ============================================================

if "agent_history" in st.session_state:

    history = st.session_state["agent_history"]
    memory = st.session_state["agent_memory"]
    summary = st.session_state["agent_summary"]

    st.divider()

    # --------------------------------------------------------
    # AGENT STATUS
    # --------------------------------------------------------

    st.subheader("🤖 Agent Status")

    status = summary["status"]

    if status == "RECOVERED":

        st.success(
            f"✅ RECOVERED — £{summary['expected_recovery']:,.2f}"
        )

    elif status == "WAITING_FOR_APPROVAL":

        st.warning(
            "👤 WAITING FOR HUMAN APPROVAL"
        )

    elif status == "STOPPED":

        st.info(
            " Agent stopped according to recovery policy."
        )

    else:

        st.warning(
            f"⚠️ Agent status: {status}"
        )

    # --------------------------------------------------------
    # AGENT ACTIVITY LOG
    # --------------------------------------------------------

    st.subheader(" Agent Activity Log")

    for item in history:

        step = item["step"]
        action = item["action"]
        result = item["result"]

        result_type = result.get(
            "result",
            "UNKNOWN"
        )

        if result_type == "SUCCESS":

            icon = "✅"

        elif result_type == "FAILED":

            icon = "❌"

        elif result_type == "BLOCKED":

            icon = "🛡️"

        else:

            icon = "ℹ️"

        st.write(
            f"**Step {step}** → "
            f" Observe → "
            f" Decide → "
            f" {action} → "
            f"{icon} {result_type}"
        )

        if "message" in result:

            st.caption(
                result["message"]
            )

    # --------------------------------------------------------
    # RECOVERY MEMORY
    # --------------------------------------------------------

    st.subheader(" Recovery Memory")

    mem1, mem2, mem3 = st.columns(3)

    with mem1:

        st.metric(
            "Attempts",
            summary["attempts"]
        )

    with mem2:

        st.metric(
            "Actions Taken",
            len(summary["actions_taken"])
        )

    with mem3:

        st.metric(
            "Recovered",
            "YES" if summary["recovered"]
            else "NO"
        )

    if summary["actions_taken"]:

        st.write("**Previous Actions:**")

        for action in summary["actions_taken"]:

            st.write(
                f"• {action}"
            )

    # --------------------------------------------------------
    # EXPLAINABLE AI
    # --------------------------------------------------------

    st.subheader(" Explainable AI")

    st.write(
        f"""
        **Customer:** {summary['customer_id']}

        **Risk Score:** {summary['risk_score']:.0f}/100

        **Recovery Probability:** \
        {summary['recovery_probability']:.1f}%

        **Expected Recovery:** \
        £{summary['expected_recovery']:,.2f}

        **AI Strategy:** The agent evaluates customer risk,
        recovery probability and previous actions before
        selecting the next recovery action.
        """
    )

    # --------------------------------------------------------
    # FULL AGENT MEMORY
    # --------------------------------------------------------

    with st.expander("View Full Agent Memory"):

        for memory_item in memory["history"]:

            st.json(memory_item)
st.divider()
st.markdown("""
<div style="text-align:center; padding:10px 0; color:#667085; font-size:12px;">
    <b>RecoverAI</b> • Autonomous Revenue Recovery Platform
    <br>Decision-support prototype with simulated recovery outcomes.
</div>
""", unsafe_allow_html=True)
