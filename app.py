"""
Project: Streamlit Interactive Reference & Component Showcase
Author: skirfanwakil 306
Description: A comprehensive interactive documentation app demonstrating core 
             Streamlit components alongside live rendered outputs and code syntax.
"""

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Streamlit Interactive Reference",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("📘 Streamlit Interactive Reference & Component Showcase")
st.markdown(
    "Explore core Streamlit modules with real-time rendered outputs alongside their exact implementation syntax."
)
st.markdown("---")

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
st.sidebar.header("📌 Module Navigation")
selected_module = st.sidebar.radio(
    "Select a Component Module:",
    [
        "1. Typography & Text Elements",
        "2. Interactive Input Widgets",
        "3. Key Performance Metrics",
        "4. Layout Containers (Columns, Tabs, Expanders)",
        "5. Tabular Data Presentation",
        "6. Data Visualization (Native & Matplotlib)",
        "7. State Management & Caching",
    ],
)

# ==========================================
# MODULE 1: TYPOGRAPHY & TEXT ELEMENTS
# ==========================================
if selected_module == "1. Typography & Text Elements":
    st.header("1. Typography & Text Elements")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Rendered Output:")
        st.title("Primary Application Title")
        st.header("Section Header")
        st.subheader("Subsection Header")
        st.write("Standard body text rendered via `st.write()`.")
        st.markdown("Formatted text supporting **bold**, *italics*, and inline code.")

    with col2:
        st.subheader("Implementation Syntax:")
        st.code(
            '''
st.title("Primary Application Title")
st.header("Section Header")
st.subheader("Subsection Header")
st.write("Standard body text rendered via st.write().")
st.markdown("Formatted text supporting **bold**, *italics*, and inline code.")
        ''',
            language="python",
        )

# ==========================================
# MODULE 2: INTERACTIVE INPUT WIDGETS
# ==========================================
elif selected_module == "2. Interactive Input Widgets":
    st.header("2. Interactive Input Widgets")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Rendered Output:")
        user_name = st.text_input("Enter Operator Name:", "skirfanwakil")
        specialization = st.selectbox(
            "Select Domain Specialization:",
            ("Information Technology", "Data Science", "Software Engineering"),
        )
        proficiency = st.slider(
            "Select Proficiency Rating:", min_value=1, max_value=10, value=8
        )

        if st.button("Confirm Selection"):
            st.success(
                f"Profile Verified: {user_name} | Domain: {specialization} | Rating: {proficiency}/10"
            )

    with col2:
        st.subheader("Implementation Syntax:")
        st.code(
            '''
user_name = st.text_input("Enter Operator Name:", "skirfanwakil")
specialization = st.selectbox(
    "Select Domain Specialization:", 
    ("Information Technology", "Data Science", "Software Engineering")
)
proficiency = st.slider("Select Proficiency Rating:", min_value=1, max_value=10, value=8)

if st.button("Confirm Selection"):
    st.success(f"Profile Verified: {user_name} | Domain: {specialization} | Rating: {proficiency}/10")
        ''',
            language="python",
        )

# ==========================================
# MODULE 3: KEY PERFORMANCE METRICS
# ==========================================
elif selected_module == "3. Key Performance Metrics":
    st.header("3. Key Performance Metrics (KPI Cards)")

    st.subheader("Rendered Output:")
    m1, m2, m3 = st.columns(3)
    m1.metric(label="Total Sales Volume", value="1,320 Units", delta="+12.4%")
    m2.metric(label="Gross Revenue", value="₹45,000", delta="+8.2%")
    m3.metric(label="Bounce Rate", value="24.0%", delta="-3.1%")

    st.subheader("Implementation Syntax:")
    st.code(
        '''
m1, m2, m3 = st.columns(3)
m1.metric(label="Total Sales Volume", value="1,320 Units", delta="+12.4%")
m2.metric(label="Gross Revenue", value="₹45,000", delta="+8.2%")
m3.metric(label="Bounce Rate", value="24.0%", delta="-3.1%")
    ''',
        language="python",
    )

# ==========================================
# MODULE 4: LAYOUT CONTAINERS
# ==========================================
elif selected_module == "4. Layout Containers (Columns, Tabs, Expanders)":
    st.header("4. Layout Containers (Columns, Tabs, Expanders)")

    st.subheader("Rendered Output:")
    tab_cols, tab_exp = st.tabs(["Grid Columns Layout", "Collapsible Expander"])

    with tab_cols:
        c1, c2 = st.columns(2)
        c1.info("Primary Left Container")
        c2.warning("Secondary Right Container")

    with tab_exp:
        with st.expander("View Technical Specifications"):
            st.write(
                "Expanders allow supplementary metadata or documentation to remain collapsed until requested."
            )

    st.subheader("Implementation Syntax:")
    st.code(
        '''
tab_cols, tab_exp = st.tabs(["Grid Columns Layout", "Collapsible Expander"])

with tab_cols:
    c1, c2 = st.columns(2)
    c1.info("Primary Left Container")
    c2.warning("Secondary Right Container")

with tab_exp:
    with st.expander("View Technical Specifications"):
        st.write("Expanders allow supplementary metadata or documentation to remain collapsed until requested.")
    ''',
        language="python",
    )

# ==========================================
# MODULE 5: TABULAR DATA PRESENTATION
# ==========================================
elif selected_module == "5. Tabular Data Presentation":
    st.header("5. Tabular Data Presentation (Interactive vs. Static)")

    df_sample = pd.DataFrame({
        "Timeline": ["Mon", "Tue", "Wed", "Thu", "Fri"],
        "Revenue_Units": [120, 250, 190, 340, 420],
    })

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Rendered Output (`st.dataframe`):")
        st.dataframe(df_sample, use_container_width=True)

    with col2:
        st.subheader("Implementation Syntax:")
        st.code(
            '''
import pandas as pd

df_sample = pd.DataFrame({
    "Timeline": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Revenue_Units": [120, 250, 190, 340, 420]
})

# Interactive table supporting sorting and scrolling
st.dataframe(df_sample, use_container_width=True)

# Static table alternative: st.table(df_sample)
        ''',
            language="python",
        )

# ==========================================
# MODULE 6: DATA VISUALIZATION
# ==========================================
elif selected_module == "6. Data Visualization (Native & Matplotlib)":
    st.header("6. Data Visualization (Native & Matplotlib)")

    df_viz = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
        "Sales": [12, 28, 19, 34, 42],
        "Visitors": [120, 210, 175, 290, 360],
        "Duration_Min": [85, 92, 110, 78, 105],
    })

    tab_native, tab_mpl = st.tabs([
        "Streamlit Native Charts",
        "Matplotlib Charts (Pie, Hist, Barh)",
    ])

    # --- TAB 1: STREAMLIT NATIVE CHARTS ---
    with tab_native:
        st.subheader("1. Line Chart (`st.line_chart`)")
        c1, c2 = st.columns(2)
        with c1:
            st.line_chart(df_viz.set_index("Day")["Sales"])
        with c2:
            st.code(
                'st.line_chart(df_viz.set_index("Day")["Sales"])',
                language="python",
            )

        st.markdown("---")
        st.subheader("2. Bar Chart (`st.bar_chart`)")
        c1, c2 = st.columns(2)
        with c1:
            st.bar_chart(df_viz.set_index("Day")["Sales"])
        with c2:
            st.code(
                'st.bar_chart(df_viz.set_index("Day")["Sales"])',
                language="python",
            )

        st.markdown("---")
        st.subheader("3. Area Chart (`st.area_chart`)")
        c1, c2 = st.columns(2)
        with c1:
            st.area_chart(df_viz.set_index("Day")["Visitors"])
        with c2:
            st.code(
                'st.area_chart(df_viz.set_index("Day")["Visitors"])',
                language="python",
            )

        st.markdown("---")
        st.subheader("4. Scatter Chart (`st.scatter_chart`)")
        c1, c2 = st.columns(2)
        with c1:
            st.scatter_chart(df_viz, x="Visitors", y="Sales")
        with c2:
            st.code(
                'st.scatter_chart(df_viz, x="Visitors", y="Sales")',
                language="python",
            )

    # --- TAB 2: MATPLOTLIB CHARTS ---
    with tab_mpl:
        st.subheader("5. Pie Chart (`ax.pie`)")
        c1, c2 = st.columns(2)
        with c1:
            fig_pie, ax_pie = plt.subplots(figsize=(4, 3))
            ax_pie.pie(
                df_viz["Sales"],
                labels=df_viz["Day"],
                autopct="%1.1f%%",
                startangle=90,
            )
            ax_pie.axis("equal")
            st.pyplot(fig_pie)
        with c2:
            st.code(
                '''fig, ax = plt.subplots(figsize=(4, 3))
ax.pie(df_viz["Sales"], labels=df_viz["Day"], autopct="%1.1f%%", startangle=90)
ax.axis("equal")
st.pyplot(fig)''',
                language="python",
            )

        st.markdown("---")
        st.subheader("6. Histogram (`ax.hist`)")
        c1, c2 = st.columns(2)
        with c1:
            fig_hist, ax_hist = plt.subplots(figsize=(5, 3))
            ax_hist.hist(df_viz["Duration_Min"], bins=5, edgecolor="black")
            ax_hist.set_xlabel("Duration (Minutes)")
            ax_hist.set_ylabel("Frequency")
            st.pyplot(fig_hist)
        with c2:
            st.code(
                '''fig, ax = plt.subplots(figsize=(5, 3))
ax.hist(df_viz["Duration_Min"], bins=5, edgecolor="black")
ax.set_xlabel("Duration (Minutes)")
ax.set_ylabel("Frequency")
st.pyplot(fig)''',
                language="python",
            )

        st.markdown("---")
        st.subheader("7. Horizontal Bar Chart (`ax.barh`)")
        c1, c2 = st.columns(2)
        with c1:
            fig_barh, ax_barh = plt.subplots(figsize=(5, 3))
            ax_barh.barh(df_viz["Day"], df_viz["Sales"])
            ax_barh.set_xlabel("Sales Volume")
            st.pyplot(fig_barh)
        with c2:
            st.code(
                '''fig, ax = plt.subplots(figsize=(5, 3))
ax.barh(df_viz["Day"], df_viz["Sales"])
ax.set_xlabel("Sales Volume")
st.pyplot(fig)''',
                language="python",
            )

# ==========================================
# MODULE 7: STATE MANAGEMENT & CACHING
# ==========================================
elif selected_module == "7. State Management & Caching":
    st.header("7. Session State Management (`st.session_state`)")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Rendered Output:")
        if "counter" not in st.session_state:
            st.session_state.counter = 0

        if st.button("Increment Counter (+1)"):
            st.session_state.counter += 1

        st.write(f"Persistent Counter Value: **{st.session_state.counter}**")

    with col2:
        st.subheader("Implementation Syntax:")
        st.code(
            '''
# Persist variable values across script reruns
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment Counter (+1)"):
    st.session_state.counter += 1

st.write(f"Persistent Counter Value: {st.session_state.counter}")
        ''',
            language="python",
        )

# ==========================================
# FOOTER
# ==========================================
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>Streamlit Interactive Reference | Developed by <b>skirfanwakil 306</b></div>",
    unsafe_allow_html=True,
)
