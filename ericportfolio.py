import streamlit as st
from PIL import Image

# Set page title and icon
st.set_page_config(page_title="Student Portfolio", page_icon="🎓")

# Initialize session state for timeline, testimonials, and profile
if 'timeline' not in st.session_state:
    st.session_state.timeline = [
        {
            'year': '2023',
            'title': 'University Enrollment',
            'description': 'Started BSc in Computer Science at INES-Ruhengeri'
        },
        {
            'year': '2024',
            'title': 'First Programming Competition',
            'description': 'Participated in the national coding hackathon and secured 3rd position'
        },
        {
            'year': '2025',
            'title': 'Internship at Tech Company',
            'description': 'Completed a 2-month internship at a leading software company'
        },
        {
            'year': '2025',
            'title': 'Dissertation Submission',
            'description': 'Working on final year project: healthcare fraud detection system using machine learning'
        }
    ]

if 'testimonials' not in st.session_state:
    st.session_state.testimonials = [
        {
            'text': 'Clement is a brilliant problem solver! His final year project was truly innovative.',
            'author': 'mr.clement'
        }
    ]

if 'profile' not in st.session_state:
    st.session_state.profile = {
        'name': 'TUYISENGE Eric',
        'location': 'Musanze, Rwanda',
        'university': 'INES - Ruhengeri',
        'field': 'Computer Science, SWE',
        'bio': 'I am software engineer!',
        'email': 'ug2321737@ines.ac.rw',
        'phone': '+250789595211',
        'github': 'https://github.com/t-eric12',
        'linkedin': 'https://www.linkedin.com/in/eric-tuyisenge-54702634b/',
    }

# Sidebar navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go To:", ["Home", "Projects", "Skills", "Timeline", "Testimonials", "Contact", "Customize Profile"])

# Home section
if page == "Home":
    st.title("🎓 Student Portfolio")
    uploaded_image = st.file_uploader("Upload Profile Picture", type=["jpg", "png"])
    if uploaded_image is not None:
        st.image(uploaded_image, width=150, caption="Uploaded image")
    else:
        st.image("AAA.jpg", width=150, caption="Default image")
    
    name = st.text_input("Name: ", "TUYISENGE Eric")
    location = st.text_input("Location: ", "Musanze, Rwanda")
    field_of_study = st.text_input("Field of Study: ", "Computer Science, SWE")
    university = st.text_input("University: ", "INES - Ruhengeri")
    
    st.write(f"📍{location}")
    st.write(f"📚{field_of_study}")
    st.write(f"🎓{university}")
    
    with open("ERI.pdf", "rb") as file:
        resume_bytes = file.read()
    st.download_button(label="📄Download Resume", data=resume_bytes, file_name="ERI.pdf", mime="application/pdf")
    
    st.markdown("---")
    st.subheader("About Me")
    about_me = st.text_area("Short introduction about myself:", "I am software engineer!")
    st.write(about_me)

# Projects section
elif page == "Projects":
    st.title("💻 My Projects")
    
    with st.expander("📊 E farming management system"):
        st.write(" 'type': 'Individual Project',")
        st.write("year 1")
        st.write('discription:''Developed e farming management system using Python gui')
        st.write( 'link:' 'https://github.com/t-eric12/dilichieric.git')
    
    with st.expander("traffic simulator system"):
        st.write(" 'type': 'group work Project',")
        st.write("year 2")
        st.write('discription:''Developed taffic simulator system using Python ')
        st.write( 'link:' 'https://github.com/t-eric12/traffic_simulatorsystem.git')
            

          
    
    with st.expander("🌐 banking system"):
        st.write(" 'type': 'group Project',")
        st.write("year 3")
        st.write('discription:''Developed banking system using Python ')
        st.write( 'link:' 'https://github.com/t-eric12/bank_system.git')

# Skills section
elif page == "Skills":
    st.title("⚡ Skills and Achievements")
    
    st.subheader("Programming Skills")
    skill_python = st.slider("Python", 0, 100, 90)
    st.progress(skill_python)
    
    skill_js = st.slider("JavaScript", 0, 100, 75)
    st.progress(skill_js)
    
    skill_AI = st.slider("Artificial Intelligence", 0, 100, 65)
    st.progress(skill_AI)
    
    st.subheader("Certifications & Achievements")
    st.write("✔ Complete introduction to python in Business Certification")
    st.write("✔ Certified of microsoft office")

# Timeline section
elif page == "Timeline":
    st.title("📅 My Academic Journey")
    
    for item in st.session_state.timeline:
        st.markdown(f"""
        <div class="timeline-item">
            <h3>{item['year']} - {item['title']}</h3>
            <p>{item['description']}</p>
        </div>
        """, unsafe_allow_html=True)

# Testimonials section
elif page == "Testimonials":
    st.title("🌟 Testimonials")
    
    for testimonial in st.session_state.testimonials:
        st.markdown(f"""
        <div class="testimonial-card">
            <p style="font-style: italic;">"{testimonial['text']}"</p>
            <p style="text-align: right; font-weight: bold;">— {testimonial['author']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### Add a New Testimonial")
    with st.form("new_testimonial"):
        new_testimonial_text = st.text_area("Testimonial")
        new_testimonial_author = st.text_input("Author")
        submit_testimonial = st.form_submit_button("Add Testimonial")
        
        if submit_testimonial and new_testimonial_text and new_testimonial_author:
            st.session_state.testimonials.append({
                'text': new_testimonial_text,
                'author': new_testimonial_author
            })
            st.success("Testimonial added successfully!")

# Contact section
elif page == "Contact":
    st.title("📬 Contact Me")
    
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            st.success("✅ Message sent successfully")
    
    st.write("📧 Email: tuyisengeeric034@gmail.com")
    st.write("[🔗 LinkedIn](https://www.linkedin.com/in/eric-tuyisenge-54702634b/)")
    st.write("[📂 GitHub](https://github.com/t-eric12)")

# Customize Profile section
elif page == "Customize Profile":
    st.title("🎨 Customize Your Profile")
    
    with st.form("profile_customization"):
        st.markdown("### Personal Information")
        name = st.text_input("Full Name", st.session_state.profile['name'])
        location = st.text_input("Location", st.session_state.profile['location'])
        university = st.text_input("University", st.session_state.profile['university'])
        field = st.text_input("Field of Study", st.session_state.profile['field'])
        bio = st.text_area("Bio", st.session_state.profile['bio'])
        
        st.markdown("### Contact Information")
        email = st.text_input("Email", st.session_state.profile['email'])
        phone = st.text_input("Phone", st.session_state.profile['phone'])
        github = st.text_input("GitHub URL", st.session_state.profile['github'])
        linkedin = st.text_input("LinkedIn URL", st.session_state.profile['linkedin'])
        
        st.markdown("### Profile Picture")
        profile_pic = st.file_uploader("Upload your profile picture", type=["jpg", "jpeg", "png"])
        
        if profile_pic is not None:
            st.session_state.profile_pic = Image.open(profile_pic)
            st.image(st.session_state.profile_pic, width=150)
        
        submitted = st.form_submit_button("Save Changes")
        
        if submitted:
            st.session_state.profile.update({
                'name': name,
                'location': location,
                'university': university,
                'field': field,
                'bio': bio,
                'email': email,
                'phone': phone,
                'github': github,
                'linkedin': linkedin
            })
            st.success("Profile updated successfully!")