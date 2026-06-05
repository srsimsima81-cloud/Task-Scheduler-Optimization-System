import streamlit as st
import pandas as pd
import plotly.express as px
import heapq

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Task Scheduler Optimization System",
    page_icon="⚡",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(
        135deg,
        #050816,
        #0B1026,
        #111827
    );
    color: white;
}

/* Hide Streamlit menu */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Title */
.main-title{
    text-align:center;
    font-size:3.2rem;
    font-weight:bold;
    color:#00F5FF;
    text-shadow:
        0 0 10px #00F5FF,
        0 0 20px #00F5FF,
        0 0 40px #00F5FF;
}

/* Hero Card */
.glass-card{
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(15px);
    border-radius:20px;
    padding:25px;
    border:1px solid rgba(255,255,255,0.1);
    box-shadow:0 0 20px rgba(0,245,255,0.25);
    margin-bottom:20px;
}

/* KPI Card */
.metric-card{
    background:#0F172A;
    border-radius:20px;
    padding:20px;
    text-align:center;
    box-shadow:0 0 15px #00F5FF;
}

/* Buttons */
.stButton button{
    width:100%;
    background:linear-gradient(
        90deg,
        #00F5FF,
        #7C3AED
    );
    color:white;
    border:none;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
    padding:12px;
    box-shadow:
        0 0 15px #00F5FF,
        0 0 25px #7C3AED;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#0B1026;
}

/* Tables */
[data-testid="stDataFrame"]{
    border-radius:15px;
    overflow:hidden;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.markdown("""
# ⏱️ Scheduler AI

### Premium Optimization Dashboard

**Algorithms Used**

- Heap
- Priority Queue
- Greedy Scheduling
- Deadline Optimization
""")

# --------------------------------------------------
# TASK CLASS
# --------------------------------------------------

class Task:
    def __init__(
        self,
        name,
        priority,
        deadline,
        duration,
        profit
    ):
        self.name = name
        self.priority = priority
        self.deadline = deadline
        self.duration = duration
        self.profit = profit

# --------------------------------------------------
# SCHEDULING ALGORITHM
# --------------------------------------------------

def schedule_tasks(tasks):

    tasks = sorted(
        tasks,
        key=lambda x: (
            x.deadline,
            -x.priority
        )
    )

    scheduled = []
    missed = []

    current_time = 0
    total_profit = 0

    for task in tasks:

        if (
            current_time +
            task.duration
            <= task.deadline
        ):

            scheduled.append(task)

            current_time += task.duration

            total_profit += task.profit

        else:

            missed.append(task)

    return (
        scheduled,
        missed,
        total_profit
    )

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    """
    <h1 class="main-title">
    ⏱️ TASK SCHEDULER OPTIMIZATION SYSTEM
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="glass-card">
    <h3>⏱️ Intelligent Task Scheduling</h3>

    Optimize tasks using:

    ✔ Greedy Algorithms<br>
    ✔ Heap Priority Queue<br>
    ✔ Deadline Constraints<br>
    ✔ Profit Maximization<br>
    ✔ Real-Time Visualization

    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# INPUTS
# --------------------------------------------------

st.sidebar.header("Add New Task")

task_name = st.sidebar.text_input("Task Name")

priority = st.sidebar.slider(
    "Priority",
    1,
    10,
    5
)

deadline = st.sidebar.number_input(
    "Deadline",
    min_value=1,
    value=5
)

duration = st.sidebar.number_input(
    "Duration",
    min_value=1,
    value=1
)

profit = st.sidebar.number_input(
    "Profit",
    min_value=1,
    value=100
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "tasks" not in st.session_state:

    st.session_state.tasks = [

        Task("Task A",5,4,2,100),
        Task("Task B",4,3,1,80),
        Task("Task C",3,2,2,60),
        Task("Task D",2,5,1,40),

    ]

# --------------------------------------------------
# ADD TASK
# --------------------------------------------------

if st.sidebar.button("➕ Add Task"):

    if task_name.strip():

        st.session_state.tasks.append(
            Task(
                task_name,
                priority,
                deadline,
                duration,
                profit
            )
        )

        st.sidebar.success("Task Added")

# --------------------------------------------------
# CURRENT TASK TABLE
# --------------------------------------------------

st.subheader("📋 Current Tasks")

task_df = pd.DataFrame([
    {
        "Task": t.name,
        "Priority": t.priority,
        "Deadline": t.deadline,
        "Duration": t.duration,
        "Profit": t.profit
    }
    for t in st.session_state.tasks
])

st.dataframe(
    task_df,
    use_container_width=True
)

# --------------------------------------------------
# OPTIMIZE BUTTON
# --------------------------------------------------

if st.button("✨ Optimize Schedule"):

    scheduled, missed, total_profit = schedule_tasks(
        st.session_state.tasks
    )

    # KPI CARDS

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div class="metric-card">
            <h1>{len(scheduled)}</h1>
            <h4>Scheduled Tasks</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="metric-card">
            <h1>{len(missed)}</h1>
            <h4>Missed Tasks</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="metric-card">
            <h1>{total_profit}</h1>
            <h4>Total Profit</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # ---------------------
    # SCHEDULED TASKS
    # ---------------------

    st.subheader("✅ Scheduled Tasks")

    scheduled_df = pd.DataFrame([
        {
            "Task": t.name,
            "Deadline": t.deadline,
            "Duration": t.duration,
            "Profit": t.profit
        }
        for t in scheduled
    ])

    st.dataframe(
        scheduled_df,
        use_container_width=True
    )

    # ---------------------
    # MISSED TASKS
    # ---------------------

    st.subheader("❌ Missed Tasks")

    missed_df = pd.DataFrame([
        {
            "Task": t.name,
            "Deadline": t.deadline,
            "Duration": t.duration,
            "Profit": t.profit
        }
        for t in missed
    ])

    st.dataframe(
        missed_df,
        use_container_width=True
    )

    # ---------------------
    # EXECUTION TIMELINE
    # ---------------------

    st.subheader("📈 Execution Timeline")

    timeline = []

    base_time = pd.Timestamp("2025-01-01 09:00:00")

    current_time = 0

    for task in scheduled:

        start_time = (
            base_time +
            pd.Timedelta(hours=current_time)
        )

        finish_time = (
            base_time +
            pd.Timedelta(
                hours=current_time + task.duration
            )
        )

        timeline.append({
            "Task": task.name,
            "Start": start_time,
            "Finish": finish_time
        })

        current_time += task.duration

    if len(timeline) > 0:

        gantt_df = pd.DataFrame(timeline)

        fig = px.timeline(
            gantt_df,
            x_start="Start",
            x_end="Finish",
            y="Task",
            color="Task"
        )

        fig.update_yaxes(
            autorange="reversed"
        )

        fig.update_layout(
            paper_bgcolor="#0B1026",
            plot_bgcolor="#0B1026",
            font_color="white",
            height=650,
            title="⚡ Premium Task Execution Timeline",
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.warning(
            "No scheduled tasks available."
        )