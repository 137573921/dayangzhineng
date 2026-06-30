"""
大洋智能科技 - 官网 Flask 应用
"""
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'dayang-tech-secret-2026'

# ========== 数据层（模拟数据库）==========
COMPANY = {
    'name': '大洋智能科技',
    'slogan': '智能科技 · 驱动未来',
    'founded': 2015,
    'description': '深耕人工智能、物联网与大数据技术，为政企客户提供全栈式数字化解决方案。',
}

PRODUCTS = [
    {
        'name': '智能物联平台',
        'desc': '百万级设备并发接入，提供设备管理与远程控制的一体化 IoT 基座。',
        'tags': ['设备管理', '边缘计算', '协议适配'],
    },
    {
        'name': '数据智能引擎',
        'desc': '海量数据实时处理与分析，内置可视化大屏与 BI 报表能力。',
        'tags': ['实时分析', '数据治理', '可视化'],
    },
    {
        'name': 'AI 视觉算法',
        'desc': '基于深度学习的视觉识别引擎，支持 200+ 场景算法。',
        'tags': ['目标检测', '行为分析', '边缘部署'],
    },
    {
        'name': '云端服务平台',
        'desc': '弹性云原生架构，提供微服务治理与 DevOps 自动化能力。',
        'tags': ['云原生', '微服务', 'DevOps'],
    },
]

SOLUTIONS = [
    {'name': '智慧城市', 'desc': '城市运行一网统管，涵盖智慧政务、公共安全与城市大脑。'},
    {'name': '智慧工业', 'desc': '工业互联网平台赋能制造升级，实现设备预测性维护与质量检测。'},
    {'name': '智慧交通', 'desc': '交通信号智能优化、车路协同与拥堵预警，构建高效交通体系。'},
    {'name': '智慧医疗', 'desc': '医学影像 AI 辅助诊断、智慧病房与远程医疗协作。'},
]

ADVANTAGES = [
    {'title': '核心优势', 'desc': '自研核心技术，核心代码自主率超 90%'},
    {'title': '快速交付', 'desc': '标准化产品 + 模块化定制，交付周期缩短 40%'},
    {'title': '行业经验', 'desc': '十年深耕，深入理解政务、制造、交通、医疗业务'},
]

CONTACT_INFO = {
    'address': '深圳市南山区科技园粤兴二道 10 号',
    'phone': '400-888-6688',
    'email': 'contact@dayang-tech.com',
    'hours': '周一至周日 9:00 — 21:00',
}

NAV_LINKS = [
    {'url': 'index', 'label': '首页'},
    {'url': 'products', 'label': '产品服务'},
    {'url': 'solutions', 'label': '解决方案'},
    {'url': 'about', 'label': '关于我们'},
    {'url': 'contact', 'label': '联系我们'},
]


# ========== 路由层 ==========
@app.route('/')
def index():
    """首页：Hero + 产品概览 + 解决方案概览"""
    return render_template(
        'index.html',
        company=COMPANY,
        products=PRODUCTS,
        solutions=SOLUTIONS[:2],  # 首页只展示前两个方案
        nav_links=NAV_LINKS,
        active='index',
    )


@app.route('/products')
def products():
    """产品服务页"""
    return render_template(
        'products.html',
        company=COMPANY,
        products=PRODUCTS,
        nav_links=NAV_LINKS,
        active='products',
    )


@app.route('/solutions')
def solutions():
    """解决方案页"""
    return render_template(
        'solutions.html',
        company=COMPANY,
        solutions=SOLUTIONS,
        nav_links=NAV_LINKS,
        active='solutions',
    )


@app.route('/about')
def about():
    """关于我们页"""
    return render_template(
        'about.html',
        company=COMPANY,
        advantages=ADVANTAGES,
        nav_links=NAV_LINKS,
        active='about',
    )


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """联系我们页（支持表单提交）"""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        phone = request.form.get('phone', '').strip()
        company_name = request.form.get('company', '').strip()
        message = request.form.get('message', '').strip()

        # 简单校验
        if not name or not phone:
            flash('请填写姓名和手机号', 'error')
            return render_template(
                'contact.html',
                company=COMPANY,
                contact_info=CONTACT_INFO,
                nav_links=NAV_LINKS,
                active='contact',
            )

        # 这里可以接入数据库或邮件通知
        # 实际项目中：db.session.add(Inquiry(...)) 或 send_email(...)
        flash(f'感谢您的咨询，{name}！我们的顾问将在 24 小时内与您联系。', 'success')
        return redirect(url_for('contact'))

    return render_template(
        'contact.html',
        company=COMPANY,
        contact_info=CONTACT_INFO,
        nav_links=NAV_LINKS,
        active='contact',
    )


# ========== 错误处理 ==========
@app.errorhandler(404)
def page_not_found(e):
    return render_template(
        '404.html',
        company=COMPANY,
        nav_links=NAV_LINKS,
        active='',
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
