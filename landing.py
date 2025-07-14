import streamlit as st
from utils import rerun
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def landing_page():
    st.set_page_config(
        page_title="MediCare+ | Advanced Online Healthcare Platform",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Encode the local image to base64
    img_path = "1752061034840.jpg"  # Change to your image filename
    img_base64 = get_base64_of_bin_file(img_path)

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@300;400;500;600;700&display=swap');
    
    /* Hide default Streamlit elements */
    header, #MainMenu, footer, .stDeployButton {{
        visibility: hidden;
        height: 0;
        padding: 0;
        margin: 0;
    }}

    /* Custom scrollbar */
    ::-webkit-scrollbar {{
        width: 8px;
    }}
    
    ::-webkit-scrollbar-track {{
        background: #f1f1f1;
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: linear-gradient(45deg, #667eea, #764ba2);
        border-radius: 10px;
    }}

    /* Main app styling */
    .stApp {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        min-height: 100vh;
        font-family: 'Inter', sans-serif;
    }}

    /* Floating navigation */
    .floating-nav {{
        position: fixed;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 50px;
        padding: 10px 30px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        z-index: 1000;
        animation: slideDown 0.8s ease-out;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }}

    .nav-items {{
        display: flex;
        gap: 30px;
        align-items: center;
    }}

    .nav-logo {{
        font-size: 1.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-right: 20px;
    }}

    .nav-item {{
        color: #4a5568;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s ease;
        cursor: pointer;
    }}

    .nav-item:hover {{
        color: #667eea;
    }}

    /* Hero section */
    .hero-container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 80px 20px 60px;
        text-align: center;
    }}

    .hero-badge {{
        display: inline-block;
        background: rgba(255, 255, 255, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 50px;
        padding: 8px 20px;
        color: white;
        font-size: 0.9rem;
        margin-bottom: 30px;
        animation: fadeIn 1s ease-out;
    }}

    .hero-title {{
        font-size: 4rem;
        font-weight: 800;
        color: white;
        margin-bottom: 20px;
        line-height: 1.1;
        animation: fadeInUp 1.2s ease-out;
        text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }}

    .hero-subtitle {{
        font-size: 1.3rem;
        color: rgba(255, 255, 255, 0.9);
        margin-bottom: 40px;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.6;
        animation: fadeInUp 1.4s ease-out;
    }}

    .hero-stats {{
        display: flex;
        justify-content: center;
        gap: 60px;
        margin: 50px 0;
        animation: fadeInUp 1.6s ease-out;
    }}

    .stat-item {{
        text-align: center;
        color: white;
    }}

    .stat-number {{
        font-size: 2.5rem;
        font-weight: 700;
        display: block;
        margin-bottom: 5px;
    }}

    .stat-label {{
        font-size: 1rem;
        opacity: 0.9;
    }}

    /* CTA Buttons */
    .cta-buttons {{
        display: flex;
        justify-content: center;
        gap: 20px;
        margin: 40px 0;
        animation: fadeInUp 1.8s ease-out;
    }}

    .btn-primary {{
        background: white;
        color: #667eea;
        border: none;
        border-radius: 50px;
        padding: 15px 40px;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        text-decoration: none;
        display: inline-block;
    }}

    .btn-primary:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
    }}

    .btn-secondary {{
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: 2px solid rgba(255, 255, 255, 0.3);
        border-radius: 50px;
        padding: 15px 40px;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
        backdrop-filter: blur(10px);
    }}

    .btn-secondary:hover {{
        background: rgba(255, 255, 255, 0.2);
        transform: translateY(-3px);
    }}

    /* Features section */
    .features-section {{
        background: white;
        padding: 100px 0;
        margin-top: 60px;
    }}

    .features-container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }}

    .section-title {{
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        color: #2d3748;
        margin-bottom: 60px;
        position: relative;
    }}

    .section-title::after {{
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 4px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 2px;
    }}

    .features-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 30px;
        margin-bottom: 60px;
    }}

    .feature-card {{
        background: white;
        border-radius: 20px;
        padding: 40px 30px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        border: 1px solid rgba(0, 0, 0, 0.05);
        position: relative;
        overflow: hidden;
    }}

    .feature-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        transform: scaleX(0);
        transition: transform 0.3s ease;
    }}

    .feature-card:hover::before {{
        transform: scaleX(1);
    }}

    .feature-card:hover {{
        transform: translateY(-10px);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
    }}

    .feature-icon {{
        width: 80px;
        height: 80px;
        margin: 0 auto 20px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        color: white;
    }}

    .feature-title {{
        font-size: 1.4rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 15px;
    }}

    .feature-desc {{
        color: #718096;
        line-height: 1.6;
        font-size: 1rem;
    }}

    /* Services section */
    .services-section {{
        background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
        padding: 100px 0;
    }}

    .services-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 30px;
        margin-top: 60px;
    }}

    .service-card {{
        background: white;
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        cursor: pointer;
    }}

    .service-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.12);
    }}

    .service-icon {{
        width: 60px;
        height: 60px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        color: white;
        margin-bottom: 20px;
    }}

    .service-title {{
        font-size: 1.2rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 10px;
    }}

    .service-desc {{
        color: #718096;
        font-size: 0.95rem;
        line-height: 1.5;
    }}

    /* Testimonials section */
    .testimonials-section {{
        background: white;
        padding: 100px 0;
    }}

    .testimonials-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 30px;
        margin-top: 60px;
    }}

    .testimonial-card {{
        background: #f7fafc;
        border-radius: 20px;
        padding: 30px;
        position: relative;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
    }}

    .testimonial-text {{
        font-style: italic;
        color: #4a5568;
        margin-bottom: 20px;
        font-size: 1.1rem;
        line-height: 1.6;
    }}

    .testimonial-author {{
        display: flex;
        align-items: center;
        gap: 15px;
    }}

    .author-avatar {{
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea, #764ba2);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 600;
        font-size: 1.2rem;
    }}

    .author-info {{
        flex: 1;
    }}

    .author-name {{
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 2px;
    }}

    .author-role {{
        color: #718096;
        font-size: 0.9rem;
    }}

    /* Footer */
    .footer {{
        background: #2d3748;
        color: white;
        padding: 60px 0 30px;
    }}

    .footer-content {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 40px;
    }}

    .footer-section h3 {{
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 20px;
        color: white;
    }}

    .footer-section p, .footer-section li {{
        color: #a0aec0;
        line-height: 1.6;
        margin-bottom: 10px;
    }}

    .footer-section ul {{
        list-style: none;
        padding: 0;
    }}

    .footer-section a {{
        color: #a0aec0;
        text-decoration: none;
        transition: color 0.3s ease;
    }}

    .footer-section a:hover {{
        color: #667eea;
    }}

    .footer-bottom {{
        text-align: center;
        padding-top: 30px;
        border-top: 1px solid #4a5568;
        color: #a0aec0;
    }}

    /* Streamlit button override */
    .stButton > button {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 15px 40px;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        width: 100%;
        margin: 20px 0;
    }}

    .stButton > button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.4);
    }}

    /* Animations */
    @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}

    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(30px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}

    @keyframes slideDown {{
        from {{ transform: translateX(-50%) translateY(-100%); }}
        to {{ transform: translateX(-50%) translateY(0); }}
    }}

    @keyframes float {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-20px); }}
    }}

    /* Responsive design */
    @media (max-width: 768px) {{
        .hero-title {{
            font-size: 2.5rem;
        }}
        
        .hero-stats {{
            flex-direction: column;
            gap: 30px;
        }}
        
        .cta-buttons {{
            flex-direction: column;
            align-items: center;
        }}
        
        .floating-nav {{
            position: relative;
            top: 0;
            left: 0;
            transform: none;
            margin: 20px;
            border-radius: 15px;
        }}
        
        .nav-items {{
            flex-direction: column;
            gap: 15px;
        }}
        
        .features-grid, .services-grid, .testimonials-grid {{
            grid-template-columns: 1fr;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)



    # Hero Section
    st.markdown("""
    <div class="hero-container">
        <div class="hero-badge">✨ Trusted by 50,000+ patients worldwide</div>
        <h1 class="hero-title">Your Health, Our Priority</h1>
        <p class="hero-subtitle">Experience the future of healthcare with our comprehensive online platform. Get medicines delivered, consult with expert doctors, and manage your health from anywhere.</p>
    </div>
    """, unsafe_allow_html=True)

    # CTA Buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 Get Started Now", key="start_button", help="Start your healthcare journey"):
            st.session_state["current_page"] = "login"
            rerun(st)

    # Features Section
    st.markdown("""
    <div class="features-section">
        <div class="features-container">
            <h2 class="section-title">Why Choose MediCare+?</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">🛒</div>
                    <h3 class="feature-title">Easy Medicine Ordering</h3>
                    <p class="feature-desc">Browse through thousands of medicines, upload prescriptions, and get them delivered to your doorstep with just a few clicks.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">👩‍⚕️</div>
                    <h3 class="feature-title">Expert Doctor Consultations</h3>
                    <p class="feature-desc">Connect with certified doctors via video calls, chat, or phone. Get professional medical advice from the comfort of your home.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">⚡</div>
                    <h3 class="feature-title">Fast & Secure Delivery</h3>
                    <p class="feature-desc">Same-day delivery in major cities, secure packaging, and real-time tracking. Your health can't wait, and neither do we.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🔒</div>
                    <h3 class="feature-title">Privacy & Security</h3>
                    <p class="feature-desc">Your medical data is encrypted and protected with bank-level security. HIPAA compliant and ISO certified platform.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">💰</div>
                    <h3 class="feature-title">Best Prices Guaranteed</h3>
                    <p class="feature-desc">Compare prices, get discounts, and save up to 60% on your medical expenses. Insurance claims made easy.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">📱</div>
                    <h3 class="feature-title">Mobile App Available</h3>
                    <p class="feature-desc">Download our mobile app for iOS and Android. Manage your health on-the-go with offline access to medical records.</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

   
    # Footer
    st.markdown("""
    <div class="footer">
        <div class="footer-content">
            <div class="footer-section">
                <h3>MediCare+</h3>
                <p>Your trusted partner in health and wellness. We're committed to making healthcare accessible, affordable, and convenient for everyone.</p>
            </div>
            <div class="footer-section">
                <h3>Quick Links</h3>
                <ul>
                    <li><a href="#about">About Us</a></li>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#doctors">Our Doctors</a></li>
                    <li><a href="#careers">Careers</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Support</h3>
                <ul>
                    <li><a href="#help">Help Center</a></li>
                    <li><a href="#contact">Contact Us</a></li>
                    <li><a href="#privacy">Privacy Policy</a></li>
                    <li><a href="#terms">Terms of Service</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Contact Info</h3>
                <p>📧 support@medicareplus.com</p>
                <p>📞 1-800-MEDICARE</p>
                <p>📍 123 Health Street, Medical City, MC 12345</p>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2025 MediCare+. All rights reserved. | Licensed Healthcare Provider</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Example usage:
# landing_page()