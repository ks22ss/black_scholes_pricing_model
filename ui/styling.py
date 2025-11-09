"""
CSS styling definitions for the Option Pricing and Risk Analyzer application
"""


def get_dark_mode_css():
    """Returns the comprehensive dark mode CSS styling"""
    return """
    <style>
    /* Main app background */
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    
    /* Top header/navigation */
    header[data-testid="stHeader"] {
        background-color: #1e1e1e;
        border-bottom: 1px solid #333;
    }
    
    /* Main container */
    .main .block-container {
        background-color: #0e1117;
        color: #fafafa;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #1e1e1e;
        color: #fafafa;
    }
    
    section[data-testid="stSidebar"] > div {
        background-color: #1e1e1e;
    }
    
    /* Sidebar header */
    .css-1d391kg {
        background-color: #1e1e1e;
    }
    
    /* All text elements */
    h1, h2, h3, h4, h5, h6, p, label, span, div {
        color: #fafafa !important;
    }
    
    /* Input fields */
    .stNumberInput > div > div > input,
    .stSlider > div > div > input,
    .stTextInput > div > div > input {
        background-color: #262730;
        color: #fafafa;
        border: 1px solid #444;
    }
    
    .stNumberInput label,
    .stSlider label,
    .stTextInput label {
        color: #fafafa !important;
    }
    
    /* Slider track */
    .stSlider > div > div > div {
        background-color: #262730;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #262730;
        color: #fafafa;
        border: 1px solid #444;
    }
    
    .stButton > button:hover {
        background-color: #333;
        border-color: #555;
    }
    
    /* DataFrames/Tables */
    .stDataFrame,
    .dataframe {
        background-color: #1e1e1e;
        color: #fafafa;
    }
    
    .stDataFrame table,
    .dataframe table {
        background-color: #1e1e1e;
        color: #fafafa;
    }
    
    .stDataFrame th,
    .dataframe th {
        background-color: #262730;
        color: #fafafa;
    }
    
    .stDataFrame td,
    .dataframe td {
        background-color: #1e1e1e;
        color: #fafafa;
    }
    
    /* Dividers */
    hr {
        border-color: #333;
    }
    
    /* Metrics */
    .stMetric {
        background-color: #262730;
        padding: 10px;
        border-radius: 5px;
        color: #fafafa;
    }
    
    .stMetric label {
        color: #aaa !important;
    }
    
    .stMetric [data-testid="stMetricValue"] {
        color: #fafafa !important;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #fafafa !important;
    }
    
    /* Call value box */
    .call-value-box {
        background-color: #2d5a3d;
        color: #90ee90;
        padding: 10px;
        border-radius: 15px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 10px;
        border: 2px solid #4a7c59;
    }
    
    /* Put value box */
    .put-value-box {
        background-color: #5a2d3d;
        color: #ffb6c1;
        padding: 10px;
        border-radius: 15px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 10px;
        border: 2px solid #7c4a5a;
    }
    
    /* Streamlit widget labels */
    .stNumberInput label,
    .stSlider label,
    .stTextInput label,
    .stSelectbox label {
        color: #fafafa !important;
    }
    
    /* Sidebar text */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] span {
        color: #fafafa !important;
    }
    
    /* Success/Error messages */
    .stSuccess {
        background-color: #1e3a1e;
        color: #90ee90;
    }
    
    .stError {
        background-color: #3a1e1e;
        color: #ff6b6b;
    }
    
    /* Info boxes */
    .stInfo {
        background-color: #1e1e3a;
        color: #87ceeb;
    }
    
    /* Additional Streamlit component styling */
    .element-container {
        color: #fafafa;
    }
    
    /* Number input styling */
    input[type="number"] {
        background-color: #262730 !important;
        color: #fafafa !important;
    }
    
    /* Selectbox dropdown */
    .stSelectbox > div > div > select {
        background-color: #262730;
        color: #fafafa;
    }
    
    /* Checkbox */
    .stCheckbox label {
        color: #fafafa !important;
    }
    
    /* Radio buttons */
    .stRadio label {
        color: #fafafa !important;
    }
    
    /* Text area */
    textarea {
        background-color: #262730;
        color: #fafafa;
        border: 1px solid #444;
    }
    
    /* Streamlit's default text color override */
    .stMarkdown {
        color: #fafafa;
    }
    
    /* Sidebar navigation */
    [data-testid="stSidebarNav"] {
        background-color: #1e1e1e;
    }
    
    /* Main content area */
    .main {
        background-color: #0e1117;
    }
    
    /* Plotly chart container */
    .js-plotly-plot {
        background-color: transparent;
    }
    </style>
    """


def get_title_css():
    """Returns CSS for compact title styling"""
    return """
    <style>
    h1 {
        font-size: 28px !important;
        margin-bottom: 10px !important;
        margin-top: 10px !important;
    }
    </style>
    """


def get_params_box_css():
    """Returns CSS for the parameters display box"""
    return """
    <style>
    .params-box {
        background-color: #1e3a5f;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
    }
    .params-row {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        gap: 10px;
    }
    .param-item {
        flex: 1;
        min-width: 120px;
        text-align: center;
    }
    .param-label {
        font-size: 11px;
        color: #b0c4de;
        margin-bottom: 3px;
        font-weight: 500;
    }
    .param-value {
        font-size: 16px;
        color: #ffffff;
        font-weight: bold;
    }
    </style>
    """

