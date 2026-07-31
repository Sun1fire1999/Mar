import streamlit as st
import pandas as pd
from datetime import datetime
import os

# ==========================
# 🎯 إعدادات التطبيق الأساسية
# ==========================
def setup_application():
    env_config = {
        "APP_INFO": {
            "APP_NAME": "SiraWork منصـة سـيرا القانونـية",
            "VERSION": "v2.0.0",
            "DESCRIPTION": "منصة توعوية تعليمية تهدف إلى نشر الوعي القانوني في مجال قانون التجارة وتوفير أدوات تعليمية تفاعلية للمستخدمين"
        },
        "FOOTER": {
            "TEXT": "© 2025 SiraWork سيرا — جميع الحقوق محفوظة"
        }
    }
    return env_config

config = setup_application()

# إعداد صفحة Streamlit
st.set_page_config(
    page_title="SiraWork سيرا",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# 🎨 التصميم الفاتح الاحترافي
# ==========================
def load_custom_css():
    st.markdown("""
    <style>
    /* التصميم الفاتح الاحترافي */
    .stApp {
        background-color: #FFFFFF !important;
        color: #1F2937 !important;
    }
    
    /* تحسينات عامة للنص */
    .main * {
        color: #1F2937 !important;
    }
    
    /* تصميم الهيدر البسيط */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        margin-bottom: 2rem;
        border-bottom: 1px solid #E5E7EB;
    }
    
    .platform-name {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E40AF !important;
        margin-bottom: 0.5rem;
    }
    
    .platform-subtitle {
        font-size: 1.2rem;
        color: #6B7280 !important;
        font-weight: 400;
    }
    
    /* تصميم البطاقات البسيط */
    .section-card {
        background: #FFFFFF;
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #E5E7EB;
        margin: 1rem 0;
        transition: all 0.2s ease;
    }
    
    .section-card:hover {
        border-color: #1E40AF;
    }
    
    /* تصميم العناصر التفاعلية */
    .feature-item {
        background: #F9FAFB;
        padding: 1rem;
        border-radius: 6px;
        margin: 0.5rem 0;
        border-left: 4px solid #1E40AF;
        transition: all 0.2s ease;
    }
    
    .feature-item:hover {
        background: #F3F4F6;
    }
    
    /* تصميم التبويبات البسيط */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0px;
        background: #FFFFFF;
        border-bottom: 1px solid #E5E7EB;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: #FFFFFF !important;
        color: #6B7280 !important;
        border-radius: 0px !important;
        padding: 12px 24px !important;
        margin: 0px !important;
        border: none !important;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        color: #1E40AF !important;
        background: #F9FAFB !important;
    }
    
    .stTabs [aria-selected="true"] {
        color: #1E40AF !important;
        background: #FFFFFF !important;
        border-bottom: 2px solid #1E40AF !important;
    }
    
    /* تصميم الأزرار */
    .stButton button {
        background: #1E40AF !important;
        color: white !important;
        border: none !important;
        border-radius: 6px !important;
        padding: 10px 20px !important;
        font-weight: 500 !important;
    }
    
    .stButton button:hover {
        background: #1E3A8A !important;
    }
    
    /* تصميم المدخلات */
    .stTextInput input, 
    .stNumberInput input, 
    .stSelectbox select {
        background: #FFFFFF !important;
        color: #1F2937 !important;
        border: 1px solid #D1D5DB !important;
        border-radius: 6px !important;
    }
    
    .stTextInput input:focus, 
    .stNumberInput input:focus, 
    .stSelectbox select:focus {
        border-color: #1E40AF !important;
        box-shadow: 0 0 0 2px rgba(30, 64, 175, 0.1) !important;
    }
    
    /* تصميم الشريط الجانبي */
    section[data-testid="stSidebar"] {
        background: #F9FAFB !important;
        border-right: 1px solid #E5E7EB !important;
    }
    
    /* تحسينات للجوال */
    @media (max-width: 768px) {
        .platform-name {
            font-size: 2rem !important;
        }
        .platform-subtitle {
            font-size: 1rem !important;
        }
        .section-card {
            padding: 1rem !important;
        }
    }
    
    /* إزالة العناصر غير الضرورية */
    .stExpander {
        border: 1px solid #E5E7EB !important;
        border-radius: 6px !important;
    }
    
    /* تحسينات النتائج */
    .stSuccess {
        background: #D1FAE5 !important;
        border: 1px solid #10B981 !important;
        color: #065F46 !important;
    }
    
    .stInfo {
        background: #DBEAFE !important;
        border: 1px solid #3B82F6 !important;
        color: #1E40AF !important;
    }
    </style>
    """, unsafe_allow_html=True)

load_custom_css()

# ==========================
# 🧭 نظام التنقل المبسط
# ==========================
def setup_navigation():
    page_options = {
        "🏠 الرئيسية": "home",
        "🏢 التجار والأفراد": "traders",
        "🏛️ الشركات والمؤسسات": "companies", 
        "📝 العقود التجارية": "contracts",
        "💳 الأوراق التجارية": "commercial_papers",
        "🏦 الإفلاس والتسوية": "bankruptcy",
        "🔬 الباحثين": "researchers",
        "🧮 الحاسبات": "calculators",
        "⚙️ الإعدادات": "settings"
    }
    return page_options

def show_sidebar_navigation():
    """إظهار القائمة الجانبية المبسطة"""
    st.sidebar.markdown("""
    <div style="text-align: center; padding: 1.5rem 0; border-bottom: 1px solid #E5E7EB; margin-bottom: 1rem;">
        <h3 style="margin: 0; color: #1E40AF;">⚖️ SiraWork</h3>
        <p style="margin: 0; color: #6B7280; font-size: 0.9rem;">منصة القانون التجاري</p>
    </div>
    """, unsafe_allow_html=True)
    
    page_options = setup_navigation()
    
    for page_name, page_id in page_options.items():
        if st.sidebar.button(
            page_name, 
            key=f"nav_{page_id}",
            use_container_width=True
        ):
            st.session_state.selected_page = page_id
            st.rerun()

# ==========================
# 🧮 دوال مساعدة
# ==========================
def initialize_session_state():
    """تهيئة حالة الجلسة"""
    default_states = {
        'selected_page': 'home',
        'calculation_history': [],
        'user_type': None
    }
    
    for key, value in default_states.items():
        if key not in st.session_state:
            st.session_state[key] = value

def show_breadcrumbs(section_name):
    st.markdown(f"""
    <div style='
        background: #F9FAFB; 
        padding: 12px 16px; 
        border-radius: 6px; 
        margin-bottom: 20px; 
        border: 1px solid #E5E7EB;
        color: #6B7280;
        font-size: 0.9rem;
    '>
        <strong>المسار:</strong> الرئيسية ▶ {section_name}
    </div>
    """, unsafe_allow_html=True)

# ==========================
# 🏠 الصفحة الرئيسية - النسخة المحدثة
# ==========================
def show_home_page():
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 2.5rem 0;
        margin-bottom: 2rem;
        border-bottom: 1px solid #E5E7EB;
    }
    .platform-name {
        margin-bottom: 1.2rem;
    }
    .english-name {
        font-family: 'Arial', 'Helvetica', sans-serif;
        letter-spacing: 3px;
        margin-bottom: 0.2rem;
        font-size: 1.8rem;
        font-weight: 600;
        color: #1E40AF;
        line-height: 1.1;
    }
    .arabic-name {
        font-size: 1.6rem;
        color: #1E40AF;
        font-weight: 600;
        margin-top: 0.3rem;
    }
    .platform-subtitle {
        font-size: 1.1rem;
        color: #6B7280;
        font-weight: 400;
        line-height: 1.5;
        max-width: 600px;
        margin: 0 auto;
        padding-top: 0.3rem;
    }
    </style>

    <div class="main-header">
        <div class="platform-name">
            <div class="english-name">S I R A W O R K</div>
            <div class="arabic-name">منصة سيرا القانونية</div>
        </div>
        <div class="platform-subtitle">منصة توعوية تعليمية لنشر الوعي القانوني في مجال قانون التجارة الأردني</div>
    </div>
    """, unsafe_allow_html=True)

    # تنويه مهم
    st.markdown("""
    <div class="section-card">
        <h4>⚖️ تنويه هام</h4>
        <p>منصة توعوية تعليمية - المعلومات مقدمة لأغراض التعلم والمعرفة العامة ولا تغني عن استشارة المختصين.</p>
    </div>
    """, unsafe_allow_html=True)

    # الفئات المستهدفة
    st.markdown("### الفئات المستهدفة")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-item">
            <h4>🏢 التجار والأفراد</h4>
            <p>تعرف على حقوقك وواجباتك التجارية وكيفية إدارة الأعمال</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-item">
            <h4>🏛️ الشركات والمؤسسات</h4>
            <p>التزم بالتشريعات والقوانين التجارية والشركات</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-item">
            <h4>🔬 الباحثين</h4>
            <p>مواد بحثية ومراجع قانونية متخصصة في القانون التجاري</p>
        </div>
        """, unsafe_allow_html=True)

    # طريقة الاستخدام
    st.markdown("### طريقة الاستخدام")
    st.markdown("""
    <div class="section-card">
        <ol>
            <li><strong>اختر فئتك</strong> من القائمة الجانبية</li>
            <li><strong>انتقل إلى القسم المناسب</strong> لاحتياجاتك</li>
            <li><strong>استخدم الأدوات المتاحة</strong> في كل قسم</li>
            <li><strong>استفد من الحاسبات</strong> والنماذج الجاهزة</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

    # المواضيع الرئيسية
    st.markdown("### 📚 المواضيع الرئيسية في قانون التجارة")
    
    topics_col1, topics_col2 = st.columns(2)
    
    with topics_col1:
        st.markdown("""
        <div class="section-card">
            <h4>📋 الأعمال التجارية</h4>
            <p>• تعريف الأعمال التجارية (المواد 6-8)</p>
            <p>• أنواع الأعمال التجارية</p>
            <p>• الالتزامات العامة للتجار</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="section-card">
            <h4>🏪 السجل التجاري</h4>
            <p>• إجراءات القيد والتسجيل</p>
            <p>• البيانات الإلزامية</p>
            <p>• التحديثات والتعديلات</p>
        </div>
        """, unsafe_allow_html=True)
    
    with topics_col2:
        st.markdown("""
        <div class="section-card">
            <h4>📝 العقود التجارية</h4>
            <p>• عقود البيع التجاري</p>
            <p>• عقود النقل والتأمين</p>
            <p>• عقود الوكالة والسمسرة</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="section-card">
            <h4>💳 الأوراق التجارية</h4>
            <p>• الكمبيالة والسند الإذني</p>
            <p>• الشيكات والتظهير</p>
            <p>• الضمانات والرهون</p>
        </div>
        """, unsafe_allow_html=True)

# ==========================
# 🏢 قسم التجار والأفراد - وفق قانون التجارة الأردني
# ==========================
def show_traders_section():
    show_breadcrumbs("🏢 قسم التجار والأفراد")
    
    st.markdown("""
    <div class="main-header">
        <h1>🏢 منصة التجار والأفراد في الأردن</h1>
        <p>دليل شامل حسب قانون التجارة الأردني رقم 12 لسنة 1966 وتعديلاته</p>
    </div>
    """, unsafe_allow_html=True)

    # شريط المعلومات حسب القانون
    st.info("""
    **📢 أحكام قانون التجارة الأردني:** 
    - قانون التجارة رقم 12 لسنة 1966 وتعديلاته
    - قانون الشركات رقم 22 لسنة 1997
    - قانون حماية المستهلك رقم 16 لسنة 2004
    """)

    trader_tabs = st.tabs([
        "📋 الأحكام العامة", 
        "🏪 السجل التجاري",
        "📝 العقود التجارية",
        "💰 الأوراق التجارية", 
        "🏦 الإفلاس",
        "🔍 فحص الالتزامات"
    ])

    with trader_tabs[0]:
        show_general_commercial_provisions()

    with trader_tabs[1]:
        show_commercial_registry()

    with trader_tabs[2]:
        show_commercial_contracts()

    with trader_tabs[3]:
        show_commercial_papers()

    with trader_tabs[4]:
        show_bankruptcy_provisions()
        
    with trader_tabs[5]:
        show_compliance_checker()

# ==========================
# 📋 الأحكام العامة - قانون التجارة
# ==========================
def show_general_commercial_provisions():
    st.markdown("#### 📋 الأحكام العامة - حسب قانون التجارة الأردني")
    
    general_provisions = [
        {
            "title": "📄 تعريف التاجر - المادة 6",
            "content": """
            **التاجر وفق القانون:**
            - كل شخص طبيعي أو اعتباري يمارس الأعمال التجارية ويتخذها مهنة معتادة له
            - الأعمال التجارية هي التي يقوم بها التاجر لشؤون تجارته
            - يعتبر في حكم التاجر كل من سجل في السجل التجاري
            """
        },
        {
            "title": "🏪 الأعمال التجارية - المادة 5",
            "content": """
            **الأعمال التجارية بحسب القانون:**
            - شراء المنقولات لأجل بيعها بذاتها أو بعد تحويلها
            - استئجار المنقولات لأجل تأجيرها
            - الأعمال المصرفية والصرف والوساطة المالية
            - عمليات الشركات التجارية
            - عمليات السمسرة والوكالة بالعمولة
            """
        },
        {
            "title": "📚 الالتزامات العامة للتاجر - المواد 8-15",
            "content": """
            **الالتزامات الأساسية:**
            - القيد في السجل التجاري
            - مسك الدفاتر التجارية بشكل منتظم
            - الاحتفاظ بالمراسلات والمستندات لمدة 10 سنوات
            - الالتزام بقواعد الشرف والأمانة في المعاملات
            - الإفصاح عن المعلومات الأساسية للعملاء
            """
        }
    ]
    
    for provision in general_provisions:
        with st.expander(provision["title"], expanded=False):
            st.markdown(provision["content"])

# ==========================
# 🏪 السجل التجاري
# ==========================
def show_commercial_registry():
    st.markdown("#### 🏪 نظام السجل التجاري")
    
    registry_provisions = [
        {
            "title": "📝 إجراءات القيد - المادة 16",
            "content": """
            **شروط القيد في السجل التجاري:**
            - تقديم طلب خطي إلى دائرة السجل التجاري
            - إرفاق المستندات المطلوبة (هوية، سند ملكية المحل، إفادة بنكية)
            - دفع الرسوم المقررة
            - الحصول على شهادة القيد
            """
        },
        {
            "title": "📊 البيانات الإلزامية - المادة 18",
            "content": """
            **البيانات الواجب ذكرها:**
            - اسم التاجر وجنسيته وعنوانه
            - نوع التجارة ومحلها
            - رأس المال المخصص للتجارة
            - تاريخ بدء النشاط التجاري
            - أي تعديلات تطرأ على هذه البيانات
            """
        },
        {
            "title": "📑 الدفاتر التجارية - المواد 20-25",
            "content": """
            **الدفاتر الإلزامية:**
            - دفتر اليومية: تسجيل العمليات اليومية
            - دفتر الجرد: بيان المركز المالي
            - دفتر الأستاذ: تفصيل الحسابات
            - يجب حفظ الدفاتر لمدة 10 سنوات
            """
        }
    ]
    
    for provision in registry_provisions:
        with st.expander(provision["title"], expanded=False):
            st.markdown(provision["content"])

# ==========================
# 📝 العقود التجارية
# ==========================
def show_commercial_contracts():
    st.markdown("#### 📝 العقود التجارية")
    
    contract_types = [
        {
            "title": "🛒 عقد البيع التجاري - المواد 51-59",
            "content": """
            **خصائص البيع التجاري:**
            - نقل ملكية البضائع مقابل ثمن
            - يمكن أن يكون البيع نقداً أو آجلاً
            - يخضع للشروط العامة للعقود مع خصوصيات تجارية
            - يشمل نقل المخاطر والمنافع
            """
        },
        {
            "title": "🚚 عقد النقل التجاري - المواد 68-79",
            "content": """
            **أحكام النقل التجاري:**
            - نقل البضائع أو الأشخاص مقابل أجر
            - مسؤولية الناقل عن سلامة البضائع
            - مواعيد التسليم والاستلام
            - تعويضات التلف أو الفقدان
            """
        },
        {
            "title": "🤝 عقد الوكالة التجارية - المواد 80-98",
            "content": """
            **الوكالة بالعمولة:**
            - الوكيل يتصرف باسمه الخاص ولحساب الموكل
            - الالتزام بتعليمات الموكل
            - الحق في العمولة والاستحقاقات
            - إنهاء الوكالة وإجراءاته
            """
        }
    ]
    
    for contract in contract_types:
        with st.expander(contract["title"], expanded=False):
            st.markdown(contract["content"])

# ==========================
# 💰 الأوراق التجارية
# ==========================
def show_commercial_papers():
    st.markdown("#### 💰 الأوراق التجارية")
    
    papers_types = [
        {
            "title": "💸 الكمبيالة - المواد 123-185",
            "content": """
            **الكمبيالة (السند لأمر):**
            - ورقة تجارية تحتوي على أمر غير مشروط بدفع مبلغ معين
            - يجب أن تشمل بيانات إلزامية محددة
            - قابلة للتظهير والتداول
            - آجال السداد والإجراءات
            """
        },
        {
            "title": "📋 السند الإذني - المواد 186-210",
            "content": """
            **السند الإذني:**
            - وعد غير مشروط بدفع مبلغ معين
            - يصدر من المدين مباشرة
            - يستخدم في المعاملات التجارية
            - إجراءات التحصيل والاحتجاج
            """
        },
        {
            "title": "🏦 الشيك - المواد 211-289",
            "content": """
            **الشيك البنكي:**
            - أمر من الساحب إلى المسحوب عليه بدفع مبلغ محدد
            - يجب أن يكون على مصرف
            - آجال التقديم والتحصيل
            - المسؤوليات والعقوبات
            """
        }
    ]
    
    for paper in papers_types:
        with st.expander(paper["title"], expanded=False):
            st.markdown(paper["content"])

# ==========================
# 🏦 الإفلاس
# ==========================
def show_bankruptcy_provisions():
    st.markdown("#### 🏦 نظام الإفلاس والتسوية")
    
    bankruptcy_types = [
        {
            "title": "🔄 الصلح الواقي - المواد 290-315",
            "content": """
            **إجراءات الصلح الواقي:**
            - طلب التاجر للصلح الواقي من الإفلاس
            - شروط القبول والرفض
            - إجراءات المصادقة على اتفاق الصلح
            - حقوق الدائنين والتزامات التاجر
            """
        },
        {
            "title": "📉 الإفلاس - المواد 316-424",
            "content": """
            **أحكام الإفلاس:**
            - إعلان الإفلاس وأسبابه
            - إجراءات التصفية وتوزيع الأموال
            - مسؤوليات المفلس وحقوقه
            - إنهاء الإفلاس وآثاره
            """
        }
    ]
    
    for bankruptcy in bankruptcy_types:
        with st.expander(bankruptcy["title"], expanded=False):
            st.markdown(bankruptcy["content"])

# ==========================
# 🔍 فحص الالتزامات
# ==========================
def show_compliance_checker():
    st.markdown("#### 🔍 فحص الالتزامات التجارية")
    
    compliance_checks = [
        "هل تم القيد في السجل التجاري؟ - المادة 16",
        "هل يتم مسك الدفاتر التجارية بشكل منتظم؟ - المادة 20",
        "هل يتم الاحتفاظ بالمراسلات لمدة 10 سنوات؟ - المادة 15",
        "هل يتم الإفصاح عن المعلومات الأساسية للعملاء؟ - المادة 14",
        "هل يتم الالتزام بقواعد الشرف في المعاملات؟ - المادة 13"
    ]
    
    violations = 0
    results = []
    
    for i, check in enumerate(compliance_checks):
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.write(f"{i+1}. {check}")
        with col2:
            answer = st.selectbox("", ["نعم", "لا"], key=f"comp_{i}", label_visibility="collapsed")
        with col3:
            if answer == "لا":
                violations += 1
                st.error("⚠️")
                results.append(f"انتهاك: {check}")
            else:
                st.success("✅")
    
    st.metric("إجمالي الانتهاكات المحتملة", violations)
    
    if violations > 0:
        st.error(f"🚨 هناك {violations} انتهاكات محتملة تحتاج متابعة فورية")
        with st.expander("تفاصيل الانتهاكات"):
            for result in results:
                st.write(f"• {result}")
    else:
        st.success("✅ ممتاز! لا توجد انتهاكات واضحة - نشاط تجاري متوافق مع القانون")

# ==========================
# 🏛️ قسم الشركات والمؤسسات - النسخة المحدثة
# ==========================
def show_companies_section():
    show_breadcrumbs("🏛️ قسم الشركات والمؤسسات")
    
    st.markdown("""
    <div class="main-header">
        <h1>🏛️ منصة الشركات والمؤسسات التجارية</h1>
        <p>دليل شامل حسب قانون الشركات الأردني رقم 22 لسنة 1997 وتعديلاته</p>
    </div>
    """, unsafe_allow_html=True)

    st.info("""
    **📢 أحدث التعديلات التشريعية:** 
    - **قانون الشركات:** رقم 22 لسنة 1997 وتعديلاته
    - **الاستثمار:** قانون تشجيع الاستثمار
    - **الضرائب:** قانون ضريبة الدخل
    """)

    # تبويبات رئيسية
    company_tabs = st.tabs([
        "🏢 تأسيس الشركات", 
        "📊 إدارة الشركات",
        "💰 النظام المالي",
        "🛡️ المسؤولية القانونية",
        "📝 عقود الشركات",
        "🔍 فحص الامتثال"
    ])

    with company_tabs[0]:
        show_company_formation()

    with company_tabs[1]:
        show_company_management()

    with company_tabs[2]:
        show_company_finance()

    with company_tabs[3]:
        show_company_liability()

    with company_tabs[4]:
        show_company_contracts()
        
    with company_tabs[5]:
        show_company_compliance()

# ==========================
# 🏢 تأسيس الشركات
# ==========================
def show_company_formation():
    st.markdown("#### 🏢 تأسيس الشركات التجارية")
    
    company_types = [
        {
            "type": "شركة التضامن",
            "description": "تتألف من شريكين أو أكثر مسؤولين بالتضامن عن ديون الشركة",
            "capital": "لا يوجد حد أدنى",
            "partners": "شخصان على الأقل",
            "liability": "مسؤولية غير محدودة"
        },
        {
            "type": "شركة التوصية البسيطة",
            "description": "تتألف من شركاء متضامنين وشركاء موصين",
            "capital": "لا يوجد حد أدنى",
            "partners": "شريك متضامن واحد على الأقل وشريك موصٍ واحد",
            "liability": "المتضامنون غير محدودي المسؤولية، الموصون محدودو المسؤولية"
        },
        {
            "type": "شركة المساهمة العامة",
            "description": "رأس مالها مقسم إلى أسهم قابلة للتداول",
            "capital": "500,000 دينار كحد أدنى",
            "partners": "7 مساهمين على الأقل",
            "liability": "مسؤولية محدودة بقيمة الأسهم"
        },
        {
            "type": "شركة المساهمة الخاصة",
            "description": "رأس مالها مقسم إلى أسهم غير قابلة للتداول علناً",
            "capital": "50,000 دينار كحد أدنى",
            "partners": "شخصان على الأقل",
            "liability": "مسؤولية محدودة بقيمة الأسهم"
        },
        {
            "type": "شركة ذات مسؤولية محدودة",
            "description": "تتألف من شركاء مسؤولين ضمن حدود حصصهم",
            "capital": "1 دينار كحد أدنى",
            "partners": "شخصان على الأقل و50 كحد أقصى",
            "liability": "مسؤولية محدودة بقيمة الحصص"
        }
    ]
    
    for company in company_types:
        with st.expander(f"🏢 {company['type']}", expanded=False):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**الوصف:** {company['description']}")
                st.write(f"**رأس المال:** {company['capital']}")
            with col2:
                st.write(f"**الشركاء:** {company['partners']}")
                st.write(f"**المسؤولية:** {company['liability']}")

# ==========================
# 📊 إدارة الشركات
# ==========================
def show_company_management():
    st.markdown("#### 📊 إدارة وهيكل الشركات")
    
    management_structure = [
        {
            "position": "الجمعية العمومية",
            "responsibilities": "أعلى سلطة في الشركة - اتخاذ القرارات المصيرية",
            "authority": "تعديل النظام الأساسي - تعيين المدققين - توزيع الأرباح"
        },
        {
            "position": "مجلس الإدارة",
            "responsibilities": "إدارة الشركة وتنفيذ سياساتها",
            "authority": "تعيين المديرين - اعتماد الميزانيات - التوقيع على العقود"
        },
        {
            "position": "المدير العام",
            "responsibilities": "الإدارة اليومية للشركة وتنفيذ قرارات مجلس الإدارة",
            "authority": "تمثيل الشركة - إبرام العقود - إدارة الموظفين"
        },
        {
            "position": "مدقق الحسابات",
            "responsibilities": "مراجعة القوائم المالية وضمان دقتها",
            "authority": "فحص السجلات - إعداد تقارير التدقيق - الإبلاغ عن المخالفات"
        }
    ]
    
    for position in management_structure:
        with st.expander(f"📊 {position['position']}", expanded=False):
            st.write(f"**المسؤوليات:** {position['responsibilities']}")
            st.write(f"**الصلاحيات:** {position['authority']}")

# ==========================
# 💰 النظام المالي
# ==========================
def show_company_finance():
    st.markdown("#### 💰 النظام المالي والمحاسبي")
    
    financial_requirements = [
        {
            "requirement": "رأس المال",
            "details": "يجب تحديد رأس المال في النظام الأساسي والالتزام بالحدود الدنيا",
            "law": "المادة 5 من قانون الشركات"
        },
        {
            "requirement": "الاحتياطي القانوني",
            "details": "10% من صافي الأرباح حتى يصل إلى 50% من رأس المال",
            "law": "المادة 168 من قانون الشركات"
        },
        {
            "requirement": "القوائم المالية",
            "details": "إعداد ميزانية عمومية وحساب أرباح وخسائر وقائمة تدفقات نقدية",
            "law": "المادة 172 من قانون الشركات"
        },
        {
            "requirement": "التدقيق المالي",
            "details": "تعيين مدقق حسابات قانوني لمراجعة القوائم المالية",
            "law": "المادة 174 من قانون الشركات"
        }
    ]
    
    for req in financial_requirements:
        with st.expander(f"💰 {req['requirement']}", expanded=False):
            st.write(f"**التفاصيل:** {req['details']}")
            st.write(f"**القانون:** {req['law']}")

# ==========================
# 🛡️ المسؤولية القانونية
# ==========================
def show_company_liability():
    st.markdown("#### 🛡️ المسؤوليات والالتزامات القانونية")
    
    liabilities = [
        {
            "liability": "المسؤولية المدنية",
            "details": "مسؤولية الشركة عن الأضرار التي تسببها للغير",
            "scope": "تشمل الأضرار المادية والمعنوية الناتجة عن نشاط الشركة"
        },
        {
            "liability": "المسؤولية الجزائية",
            "details": "مسؤولية الشركة عن الجرائم التي ترتكب باسمها",
            "scope": "تشمل الغرامات والمصادرة وسحب التراخيص"
        },
        {
            "liability": "المسؤولية الإدارية",
            "details": "الالتزام بالأنظمة والتعليمات الإدارية",
            "scope": "تشمل التراخيص والموافقات والاشتراطات البلدية"
        },
        {
            "liability": "مسؤولية المدراء",
            "details": "مسؤولية أعضاء مجلس الإدارة عن الإدارة غير السليمة",
            "scope": "تشمل التعويضات والعزل والمنع من إدارة الشركات"
        }
    ]
    
    for liability in liabilities:
        with st.expander(f"🛡️ {liability['liability']}", expanded=False):
            st.write(f"**التفاصيل:** {liability['details']}")
            st.write(f"**النطاق:** {liability['scope']}")

# ==========================
# 📝 عقود الشركات
# ==========================
def show_company_contracts():
    st.markdown("#### 📝 عقود الشركات الأساسية")
    
    contracts = [
        {
            "contract": "عقد التأسيس",
            "purpose": "إنشاء الشركة وتحديد نظامها الأساسي",
            "parties": "المؤسسون والشركاء",
            "content": "الاسم - الغرض - رأس المال - الإدارة - التصفية"
        },
        {
            "contract": "عقد بيع الحصص",
            "purpose": "نقل ملكية الحصص بين الشركاء",
            "parties": "البائع والمشتري والشركة",
            "content": "وصف الحصص - الثمن - شروط النقل - الضمانات"
        },
        {
            "contract": "عقد إدارة الشركة",
            "purpose": "تنظيم علاقة الشركة مع المديرين",
            "parties": "الشركة والمدير",
            "content": "الصلاحيات - المسؤوليات - المكافآت - المدة"
        }
    ]
    
    for contract in contracts:
        with st.expander(f"📝 {contract['contract']}", expanded=False):
            st.write(f"**الغرض:** {contract['purpose']}")
            st.write(f"**الأطراف:** {contract['parties']}")
            st.write(f"**المحتوى:** {contract['content']}")

# ==========================
# 🔍 فحص الامتثال
# ==========================
def show_company_compliance():
    st.markdown("#### 🔍 فحص امتثال الشركة")
    
    compliance_checklist = [
        "هل تم تسجيل الشركة في سجل الشركات؟",
        "هل يتم عقد الجمعية العمومية سنوياً؟",
        "هل يتم تعيين مدقق حسابات؟",
        "هل يتم إعداد القوائم المالية السنوية؟",
        "هل يتم الالتزام بنسبة الاحتياطي القانوني؟",
        "هل يتم تحديث سجل الشركاء؟",
        "هل يتم الالتزام بالضرائب والرسوم؟"
    ]
    
    violations = 0
    for i, check in enumerate(compliance_checklist):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"{i+1}. {check}")
        with col2:
            answer = st.selectbox("", ["نعم", "لا"], key=f"company_comp_{i}", label_visibility="collapsed")
            if answer == "لا":
                violations += 1
    
    st.metric("مخاطر عدم الامتثال", violations)
    
    if violations > 0:
        st.warning(f"⚠️ هناك {violations} مخاطر امتثال تحتاج المعالجة")

# ==========================
# 📝 قسم العقود التجارية - قسم جديد
# ==========================
def show_contracts_section():
    show_breadcrumbs("📝 قسم العقود التجارية")
    
    st.markdown("""
    <div class="main-header">
        <h1>📝 منصة العقود التجارية المتكاملة</h1>
        <p>نماذج عقود تجارية جاهزة وأدوات صياغة متقدمة وفق القانون التجاري الأردني</p>
    </div>
    """, unsafe_allow_html=True)

    st.info("""
    **💡 دليل الاستخدام:** 
    اختر نوع العقد المناسب من القائمة أدناه، ثم املأ البيانات المطلوبة لتوليد عقد تجاري متكامل.
    جميع النماذج مبنية على قانون التجارة الأردني وتعديلاته.
    """)

    contract_tabs = st.tabs([
        "🛒 عقود البيع", 
        "🚚 عقود النقل",
        "🤝 عقود الوكالة",
        "📊 عقود السمسرة", 
        "🏦 عقود الحساب الجاري",
        "🎯 منشئ العقود"
    ])

    with contract_tabs[0]:
        show_sale_contracts()

    with contract_tabs[1]:
        show_transport_contracts()

    with contract_tabs[2]:
        show_agency_contracts()

    with contract_tabs[3]:
        show_brokerage_contracts()

    with contract_tabs[4]:
        show_current_account_contracts()
        
    with contract_tabs[5]:
        show_contract_builder()

# ==========================
# 🛒 عقود البيع
# ==========================
def show_sale_contracts():
    st.markdown("#### 🛒 عقود البيع التجاري")
    
    sale_contracts = [
        {
            "type": "عقد بيع بضائع",
            "description": "لبيع البضائع والتسليم الفوري",
            "features": ["تحديد البضائع", "السعر وطريقة الدفع", "شروط التسليم", "الضمانات"],
            "law": "المواد 51-59"
        },
        {
            "type": "عقد بيع آجل",
            "description": "للبيع مع تأجيل الدفع",
            "features": ["آجال السداد", "الفائدة", "الضمانات", "جزاءات التأخير"],
            "law": "المواد 60-67"
        }
    ]
    
    for contract in sale_contracts:
        with st.expander(f"🛒 {contract['type']}", expanded=False):
            st.write(f"**الوصف:** {contract['description']}")
            st.write("**المميزات:**")
            for feature in contract['features']:
                st.write(f"• {feature}")
            st.write(f"**القانون:** {contract['law']}")

# ==========================
# 🚚 عقود النقل
# ==========================
def show_transport_contracts():
    st.markdown("#### 🚚 عقود النقل التجاري")
    
    transport_contracts = [
        {
            "type": "عقد نقل بضائع",
            "description": "لنقل البضائع براً أو بحراً أو جواً",
            "features": ["تحديد البضائع", "مسار النقل", "التأمين", "مسؤولية الناقل"],
            "law": "المواد 68-79"
        }
    ]
    
    for contract in transport_contracts:
        with st.expander(f"🚚 {contract['type']}", expanded=False):
            st.write(f"**الوصف:** {contract['description']}")
            st.write("**المميزات:**")
            for feature in contract['features']:
                st.write(f"• {feature}")
            st.write(f"**القانون:** {contract['law']}")

# ==========================
# 🤝 عقود الوكالة
# ==========================
def show_agency_contracts():
    st.markdown("#### 🤝 عقود الوكالة التجارية")
    
    agency_contracts = [
        {
            "type": "عقد وكالة بالعمولة",
            "description": "لتمثيل الشركة في بيع منتجاتها",
            "features": ["نطاق الوكالة", "العمولة", "المنطقة", "مدة العقد"],
            "law": "المواد 80-98"
        }
    ]
    
    for contract in agency_contracts:
        with st.expander(f"🤝 {contract['type']}", expanded=False):
            st.write(f"**الوصف:** {contract['description']}")
            st.write("**المميزات:**")
            for feature in contract['features']:
                st.write(f"• {feature}")
            st.write(f"**القانون:** {contract['law']}")

# ==========================
# 📊 عقود السمسرة
# ==========================
def show_brokerage_contracts():
    st.markdown("#### 📊 عقود السمسرة التجارية")
    
    brokerage_contracts = [
        {
            "type": "عقد سمسرة",
            "description": "لتسهيل إبرام الصفقات بين الأطراف",
            "features": ["نوع الصفقات", "عمولة السمسار", "التزامات الأطراف", "سريان العقد"],
            "law": "المواد 99-105"
        }
    ]
    
    for contract in brokerage_contracts:
        with st.expander(f"📊 {contract['type']}", expanded=False):
            st.write(f"**الوصف:** {contract['description']}")
            st.write("**المميزات:**")
            for feature in contract['features']:
                st.write(f"• {feature}")
            st.write(f"**القانون:** {contract['law']}")

# ==========================
# 🏦 عقود الحساب الجاري
# ==========================
def show_current_account_contracts():
    st.markdown("#### 🏦 عقود الحساب الجاري")
    
    account_contracts = [
        {
            "type": "عقد حساب جاري",
            "description": "لتنظيم العلاقات المالية المستمرة بين التجار",
            "features": ["رصيد الحساب", "الفائدة", "العمولات", "تسوية الحساب"],
            "law": "المواد 106-122"
        }
    ]
    
    for contract in account_contracts:
        with st.expander(f"🏦 {contract['type']}", expanded=False):
            st.write(f"**الوصف:** {contract['description']}")
            st.write("**المميزات:**")
            for feature in contract['features']:
                st.write(f"• {feature}")
            st.write(f"**القانون:** {contract['law']}")

# ==========================
# 🎯 منشئ العقود
# ==========================
def show_contract_builder():
    st.markdown("#### 🎯 منشئ العقود المتقدم")
    
    with st.form("commercial_contract_builder"):
        st.subheader("إنشاء عقد تجاري مخصص")
        
        col1, col2 = st.columns(2)
        
        with col1:
            contract_type = st.selectbox("نوع العقد", [
                "عقد بيع تجاري",
                "عقد وكالة تجارية", 
                "عقد سمسرة",
                "عقد نقل تجاري"
            ])
            
            party1_name = st.text_input("اسم الطرف الأول (البائع/الموكل)")
            party1_address = st.text_input("عنوان الطرف الأول")
            
        with col2:
            party2_name = st.text_input("اسم الطرف الثاني (المشتري/الوكيل)")
            party2_address = st.text_input("عنوان الطرف الثاني")
            
            contract_value = st.number_input("قيمة العقد (دينار)", min_value=0, value=1000)
        
        contract_details = st.text_area("تفاصيل العقد", placeholder="وصف البضائع أو الخدمات...")
        
        if st.form_submit_button("🎯 إنشاء العقد", use_container_width=True):
            contract_content = generate_commercial_contract(
                contract_type, party1_name, party1_address, 
                party2_name, party2_address, contract_value, contract_details
            )
            st.session_state.generated_contract = contract_content
            st.success("✅ تم إنشاء العقد بنجاح!")
            
            st.text_area("📝 نص العقد الجاهز", value=contract_content, height=300)

def generate_commercial_contract(contract_type, party1, address1, party2, address2, value, details):
    """إنشاء عقد تجاري مخصص"""
    
    contract_template = f"""
    📜 {contract_type}
    وفقاً لأحكام قانون التجارة الأردني رقم 12 لسنة 1966 وتعديلاته
    
    تم إبرام هذا العقد في تاريخ ____ الموافق __/__/____
    
    بين:
    
    الطرف الأول: {party1}
    العنوان: {address1}
    
    و
    
    الطرف الثاني: {party2}
    العنوان: {address2}
    
    المادة 1: موضوع العقد
    {details}
    
    المادة 2: القيمة والمقابل
    - قيمة العقد: {value:,} دينار أردني
    - طريقة الدفع: ______
    - مواعيد السداد: ______
    
    المادة 3: الالتزامات العامة
    - يلتزم الطرفان بأحكام القانون التجاري الأردني
    - يحتفظ كل طرف بحقه في المطالبة القضائية
    - يتم تفسير العقد لصالح الوفاء بالالتزامات
    
    المادة 4: إنهاء العقد
    - يحق للطرفين إنهاء العقد بموافقة خطية
    - في حال الإخلال يحق للطرف المتضرر المطالبة بالتعويض
    
    توقيع الطرف الأول: __________
    توقيع الطرف الثاني: __________
    
    ⚠️ تنويه: هذا النموذج لأغراض إرشادية فقط
    """
    
    return contract_template

# ==========================
# 💳 قسم الأوراق التجارية - قسم جديد
# ==========================
def show_commercial_papers_section():
    show_breadcrumbs("💳 قسم الأوراق التجارية")
    
    st.markdown("""
    <div class="main-header">
        <h1>💳 منصة الأوراق التجارية</h1>
        <p>دليل شامل للأوراق التجارية وفق قانون التجارة الأردني - الكمبيالة، السند الإذني، الشيك</p>
    </div>
    """, unsafe_allow_html=True)

    papers_tabs = st.tabs([
        "💸 الكمبيالة", 
        "📋 السند الإذني",
        "🏦 الشيك",
        "🔄 التظهير",
        "🧮 حاسبة الاستحقاق",
        "🔍 فحص الأوراق"
    ])

    with papers_tabs[0]:
        show_bill_of_exchange()

    with papers_tabs[1]:
        show_promissory_note()

    with papers_tabs[2]:
        show_cheque()

    with papers_tabs[3]:
        show_endorsement()

    with papers_tabs[4]:
        show_maturity_calculator()
        
    with papers_tabs[5]:
        show_paper_inspection()

# ==========================
# 💸 الكمبيالة
# ==========================
def show_bill_of_exchange():
    st.markdown("#### 💸 الكمبيالة (السند لأمر)")
    
    bill_provisions = [
        {
            "title": "📋 البيانات الإلزامية - المادة 123",
            "content": """
            **البيانات الواجب توفرها في الكمبيالة:**
            - لفظ "كمبيالة" في متن السند
            - أمر غير مشروط بدفع مبلغ معين
            - اسم المسحوب عليه
            - اسم المستفيد
            - تاريخ الإنشاء
            - توقيع الساحب
            """
        },
        {
            "title": "⏰ آجال الاستحقاق - المادة 124",
            "content": """
            **أنواع آجال الاستحقاق:**
            - للإطلاع: payable at sight
            - بعد الإطلاع: payable after sight
            - بعد التاريخ: payable after date
            - تاريخ محدد: payable at fixed date
            """
        },
        {
            "title": "🔄 التظهير - المواد 125-140",
            "content": """
            **أحكام التظهير:**
            - نقل ملكية الكمبيالة بالتظهير
            - التظهير الكامل أو التظهير التوكيلي
            - التظهير غير المشروط
            - مسؤولية المظهر عن القبول والوفاء
            """
        }
    ]
    
    for provision in bill_provisions:
        with st.expander(provision["title"], expanded=False):
            st.markdown(provision["content"])

# ==========================
# 📋 السند الإذني
# ==========================
def show_promissory_note():
    st.markdown("#### 📋 السند الإذني")
    
    note_provisions = [
        {
            "title": "📝 تعريف السند الإذني - المادة 186",
            "content": """
            **السند الإذني:**
            - وعد كتابي غير مشروط بدفع مبلغ معين
            - يصدر من المدين مباشرة
            - يحتوي على البيانات الإلزامية المماثلة للكمبيالة
            - يخضع لنفس أحكام الكمبيالة ما لم ينص على خلاف ذلك
            """
        }
    ]
    
    for provision in note_provisions:
        with st.expander(provision["title"], expanded=False):
            st.markdown(provision["content"])

# ==========================
# 🏦 الشيك
# ==========================
def show_cheque():
    st.markdown("#### 🏦 الشيك البنكي")
    
    cheque_provisions = [
        {
            "title": "🏦 أحكام الشيك - المادة 211",
            "content": """
            **الشروط الأساسية للشيك:**
            - لفظ "شيك" في متن السند
            - أمر غير مشروط بدفع مبلغ معين
            - اسم المسحوب عليه (مصرف)
            - مكان الدفع
            - تاريخ وإنشاء الشيك
            - توقيع الساحب
            """
        },
        {
            "title": "⏰ تقديم الشيك - المادة 212",
            "content": """
            **مواعيد التقديم:**
            - 8 أيام إذا صدر في نفس المحافظة
            - 15 يوماً إذا صدر في محافظة أخرى
            - 30 يوماً إذا صدر خارج المملكة
            - يبدأ العد من تاريخ الإنشاء
            """
        }
    ]
    
    for provision in cheque_provisions:
        with st.expander(provision["title"], expanded=False):
            st.markdown(provision["content"])

# ==========================
# 🔄 التظهير
# ==========================
def show_endorsement():
    st.markdown("#### 🔄 نظام التظهير")
    
    endorsement_types = [
        {
            "type": "التظهير الكامل",
            "description": "نقل ملكية الورقة التجارية بالكامل",
            "effects": "ينقل جميع الحقوق - يتحمل المظهر المسؤولية"
        },
        {
            "type": "التظهير التوكيلي", 
            "description": "تفويض حامل الورقة للقيام بإجراءات التحصيل",
            "effects": "لا ينقل الملكية - للحامل حق التحصيل فقط"
        },
        {
            "type": "التظهير التقييدي",
            "description": "تقييد التصرف في الورقة التجارية",
            "effects": "يمنع التظهير اللاحق - للحقوق المحددة فقط"
        }
    ]
    
    for endorsement in endorsement_types:
        with st.expander(f"🔄 {endorsement['type']}", expanded=False):
            st.write(f"**الوصف:** {endorsement['description']}")
            st.write(f"**الآثار:** {endorsement['effects']}")

# ==========================
# 🧮 حاسبة الاستحقاق
# ==========================
def show_maturity_calculator():
    st.markdown("#### 🧮 حاسبة آجال استحقاق الأوراق التجارية")
    
    with st.form("maturity_calculator"):
        col1, col2 = st.columns(2)
        
        with col1:
            paper_type = st.selectbox("نوع الورقة التجارية", [
                "كمبيالة",
                "سند إذني", 
                "شيك"
            ])
            
            issue_date = st.date_input("تاريخ الإنشاء")
            paper_value = st.number_input("قيمة الورقة (دينار)", min_value=0, value=1000)
            
        with col2:
            maturity_type = st.selectbox("نوع الاستحقاق", [
                "للإطلاع",
                "بعد الإطلاع - 30 يوم",
                "بعد التاريخ - 60 يوم", 
                "تاريخ محدد"
            ])
            
            if maturity_type == "تاريخ محدد":
                fixed_date = st.date_input("تاريخ الاستحقاق المحدد")
            else:
                fixed_date = None
        
        if st.form_submit_button("🧮 احسب تاريخ الاستحقاق", use_container_width=True):
            result = calculate_maturity_date(issue_date, maturity_type, fixed_date)
            st.success(f"**تاريخ الاستحقاق:** {result}")

def calculate_maturity_date(issue_date, maturity_type, fixed_date=None):
    """حساب تاريخ استحقاق الورقة التجارية"""
    
    if maturity_type == "للإطلاع":
        return "للإطلاع (يستحق عند التقديم)"
    elif maturity_type == "بعد الإطلاع - 30 يوم":
        maturity = issue_date + pd.DateOffset(days=30)
        return maturity.strftime("%Y-%m-%d")
    elif maturity_type == "بعد التاريخ - 60 يوم":
        maturity = issue_date + pd.DateOffset(days=60)
        return maturity.strftime("%Y-%m-%d")
    elif maturity_type == "تاريخ محدد" and fixed_date:
        return fixed_date.strftime("%Y-%m-%d")
    else:
        return "غير محدد"

# ==========================
# 🔍 فحص الأوراق
# ==========================
def show_paper_inspection():
    st.markdown("#### 🔍 فحص صحة الورقة التجارية")
    
    inspection_checks = [
        "هل تحتوي الورقة على البيانات الإلزامية؟",
        "هل التوقيعات صحيحة ومطابقة؟",
        "هل تاريخ الإنشاء صحيح؟",
        "هل تجاوزت مدة التقديم؟",
        "هل هناك شطب أو تعديل غير مصرح به؟",
        "هل التظهير صحيح ومتوالي؟"
    ]
    
    valid_checks = 0
    for i, check in enumerate(inspection_checks):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"{i+1}. {check}")
        with col2:
            answer = st.selectbox("", ["نعم", "لا"], key=f"paper_check_{i}", label_visibility="collapsed")
            if answer == "نعم":
                valid_checks += 1
    
    st.metric("نسبة الصحة", f"{(valid_checks/len(inspection_checks))*100:.0f}%")
    
    if valid_checks == len(inspection_checks):
        st.success("✅ الورقة التجارية صحيحة وقابلة للتداول")
    else:
        st.warning("⚠️ هناك مشاكل في الورقة التجارية تحتاج المعالجة")

# ==========================
# 🏦 قسم الإفلاس والتسوية - قسم جديد
# ==========================
def show_bankruptcy_section():
    show_breadcrumbs("🏦 قسم الإفلاس والتسوية")
    
    st.markdown("""
    <div class="main-header">
        <h1>🏦 منصة الإفلاس والتسوية الواقية</h1>
        <p>دليل شامل لإجراءات الإفلاس والصلح الواقي وفق قانون التجارة الأردني</p>
    </div>
    """, unsafe_allow_html=True)

    bankruptcy_tabs = st.tabs([
        "🔄 الصلح الواقي", 
        "📉 الإفلاس",
        "📊 التصفية",
        "🧮 حاسبة الديون",
        "📋 نماذج الإفلاس",
        "🔍 فحص الجدارة"
    ])

    with bankruptcy_tabs[0]:
        show_preventive_settlement()

    with bankruptcy_tabs[1]:
        show_bankruptcy_procedures()

    with bankruptcy_tabs[2]:
        show_liquidation_procedures()

    with bankruptcy_tabs[3]:
        show_debt_calculator()

    with bankruptcy_tabs[4]:
        show_bankruptcy_forms()
        
    with bankruptcy_tabs[5]:
        show_solvency_check()

# ==========================
# 🔄 الصلح الواقي
# ==========================
def show_preventive_settlement():
    st.markdown("#### 🔄 الصلح الواقي من الإفلاس")
    
    settlement_steps = [
        {
            "step": "📋 طلب الصلح الواقي",
            "details": "تقديم التاجر طلب الصلح الواقي إلى المحكمة المختصة",
            "conditions": "التوقف عن الديون - حسن النية - إمكانية الاستمرار"
        },
        {
            "step": "📊 تعيين القيم",
            "details": "تعيين قيم للإشراف على أعمال التاجر خلال فترة الصلح",
            "conditions": "خبرة في المجال التجاري - حيادية - كفاءة"
        },
        {
            "step": "🤝 اتفاق الصلح",
            "details": "التوصل لاتفاق بين التاجر والدائنين على تسوية الديون",
            "conditions": "موافقة أغلبية الدائنين - معقولية الشروط - جدوى التنفيذ"
        },
        {
            "step": "✅ المصادقة والتنفيذ",
            "details": "مصادقة المحكمة على الاتفاق ومتابعة تنفيذه",
            "conditions": "الالتزام بالاتفاق - متابعة القيم - تقارير دورية"
        }
    ]
    
    for step in settlement_steps:
        with st.expander(f"🔄 {step['step']}", expanded=False):
            st.write(f"**التفاصيل:** {step['details']}")
            st.write(f"**الشروط:** {step['conditions']}")

# ==========================
# 📉 الإفلاس
# ==========================
def show_bankruptcy_procedures():
    st.markdown("#### 📉 إجراءات الإفلاس")
    
    bankruptcy_steps = [
        {
            "step": "📢 إعلان الإفلاس",
            "details": "إعلان المحكمة إفلاس التاجر بناء على طلب منه أو من الدائنين",
            "effects": "وقف المطالبات - تعيين مصف - حجز أموال المفلس"
        },
        {
            "step": "📋 جرد الأموال",
            "details": "جرد وتقييم أموال المفلس من قبل المصفى",
            "effects": "حصر الأصول - تقييم الموجودات - كشف الديون"
        },
        {
            "step": "💰 بيع الأموال",
            "details": "بيع أموال المفلس في المزاد العلني",
            "effects": "تحويل الأصول إلى نقد - توزيع حصيلة البيع"
        },
        {
            "step": "📊 توزيع الحصيلة",
            "details": "توزيع حصيلة البيع على الدائنين حسب الأولويات",
            "effects": "سداد الديون - إشعارات التوزيع - إنهاء الإفلاس"
        }
    ]
    
    for step in bankruptcy_steps:
        with st.expander(f"📉 {step['step']}", expanded=False):
            st.write(f"**التفاصيل:** {step['details']}")
            st.write(f"**الآثار:** {step['effects']}")

# ==========================
# 📊 التصفية
# ==========================
def show_liquidation_procedures():
    st.markdown("#### 📊 إجراءات التصفية")
    
    liquidation_info = [
        {
            "aspect": "أولويات الدائنين",
            "order": "1. مصاريف التصفية 2. الديون المضمونة 3. ديون العمل 4. الدائنين العاديين"
        },
        {
            "aspect": "مدة التصفية",
            "order": "تستمر حتى الانتهاء من بيع جميع الأصول وسداد جميع الديون"
        },
        {
            "aspect": "حقوق المفلس",
            "order": "الحق في المعيشة الكريم - الاحتفاظ بالمنزل - أدوات العمل الأساسية"
        }
    ]
    
    for info in liquidation_info:
        with st.expander(f"📊 {info['aspect']}", expanded=False):
            st.write(info['order'])

# ==========================
# 🧮 حاسبة الديون
# ==========================
def show_debt_calculator():
    st.markdown("#### 🧮 حاسبة توزيع أموال الإفلاس")
    
    with st.form("debt_calculator"):
        col1, col2 = st.columns(2)
        
        with col1:
            total_assets = st.number_input("إجمالي الأموال المتاحة (دينار)", min_value=0, value=100000)
            liquidation_costs = st.number_input("مصاريف التصفية (دينار)", min_value=0, value=10000)
            
        with col2:
            secured_debts = st.number_input("الديون المضمونة (دينار)", min_value=0, value=30000)
            labor_debts = st.number_input("ديون العاملين (دينار)", min_value=0, value=20000)
        
        ordinary_debts = st.number_input("الديون العادية (دينار)", min_value=0, value=50000)
        
        if st.form_submit_button("🧮 احسب التوزيع", use_container_width=True):
            result = calculate_bankruptcy_distribution(
                total_assets, liquidation_costs, secured_debts, labor_debts, ordinary_debts
            )
            display_distribution_result(result)

def calculate_bankruptcy_distribution(total_assets, costs, secured, labor, ordinary):
    """حساب توزيع أموال الإفلاس"""
    
    available_funds = total_assets
    
    # الأولوية الأولى: مصاريف التصفية
    liquidation_paid = min(costs, available_funds)
    available_funds -= liquidation_paid
    
    # الأولوية الثانية: الديون المضمونة
    secured_paid = min(secured, available_funds)
    available_funds -= secured_paid
    
    # الأولوية الثالثة: ديون العمل
    labor_paid = min(labor, available_funds)
    available_funds -= labor_paid
    
    # الأولوية الرابعة: الديون العادية
    ordinary_paid = min(ordinary, available_funds)
    available_funds -= ordinary_paid
    
    return {
        'liquidation_costs': {'due': costs, 'paid': liquidation_paid},
        'secured_debts': {'due': secured, 'paid': secured_paid},
        'labor_debts': {'due': labor, 'paid': labor_paid},
        'ordinary_debts': {'due': ordinary, 'paid': ordinary_paid},
        'remaining_funds': available_funds
    }

def display_distribution_result(result):
    """عرض نتيجة توزيع أموال الإفلاس"""
    
    st.success("## 🧮 نتائج توزيع أموال الإفلاس")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "مصاريف التصفية", 
            f"{result['liquidation_costs']['paid']:,.0f} دينار",
            f"من {result['liquidation_costs']['due']:,.0f} دينار"
        )
    
    with col2:
        st.metric(
            "الديون المضمونة", 
            f"{result['secured_debts']['paid']:,.0f} دينار",
            f"من {result['secured_debts']['due']:,.0f} دينار"
        )
    
    with col3:
        st.metric(
            "ديون العاملين", 
            f"{result['labor_debts']['paid']:,.0f} دينار",
            f"من {result['labor_debts']['due']:,.0f} دينار"
        )
    
    with col4:
        st.metric(
            "الديون العادية", 
            f"{result['ordinary_debts']['paid']:,.0f} دينار",
            f"من {result['ordinary_debts']['due']:,.0f} دينار"
        )
    
    if result['remaining_funds'] > 0:
        st.info(f"💰 الأموال المتبقية: {result['remaining_funds']:,.0f} دينار")
    else:
        st.warning("💸 تم توزيع جميع الأموال المتاحة")

# ==========================
# 📋 نماذج الإفلاس
# ==========================
def show_bankruptcy_forms():
    st.markdown("#### 📋 نماذج الإفلاس والصلح الواقي")
    
    forms = [
        {
            "form": "طلب الصلح الواقي",
            "description": "نموذج طلب الصلح الواقي من الإفلاس",
            "usage": "للتجار الراغبين في تسوية ديونهم تجنباً للإفلاس"
        },
        {
            "form": "إقرار الدائنين",
            "description": "نموذج إقرار الدائنين بديونهم",
            "usage": "لتسجيل ديون الدائنين في إجراءات الإفلاس"
        },
        {
            "form": "اتفاق الصلح",
            "description": "نموذج اتفاق التسوية بين التاجر والدائنين",
            "usage": "لتوثيق اتفاق الصلح الواقي المصادق عليه من المحكمة"
        }
    ]
    
    for form in forms:
        with st.expander(f"📋 {form['form']}", expanded=False):
            st.write(f"**الوصف:** {form['description']}")
            st.write(f"**الاستخدام:** {form['usage']}")

# ==========================
# 🔍 فحص الجدارة
# ==========================
def show_solvency_check():
    st.markdown("#### 🔍 فحص الجدارة المالية")
    
    solvency_checks = [
        "هل الأصول الحالية تغطي الالتزامات المتداولة؟",
        "هل هناك تدفق نقدي إيجابي من النشاط التشغيلي؟",
        "هل نسبة المديونية ضمن المعدلات المقبولة؟",
        "هل هناك قدرة على سداد الفوائد والديون؟",
        "هل الأرباح التشغيلية تغطي المصاريف الثابتة؟"
    ]
    
    positive_checks = 0
    for i, check in enumerate(solvency_checks):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"{i+1}. {check}")
        with col2:
            answer = st.selectbox("", ["نعم", "لا"], key=f"solvency_{i}", label_visibility="collapsed")
            if answer == "نعم":
                positive_checks += 1
    
    st.metric("مؤشر الجدارة المالية", f"{(positive_checks/len(solvency_checks))*100:.0f}%")
    
    if positive_checks >= 4:
        st.success("✅ الوضع المالي جيد - خطر الإفلاس منخفض")
    elif positive_checks >= 2:
        st.warning("⚠️ الوضع المالي يحتاج مراقبة - خطر الإفلاس متوسط")
    else:
        st.error("🚨 الوضع المالي حرج - خطر الإفلاس مرتفع")

# ==========================
# 🔬 قسم الباحثين - المحدث
# ==========================
def show_researchers_section():
    show_breadcrumbs("🔬 قسم الباحثين")
    
    st.markdown("""
    <div class="main-header">
        <h1>🔬 المنصة البحثية في القانون التجاري</h1>
        <p>مصادر ومراجع شاملة للباحثين في القانون التجاري الأردني والمقارن</p>
    </div>
    """, unsafe_allow_html=True)

    research_tabs = st.tabs([
        "📚 المصادر التشريعية", 
        "🎓 الدراسات الأكاديمية",
        "🌍 المقارنات الدولية",
        "🔍 أدوات البحث"
    ])

    with research_tabs[0]:
        show_legislative_sources()

    with research_tabs[1]:
        show_academic_sources()

    with research_tabs[2]:
        show_international_comparisons()

    with research_tabs[3]:
        show_research_tools()

# ==========================
# 📚 المصادر التشريعية
# ==========================
def show_legislative_sources():
    st.markdown("#### 📚 المصادر التشريعية الأساسية")
    
    legislative_sources = [
        {
            "law": "قانون التجارة الأردني",
            "number": "رقم 12 لسنة 1966",
            "description": "القانون الأساسي المنظم للأعمال التجارية والتجار",
            "link": "https://moj.gov.jo"
        },
        {
            "law": "قانون الشركات الأردني",
            "number": "رقم 22 لسنة 1997", 
            "description": "القانون المنظم لتأسيس وإدارة الشركات التجارية",
            "link": "https://mci.gov.jo"
        },
        {
            "law": "قانون حماية المستهلك",
            "number": "رقم 16 لسنة 2004",
            "description": "القانون المنظم لعلاقات التجار مع المستهلكين",
            "link": "https://mci.gov.jo"
        }
    ]
    
    for source in legislative_sources:
        with st.expander(f"📚 {source['law']} {source['number']}", expanded=False):
            st.write(f"**الوصف:** {source['description']}")
            st.write(f"**الرابط:** {source['link']}")

# ==========================
# 🎓 الدراسات الأكاديمية
# ==========================
def show_academic_sources():
    st.markdown("#### 🎓 المصادر الأكاديمية والبحثية")
    
    academic_sources = [
        {
            "type": "المجلات العلمية",
            "examples": "المجلة الأردنية للقانون - مجلة الشريعة والقانون",
            "focus": "أبحاث محكمة في القانون التجاري والشركات"
        },
        {
            "type": "الرسائل الجامعية",
            "examples": "ماجستير ودكتوراه في القانون التجاري",
            "focus": "دراسات متخصصة في فروع القانون التجاري"
        },
        {
            "type": "المؤتمرات العلمية",
            "examples": "مؤتمرات كليات القانون في الجامعات الأردنية",
            "focus": "أوراق بحثية ومناقشات علمية متخصصة"
        }
    ]
    
    for source in academic_sources:
        with st.expander(f"🎓 {source['type']}", expanded=False):
            st.write(f"**أمثلة:** {source['examples']}")
            st.write(f"**التركيز:** {source['focus']}")

# ==========================
# 🌍 المقارنات الدولية
# ==========================
def show_international_comparisons():
    st.markdown("#### 🌍 المقارنات الدولية")
    
    comparisons = [
        {
            "system": "النظام الأنجلو-سكسوني",
            "countries": "بريطانيا، الولايات المتحدة، كندا",
            "features": "Common Law - السوابق القضائية - المرونة"
        },
        {
            "system": "النظام اللاتيني",
            "countries": "فرنسا، بلجيكا، سويسرا",
            "features": "القانون المكتوب - التقنين - الشمولية"
        },
        {
            "system": "النظام الإسلامي",
            "countries": "السعودية، الإمارات، البحرين",
            "features": "الشريعة الإسلامية - المرابحة - المضاربة"
        }
    ]
    
    for comparison in comparisons:
        with st.expander(f"🌍 {comparison['system']}", expanded=False):
            st.write(f"**الدول:** {comparison['countries']}")
            st.write(f"**المميزات:** {comparison['features']}")

# ==========================
# 🔍 أدوات البحث
# ==========================
def show_research_tools():
    st.markdown("#### 🔍 أدوات ومنهجيات البحث")
    
    research_tools = [
        {
            "tool": "المنهج التحليلي",
            "description": "تحليل النصوص القانونية والفقه القضائي",
            "application": "دراسة المواد القانونية وتفسيرها"
        },
        {
            "tool": "المنهج المقارن",
            "description": "مقارنة الأنظمة القانونية المختلفة",
            "application": "دراسة التجارب الدولية واستخلاص الدروس"
        },
        {
            "tool": "المنهج التاريخي",
            "description": "دراسة تطور القوانين والتشريعات",
            "application": "تحليل التعديلات والتطور التشريعي"
        }
    ]
    
    for tool in research_tools:
        with st.expander(f"🔍 {tool['tool']}", expanded=False):
            st.write(f"**الوصف:** {tool['description']}")
            st.write(f"**التطبيق:** {tool['application']}")

# ==========================
# 🧮 قسم الحاسبات - المحدث
# ==========================
def show_calculators_section():
    show_breadcrumbs("🧮 قسم الحاسبات")
    
    st.markdown("""
    <div class="main-header">
        <h1>🧮 الحاسبات التجارية المتكاملة</h1>
        <p>أدوات حسابية دقيقة للعمليات والمعاملات التجارية وفق القانون الأردني</p>
    </div>
    """, unsafe_allow_html=True)

    calculator_tabs = st.tabs([
        "💰 الرهن التجاري",
        "💸 الأوراق التجارية", 
        "🏦 الإفلاس والتسوية",
        "📊 الالتزامات التجارية",
        "🔄 التظهير والكمبيالة",
        "📈 حاسبات متقدمة"
    ])

    with calculator_tabs[0]:
        show_mortgage_calculator()

    with calculator_tabs[1]:
        show_commercial_papers_calculator()

    with calculator_tabs[2]:
        show_bankruptcy_calculator()

    with calculator_tabs[3]:
        show_obligations_calculator()

    with calculator_tabs[4]:
        show_endorsement_calculator()

    with calculator_tabs[5]:
        show_advanced_calculators()

# ==========================
# 💰 الرهن التجاري
# ==========================
def show_mortgage_calculator():
    st.markdown("#### 💰 حاسبة الرهن التجاري")
    
    with st.form("mortgage_calculator"):
        col1, col2 = st.columns(2)
        
        with col1:
            mortgage_value = st.number_input("قيمة الرهن (دينار)", min_value=0, value=50000)
            interest_rate = st.number_input("سعر الفائدة (%)", min_value=0.0, value=5.0)
            
        with col2:
            mortgage_period = st.number_input("مدة الرهن (سنوات)", min_value=1, value=5)
            payment_frequency = st.selectbox("دورية السداد", ["شهري", "ربع سنوي", "سنوي"])
        
        if st.form_submit_button("🧮 احسب أقساط الرهن", use_container_width=True):
            result = calculate_mortgage_payments(mortgage_value, interest_rate, mortgage_period, payment_frequency)
            display_mortgage_result(result)

def calculate_mortgage_payments(principal, rate, years, frequency):
    """حساب أقساط الرهن التجاري"""
    
    # تحويل سعر الفائدة السنوي إلى شهري
    monthly_rate = rate / 100 / 12
    total_payments = years * 12
    
    # حساب القسط الشهري
    if monthly_rate > 0:
        monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** total_payments) / ((1 + monthly_rate) ** total_payments - 1)
    else:
        monthly_payment = principal / total_payments
    
    # ضبط حسب التردد
    if frequency == "شهري":
        payment = monthly_payment
        total_amount = monthly_payment * total_payments
    elif frequency == "ربع سنوي":
        payment = monthly_payment * 3
        total_amount = monthly_payment * total_payments
    else:  # سنوي
        payment = monthly_payment * 12
        total_amount = monthly_payment * total_payments
    
    total_interest = total_amount - principal
    
    return {
        'principal': principal,
        'interest_rate': rate,
        'period': years,
        'payment_frequency': frequency,
        'periodic_payment': payment,
        'total_payments': total_amount,
        'total_interest': total_interest
    }

def display_mortgage_result(result):
    """عرض نتيجة حساب الرهن"""
    
    st.success("## 💰 نتائج حساب الرهن التجاري")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("القسط الدوري", f"{result['periodic_payment']:,.0f} دينار")
    with col2:
        st.metric("إجمالي المدفوع", f"{result['total_payments']:,.0f} دينار")
    with col3:
        st.metric("إجمالي الفائدة", f"{result['total_interest']:,.0f} دينار")
    
    with st.expander("📊 التفاصيل الكاملة", expanded=True):
        st.write(f"**أصل القرض:** {result['principal']:,.0f} دينار")
        st.write(f"**سعر الفائدة:** {result['interest_rate']}%")
        st.write(f"**مدة القرض:** {result['period']} سنوات")
        st.write(f"**دورية السداد:** {result['payment_frequency']}")

# ==========================
# 💸 الأوراق التجارية
# ==========================
def show_commercial_papers_calculator():
    st.markdown("#### 💸 حاسبة الأوراق التجارية")
    
    with st.form("papers_calculator"):
        paper_type = st.selectbox("نوع الورقة التجارية", [
            "كمبيالة",
            "سند إذني",
            "شيك"
        ])
        
        col1, col2 = st.columns(2)
        
        with col1:
            face_value = st.number_input("القيمة الاسمية (دينار)", min_value=0, value=10000)
            issue_date = st.date_input("تاريخ الإنشاء")
            
        with col2:
            discount_rate = st.number_input("سعر الخصم (%)", min_value=0.0, value=8.0)
            maturity_date = st.date_input("تاريخ الاستحقاق")
        
        if st.form_submit_button("🧮 احسب القيمة الحالية", use_container_width=True):
            result = calculate_present_value(face_value, issue_date, maturity_date, discount_rate)
            display_paper_result(result, paper_type)

def calculate_present_value(face_value, issue_date, maturity_date, discount_rate):
    """حساب القيمة الحالية للورقة التجارية"""
    
    # حساب عدد الأيام حتى الاستحقاق
    days_to_maturity = (maturity_date - issue_date).days
    
    # حساب القيمة الحالية
    daily_rate = discount_rate / 100 / 365
    present_value = face_value / (1 + daily_rate * days_to_maturity)
    discount_amount = face_value - present_value
    
    return {
        'face_value': face_value,
        'present_value': present_value,
        'discount_amount': discount_amount,
        'discount_rate': discount_rate,
        'days_to_maturity': days_to_maturity
    }

def display_paper_result(result, paper_type):
    """عرض نتيجة حساب الورقة التجارية"""
    
    st.success(f"## 💸 نتائج حساب {paper_type}")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("القيمة الاسمية", f"{result['face_value']:,.0f} دينار")
    with col2:
        st.metric("القيمة الحالية", f"{result['present_value']:,.0f} دينار")
    with col3:
        st.metric("مبلغ الخصم", f"{result['discount_amount']:,.0f} دينار")
    
    with st.expander("📊 التفاصيل الكاملة", expanded=True):
        st.write(f"**سعر الخصم:** {result['discount_rate']}%")
        st.write(f"**الأيام حتى الاستحقاق:** {result['days_to_maturity']} يوم")

# ==========================
# 🏦 الإفلاس والتسوية
# ==========================
def show_bankruptcy_calculator():
    st.markdown("#### 🏦 حاسبة توزيع أموال الإفلاس")
    
    st.info("استخدم هذه الحاسبة لتقدير توزيع أموال المفلس على الدائنين حسب الأولويات القانونية")
    
    # هذه الدالة مشتركة مع قسم الإفلاس
    show_debt_calculator()

# ==========================
# 📊 الالتزامات التجارية
# ==========================
def show_obligations_calculator():
    st.markdown("#### 📊 حاسبة الالتزامات التجارية")
    
    with st.form("obligations_calculator"):
        col1, col2 = st.columns(2)
        
        with col1:
            contract_value = st.number_input("قيمة العقد (دينار)", min_value=0, value=50000)
            penalty_rate = st.number_input("نسبة الجزاء (%)", min_value=0.0, value=10.0)
            
        with col2:
            delay_days = st.number_input("أيام التأخير", min_value=0, value=30)
            interest_rate = st.number_input("سعر الفائدة القانوني (%)", min_value=0.0, value=8.0)
        
        if st.form_submit_button("🧮 احسب المستحقات", use_container_width=True):
            result = calculate_commercial_obligations(contract_value, penalty_rate, delay_days, interest_rate)
            display_obligations_result(result)

def calculate_commercial_obligations(contract_value, penalty_rate, delay_days, interest_rate):
    """حساب الالتزامات التجارية والجزاءات"""
    
    # حساب الجزاء
    penalty_amount = contract_value * (penalty_rate / 100)
    
    # حساب الفوائد
    daily_interest = interest_rate / 100 / 365
    interest_amount = contract_value * daily_interest * delay_days
    
    total_obligations = penalty_amount + interest_amount
    
    return {
        'contract_value': contract_value,
        'penalty_rate': penalty_rate,
        'penalty_amount': penalty_amount,
        'interest_rate': interest_rate,
        'interest_amount': interest_amount,
        'delay_days': delay_days,
        'total_obligations': total_obligations
    }

def display_obligations_result(result):
    """عرض نتيجة حساب الالتزامات"""
    
    st.success("## 📊 نتائج حساب الالتزامات التجارية")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("مبلغ الجزاء", f"{result['penalty_amount']:,.0f} دينار")
    with col2:
        st.metric("مبلغ الفوائد", f"{result['interest_amount']:,.0f} دينار")
    with col3:
        st.metric("الإجمالي المستحق", f"{result['total_obligations']:,.0f} دينار")
    
    with st.expander("📊 التفاصيل الكاملة", expanded=True):
        st.write(f"**قيمة العقد:** {result['contract_value']:,.0f} دينار")
        st.write(f"**نسبة الجزاء:** {result['penalty_rate']}%")
        st.write(f"**سعر الفائدة:** {result['interest_rate']}%")
        st.write(f"**أيام التأخير:** {result['delay_days']} يوم")

# ==========================
# 🔄 التظهير والكمبيالة
# ==========================
def show_endorsement_calculator():
    st.markdown("#### 🔄 حاسبة تظهير الكمبيالة")
    
    with st.form("endorsement_calculator"):
        col1, col2 = st.columns(2)
        
        with col1:
            bill_amount = st.number_input("مبلغ الكمبيالة (دينار)", min_value=0, value=15000)
            endorsement_count = st.number_input("عدد مرات التظهير", min_value=0, value=3)
            
        with col2:
            discount_per_endorsement = st.number_input("خصم كل تظهير (%)", min_value=0.0, value=1.5)
            processing_fee = st.number_input("رسوم المعالجة (دينار)", min_value=0, value=50)
        
        if st.form_submit_button("🧮 احسب القيمة النهائية", use_container_width=True):
            result = calculate_endorsement_value(bill_amount, endorsement_count, discount_per_endorsement, processing_fee)
            display_endorsement_result(result)

def calculate_endorsement_value(bill_amount, count, discount_rate, processing_fee):
    """حساب قيمة الكمبيالة بعد التظهير"""
    
    total_discount = 0
    current_value = bill_amount
    
    for i in range(count):
        discount = current_value * (discount_rate / 100)
        total_discount += discount
        current_value -= discount
    
    final_value = current_value - processing_fee
    total_fees = (bill_amount - final_value) + processing_fee
    
    return {
        'original_amount': bill_amount,
        'final_amount': final_value,
        'total_discount': total_discount,
        'processing_fee': processing_fee,
        'total_fees': total_fees,
        'endorsement_count': count
    }

def display_endorsement_result(result):
    """عرض نتيجة حساب التظهير"""
    
    st.success("## 🔄 نتائج حساب تظهير الكمبيالة")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("المبلغ الأصلي", f"{result['original_amount']:,.0f} دينار")
    with col2:
        st.metric("المبلغ النهائي", f"{result['final_amount']:,.0f} دينار")
    with col3:
        st.metric("إجمالي الخصومات", f"{result['total_fees']:,.0f} دينار")
    
    with st.expander("📊 التفاصيل الكاملة", expanded=True):
        st.write(f"**عدد مرات التظهير:** {result['endorsement_count']}")
        st.write(f"**إجمالي الخصم:** {result['total_discount']:,.0f} دينار")
        st.write(f"**رسوم المعالجة:** {result['processing_fee']:,.0f} دينار")

# ==========================
# 📈 حاسبات متقدمة
# ==========================
def show_advanced_calculators():
    st.markdown("#### 📈 الحاسبات المتقدمة")
    
    advanced_calcs = [
        {
            "name": "حاسبة الجدارة الائتمانية",
            "description": "تقييم الجدارة الائتمانية للتجار والشركات",
            "features": ["تحليل السيولة", "نسب المديونية", "التدفق النقدي"]
        },
        {
            "name": "حاسبة المخاطر التجارية", 
            "description": "تحليل وتقييم المخاطر في المعاملات التجارية",
            "features": ["مخاطر السوق", "مخاطر الائتمان", "مخاطر التشغيل"]
        },
        {
            "name": "حاسبة التمويل التجاري",
            "description": "تخطيط ودراسة جدوى المشاريع التجارية",
            "features": ["تحليل التكلفة", "توقع الإيرادات", "نقطة التعادل"]
        }
    ]
    
    for calc in advanced_calcs:
        with st.expander(f"📈 {calc['name']}", expanded=False):
            st.write(f"**الوصف:** {calc['description']}")
            st.write("**المميزات:**")
            for feature in calc['features']:
                st.write(f"• {feature}")
            
            st.info("🛠️ هذه الآلة الحاسبة قيد التطوير وسيتم إضافتها بشكل كامل في التحديثات القادمة")

# ==========================
# ⚙️ قسم الإعدادات
# ==========================
def show_settings_section():
    show_breadcrumbs("⚙️ الإعدادات")
    
    st.markdown("""
    <div class="main-header">
        <h1>⚙️ إعدادات المنصة وسياسات الخصوصية</h1>
        <p>إدارة تفضيلاتك ومراجعة سياسات الاستخدام والخصوصية</p>
    </div>
    """, unsafe_allow_html=True)

    settings_tabs = st.tabs(["🔒 الخصوصية والأمان", "📞 الدعم والاتصال", "ℹ️ عن المنصة"])

    with settings_tabs[0]:
        st.markdown("#### 🔒 سياسات الخصوصية والأمان")
        
        st.markdown("""
        <div class="section-card">
        <h4>🚫 سياسة عدم جمع البيانات</h4>
        <p>هذه المنصة <strong>لا تجمع أو تخزين أي بيانات شخصية</strong> عن المستخدمين. 
        جميع البيانات تُحفظ في جلسة المتصفح المؤقتة وتُمسح تلقائياً عند الإغلاق.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.warning("""
        **⚠️ تنويه هام:**
        هذه المنصة توعوية تعليمية فقط ولا تقدم أي خدمات استشارية قانونية.
        المعلومات المقدمة لأغراض المعرفة العامة والتعليم فقط.
        """)

    with settings_tabs[1]:
        st.markdown("#### 📞 قنوات الدعم والاتصال")
        
        st.info("""
        **💼 للاستفسارات الفنية والدعم:**
        نحن هنا لمساعدتك في أي استفسارات فنية أو تقنية متعلقة باستخدام المنصة.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📧 البريد الإلكتروني")
            st.markdown("""
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 10px; border-left: 4px solid #2563EB;">
                <h4 style="margin: 0 0 0.5rem 0;">📧 sirawork2025@gmail.com</h4>
                <p style="margin: 0; color: #666;">للأسئلة الفنية والدعم التقني</p>
            </div>
            """, unsafe_allow_html=True)

    with settings_tabs[2]:
        st.markdown("#### ℹ️ معلومات عن منصة SiraWork")
        
        st.markdown("""
        **🎯 رؤية المنصة:**
        SiraWork منصة توعوية تعليمية تهدف إلى نشر الوعي القانوني في مجال قانون التجارة
        وتوفير أدوات تعليمية تفاعلية للمستخدمين.
        
        **🏆 المميزات:**
        - ✅ مجانية بالكامل
        - ✅ لا تتطلب تسجيل دخول
        - ✅ لا تتبع المستخدمين
        - ✅ تحديثات مستمرة
        
        **📚 المحتوى:**
        - قانون التجارة الأردني وتعديلاته
        - قانون الشركات الأردني
        - الأوراق التجارية والعقود
        - الإفلاس والتسوية الواقية
        """)

# ==========================
# 🚀 التشغيل الرئيسي للتطبيق
# ==========================
def main():
    try:
        # تهيئة حالة الجلسة
        initialize_session_state()
        
        # عرض القائمة الجانبية
        show_sidebar_navigation()
        
        # نظام التوجيه للصفحات
        page_handlers = {
            "home": show_home_page,
            "traders": show_traders_section,
            "companies": show_companies_section,
            "contracts": show_contracts_section,
            "commercial_papers": show_commercial_papers_section,
            "bankruptcy": show_bankruptcy_section,
            "researchers": show_researchers_section,
            "calculators": show_calculators_section,
            "settings": show_settings_section
        }
        
        # الحصول على المعالج المناسب للصفحة
        current_page = st.session_state.selected_page
        page_handler = page_handlers.get(current_page, show_home_page)
        
        # تنفيذ الصفحة المطلوبة
        page_handler()
        
    except Exception as e:
        # معالجة الأخطاء
        st.error("""
        ## ⚠️ حدث خطأ غير متوقع
        
        نعتذر عن هذا الخطأ. يرجى:
        1. تحديث الصفحة
        2. التأكد من اتصال الإنترنت
        3. التواصل مع الدعم إذا استمرت المشكلة
        """)
        
        # زر لتحديث الصفحة
        if st.button("🔄 تحديث الصفحة"):
            st.rerun()

if __name__ == "__main__":
    main()