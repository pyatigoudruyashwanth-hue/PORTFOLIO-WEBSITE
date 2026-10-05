from pathlib import Path

root = Path(r"C:\Users\praka\OneDrive\Desktop\portfolio.harsha\portfoliobuilding")
(root / "public" / "resume").mkdir(parents=True, exist_ok=True)

portfolio_js = """export const navItems = [
  { label: 'Home', id: 'home' },
  { label: 'About', id: 'about' },
  { label: 'Skills', id: 'skills' },
  { label: 'Projects', id: 'projects' },
  { label: 'Activities', id: 'activities' },
  { label: 'Profiles', id: 'profiles' },
  { label: 'Education', id: 'education' },
  { label: 'Certificates', id: 'certificates' },
  { label: 'Resume', id: 'resume' },
  { label: 'Contact', id: 'contact' }
]

export const profile = {
  name: 'P Yashwanth',
  fullName: 'P Yashwanth',
  degree: 'BTech – Computer Science and Engineering',
  studyStatus: '2nd Year Student',
  college: 'REVA University, Bengaluru',
  year: '2nd Year',
  semester: '3rd Semester',
  location: 'Bengaluru, Karnataka, India',
  email: 'YOUR_EMAIL@example.com',
  github: 'https://github.com/pyatigoudruyashwanth-hue',
  linkedin: '',
  leetcode: 'https://leetcode.com/u/yashu_P/',
  hackerrank: 'https://www.hackerrank.com/profile/pyatigoudruyash1',
  resumePath: '/resume/P_Yashwanth_Resume.pdf',
  tagline: 'Building Skills in AI, Machine Learning, Python & Software Development',
  heroDescription: 'I am a Computer Science and Engineering student at REVA University, continuously developing my programming, problem-solving and AI/ML skills through projects, coding activities, hackathons and practical learning.',
  about: 'I am P Yashwanth, a second-year BTech Computer Science and Engineering student at REVA University. I am interested in Artificial Intelligence, Machine Learning, Python, software development and problem solving.\n\nI am continuously improving my technical skills through programming practice, Data Structures and Algorithms, coding platforms, development projects, hackathons and collaborative learning.\n\nMy goal is to build practical solutions, strengthen my programming fundamentals and develop the skills required for future internships and software/AI opportunities.'
}

export const quickProfile = [
  { label: 'Name', value: 'P Yashwanth' },
  { label: 'Education', value: 'BTech – Computer Science and Engineering' },
  { label: 'University', value: 'REVA University' },
  { label: 'Year', value: '2nd Year' },
  { label: 'Semester', value: '3rd Semester' },
  { label: 'Interests', value: 'AI • ML • Python • Software Development' },
  { label: 'Location', value: 'Bengaluru, Karnataka, India' }
]

export const skills = [
  {
    group: 'Programming Languages',
    level: 'Developing',
    items: ['C', 'C++', 'Java', 'Python', 'SQL']
  },
  {
    group: 'AI / Machine Learning',
    level: 'Learning',
    items: ['Artificial Intelligence', 'Machine Learning', 'Computer Vision', 'Object Detection', 'OpenCV', 'YOLO']
  },
  {
    group: 'Computer Science',
    level: 'Working Knowledge',
    items: ['Data Structures', 'Algorithms', 'Object-Oriented Programming', 'Database Management Systems', 'Problem Solving']
  },
  {
    group: 'Development Tools',
    level: 'Developing',
    items: ['Git', 'GitHub', 'VS Code', 'HTML', 'CSS', 'JavaScript']
  }
]

export const projects = [
  {
    number: '01',
    title: 'AI-Based Intelligent Video Analytics Platform for Border Surveillance Using Existing CCTV Infrastructure',
    description: 'An AI-based video analytics platform designed to add an intelligent monitoring layer to existing CCTV infrastructure. The system uses computer vision and object detection to identify people and vehicles and detect restricted-zone intrusion.',
    type: 'Hackathon / AI & Computer Vision Project',
    features: [
      'Person detection',
      'Vehicle detection',
      'Restricted-zone intrusion detection',
      'Activity analysis',
      'Risk/event detection',
      'Event logging',
      'SQL database integration',
      'Alert generation',
      'Security dashboard'
    ],
    tech: ['Python', 'OpenCV', 'YOLO', 'AI', 'SQL'],
    github: null,
    demo: null,
    architecture: [
      'Existing CCTV',
      'Video Stream',
      'Python + AI',
      'Object Detection',
      'Activity Analysis',
      'Risk Engine',
      'SQL Database + Alert System',
      'Security Dashboard',
      'Security Officer'
    ]
  },
  {
    number: '02',
    title: 'Programming & Algorithmic Problem Solving',
    description: 'An ongoing collection of programming practice focused on strengthening problem-solving skills, algorithms, data structures and programming fundamentals.',
    type: 'Practice & Learning',
    features: [
      'GitHub repository',
      'Problems solved',
      'Screenshots',
      'Notes'
    ],
    tech: ['C', 'C++', 'Java', 'Python'],
    github: null,
    demo: null,
    metadata: [
      { label: 'GitHub repository', value: 'Coming Soon' },
      { label: 'Problems solved', value: 'Coming Soon' },
      { label: 'Screenshots', value: 'Coming Soon' },
      { label: 'Notes', value: 'Coming Soon' }
    ]
  },
  {
    number: '03',
    title: 'More Projects Coming Soon',
    description: 'Currently learning, experimenting and building new projects in software development, Python, AI and Machine Learning.',
    type: 'Learning Phase',
    features: ['Coming Soon'],
    tech: ['Python', 'AI', 'ML', 'Software Development'],
    github: null,
    demo: null,
    metadata: []
  }
]

export const activities = [
  'Problem identification',
  'AI-based solution design',
  'CCTV video analysis',
  'Object detection',
  'Restricted-zone detection',
  'Database integration',
  'Security event logging',
  'Dashboard development',
  'Technical presentation',
  'Prototype development'
]

export const codingProfiles = [
  {
    name: 'GitHub',
    username: 'pyatigoudruyashwanth-hue',
    url: 'https://github.com/pyatigoudruyashwanth-hue',
    button: 'Visit GitHub',
    tag: 'GH'
  },
  {
    name: 'LeetCode',
    username: 'yashu_P',
    url: 'https://leetcode.com/u/yashu_P/',
    button: 'Visit LeetCode',
    tag: 'LC'
  },
  {
    name: 'HackerRank',
    username: 'pyatigoudruyash1',
    url: 'https://www.hackerrank.com/profile/pyatigoudruyash1',
    button: 'Visit HackerRank',
    tag: 'HR'
  }
]

export const education = {
  university: 'REVA University, Bengaluru',
  degree: 'BTech – Computer Science and Engineering',
  year: '2nd Year',
  semester: '3rd Semester',
  notes: 'Continuously building coding, problem-solving and AI/ML fundamentals.'
}

export const certificates = {
  message: 'Certificates and achievements will be added as I continue my learning journey.',
  categories: ['Programming', 'AI/ML', 'Cloud', 'Hackathons', 'Workshops', 'Certifications', 'Academic achievements']
}

export const socialLinks = [
  { label: 'GitHub', url: 'https://github.com/pyatigoudruyashwanth-hue', tag: 'GH' },
  { label: 'LinkedIn', url: '', tag: 'in' },
  { label: 'LeetCode', url: 'https://leetcode.com/u/yashu_P/', tag: 'LC' },
  { label: 'HackerRank', url: 'https://www.hackerrank.com/profile/pyatigoudruyash1', tag: 'HR' }
]
"""

main_js = """import { useEffect, useState } from 'react'
import { createRoot } from 'react-dom/client'
import { ArrowUpRight, Check, Code2, Github, Mail, Menu, X } from 'lucide-react'
import {
  activities,
  certificates,
  codingProfiles,
  education,
  navItems,
  profile,
  projects,
  quickProfile,
  skills,
  socialLinks
} from './data/portfolio'
import './styles.css'

const brandInitials = profile.name.split(' ').map((piece) => piece[0]).join('').slice(0, 2).toUpperCase()

const getLinkProps = (url) => {
  if (!url) {
    return { href: '#', target: undefined, rel: undefined, disabled: true }
  }

  return { href: url, target: '_blank', rel: 'noreferrer', disabled: false }
}

function App() {
  const [menuOpen, setMenuOpen] = useState(false)
  const [activeSection, setActiveSection] = useState('home')

  useEffect(() => {
    const sections = document.querySelectorAll('main section[id]')
    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries.find((entry) => entry.isIntersecting)
        if (visible) {
          setActiveSection(visible.target.id)
        }
      },
      { rootMargin: '-20% 0px -60% 0px' }
    )

    sections.forEach((section) => observer.observe(section))
    return () => observer.disconnect()
  }, [])

  return (
    <>
      <header className="site-header">
        <a className="brand" href="#home" aria-label="Go to home section">
          <span>{brandInitials}</span>
          <strong>{profile.name}</strong>
        </a>

        <button
          className="menu-toggle"
          type="button"
          aria-label="Toggle navigation"
          aria-expanded={menuOpen}
          onClick={() => setMenuOpen((current) => !current)}
        >
          {menuOpen ? <X size={20} /> : <Menu size={20} />}
        </button>

        <nav className={`site-nav ${menuOpen ? 'open' : ''}`} aria-label="Main navigation">
          {navItems.map((item) => (
            <a
              key={item.id}
              href={`#${item.id}`}
              className={activeSection === item.id ? 'active' : ''}
              onClick={() => setMenuOpen(false)}
            >
              {item.label}
            </a>
          ))}
          <a className="nav-button" href={profile.resumePath} target="_blank" rel="noreferrer">
            Resume
          </a>
        </nav>
      </header>

      <main id="home">
        <section className="hero section-shell" id="home">
          <div className="hero-copy reveal">
            <p className="eyebrow"><span className="status-dot" /> {profile.studyStatus}</p>
            <h1>
              {profile.name}
              <span className="accent-line">{profile.tagline}</span>
            </h1>
            <p className="hero-role">{profile.degree}</p>
            <p className="hero-description">{profile.heroDescription}</p>

            <div className="hero-actions">
              <a className="button button-primary" href="#projects">View Projects</a>
              <a className="button button-secondary" href="#about">About Me</a>
              <a className="button button-secondary" href={profile.resumePath} target="_blank" rel="noreferrer">Download Resume</a>
              <a className="button button-primary" href="#contact">Contact Me</a>
            </div>

            <div className="social-row" aria-label="Social profiles">
              {socialLinks.map((profileLink) => {
                const linkProps = getLinkProps(profileLink.url)
                return (
                  <a
                    key={profileLink.label}
                    className={`social-pill ${linkProps.disabled ? 'is-disabled' : ''}`}
                    href={linkProps.href}
                    target={linkProps.target}
                    rel={linkProps.rel}
                    aria-label={profileLink.label}
                    onClick={linkProps.disabled ? (event) => event.preventDefault() : undefined}
                  >
                    <span>{profileLink.tag}</span>
                    {profileLink.label}
                  </a>
                )
              })}
            </div>
          </div>

          <div className="hero-art" aria-hidden="true">
            <div className="orbit orbit-one" />
            <div className="orbit orbit-two" />
            <div className="orbit orbit-three" />
            <div className="art-window">
              <div className="window-header">
                <span className="dot red" />
                <span className="dot yellow" />
                <span className="dot green" />
              </div>
              <div className="window-body">
                <Code2 size={28} />
                <div className="code-lines">
                  <span>AI / ML</span>
                  <span>Python</span>
                  <span>Data Structures</span>
                </div>
              </div>
            </div>
            <div className="floating-tag tag-one">AI</div>
            <div className="floating-tag tag-two">Python</div>
            <div className="floating-tag tag-three">CSE</div>
          </div>
        </section>

        <section className="about-band">
          <div className="section-shell about-grid" id="about">
            <div className="section-heading">
              <p className="eyebrow">About Me</p>
              <h2>Building practical skills for the future.</h2>
            </div>

            <div className="about-text">
              <p>{profile.about}</p>
              <div className="about-links">
                <a href={`mailto:${profile.email}`}>Email Me <ArrowUpRight size={15} /></a>
                <a href={profile.github} target="_blank" rel="noreferrer">GitHub Profile <ArrowUpRight size={15} /></a>
              </div>
            </div>
          </div>
        </section>

        <section className="section-shell section-block" id="quick-profile">
          <div className="section-intro">
            <p className="eyebrow">Quick Profile</p>
            <h2>Student profile at a glance.</h2>
          </div>

          <div className="quick-grid">
            {quickProfile.map((item) => (
              <div key={item.label} className="info-card">
                <span>{item.label}</span>
                <strong>{item.value}</strong>
              </div>
            ))}
          </div>
        </section>

        <section className="section-shell section-block" id="skills">
          <div className="section-intro">
            <p className="eyebrow">Skills</p>
            <h2>Focused on fundamentals, learning and practical growth.</h2>
          </div>

          <div className="skills-grid">
            {skills.map((group) => (
              <article key={group.group} className="skill-card">
                <div className="skill-card-head">
                  <h3>{group.group}</h3>
                  <span>{group.level}</span>
                </div>
                <div className="skill-list">
                  {group.items.map((item) => (
                    <span key={item}>{item}</span>
                  ))}
                </div>
              </article>
            ))}
          </div>
        </section>

        <section className="projects-wrap" id="projects">
          <div className="section-shell">
            <div className="section-intro">
              <p className="eyebrow">Projects</p>
              <h2>Concepts and learning work that reflect my interests.</h2>
            </div>

            <div className="project-grid">
              {projects.map((project) => (
                <article className="project-card" key={project.number}>
                  <div className="project-header">
                    <span className="project-number">{project.number}</span>
                    <span className="project-type">{project.type}</span>
                    <a href={project.github || '#'}
                      target={project.github ? '_blank' : undefined}
                      rel={project.github ? 'noreferrer' : undefined}
                      onClick={project.github ? undefined : (event) => event.preventDefault()}
                      aria-label={project.github ? `View ${project.title}` : 'Project link coming soon'}
                      className={project.github ? '' : 'muted-link'}
                    >
                      <Github size={18} />
                    </a>
                  </div>

                  <div className="project-body">
                    <h3>{project.title}</h3>
                    <p>{project.description}</p>

                    {project.architecture ? (
                      <div className="architecture-block">
                        <span className="detail-label">Architecture</span>
                        <div className="architecture-flow">
                          {project.architecture.map((step) => (
                            <span key={step}>{step}</span>
                          ))}
                        </div>
                      </div>
                    ) : null}

                    <div className="feature-list">
                      {project.features.map((feature) => (
                        <div key={feature} className="feature-item">
                          <Check size={14} />
                          <span>{feature}</span>
                        </div>
                      ))}
                    </div>

                    {project.metadata && project.metadata.length > 0 ? (
                      <div className="meta-grid">
                        {project.metadata.map((meta) => (
                          <div key={meta.label} className="mini-field">
                            <span>{meta.label}</span>
                            <strong>{meta.value}</strong>
                          </div>
                        ))}
                      </div>
                    ) : null}
                  </div>

                  <div className="project-footer">
                    <div className="tech-list">
                      {project.tech.map((tech) => (
                        <span key={tech}>{tech}</span>
                      ))}
                    </div>
                    <a className="text-link" href={project.github || '#'}
                      target={project.github ? '_blank' : undefined}
                      rel={project.github ? 'noreferrer' : undefined}
                      onClick={project.github ? undefined : (event) => event.preventDefault()}
                    >
                      {project.github ? 'GitHub' : 'Coming Soon'} <ArrowUpRight size={14} />
                    </a>
                  </div>
                </article>
              ))}
            </div>
          </div>
        </section>

        <section className="section-shell section-block" id="activities">
          <div className="section-intro">
            <p className="eyebrow">Hackathons & Technical Activities</p>
            <h2>Focused on exploring meaningful AI and problem-solving workflows.</h2>
          </div>

          <div className="activity-panel">
            <div className="panel-heading">
              <span className="panel-label">Project</span>
              <strong>AI-Based Intelligent Video Analytics Platform for Border Surveillance</strong>
            </div>

            <div className="activity-list">
              {activities.map((item, index) => (
                <div key={item} className="activity-item">
                  <span>{String(index + 1).padStart(2, '0')}</span>
                  <p>{item}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section className="section-shell section-block" id="profiles">
          <div className="section-intro">
            <p className="eyebrow">Coding & Developer Profiles</p>
            <h2>Places where I continue learning, practicing and building.</h2>
          </div>

          <div className="profiles-grid">
            {codingProfiles.map((item) => (
              <article key={item.name} className="profile-card">
                <div className="profile-icon">{item.tag}</div>
                <div>
                  <p className="profile-name">{item.name}</p>
                  <h3>{item.username}</h3>
                </div>
                <a className="button button-secondary" href={item.url} target="_blank" rel="noreferrer">{item.button}</a>
              </article>
            ))}
          </div>
        </section>

        <section className="section-shell section-block" id="education">
          <div className="section-intro">
            <p className="eyebrow">Education</p>
            <h2>Academic foundation and current learning journey.</h2>
          </div>

          <div className="education-card">
            <div className="education-header">
              <span className="education-badge">Education</span>
              <p>{education.university}</p>
            </div>

            <h3>{education.degree}</h3>
            <div className="education-meta">
              <span>{education.year}</span>
              <span>{education.semester}</span>
            </div>
            <p className="education-note">{education.notes}</p>
          </div>
        </section>

        <section className="section-shell section-block" id="certificates">
          <div className="section-intro">
            <p className="eyebrow">Certificates & Achievements</p>
            <h2>Professional growth that will be added as it happens.</h2>
          </div>

          <div className="certificate-box">
            <p>{certificates.message}</p>
            <div className="certificate-tags">
              {certificates.categories.map((tag) => (
                <span key={tag}>{tag}</span>
              ))}
            </div>
            <button type="button" className="button button-secondary">Add Certificate</button>
          </div>
        </section>

        <section className="section-shell section-block" id="resume">
          <div className="resume-card">
            <div>
              <p className="eyebrow">My Resume</p>
              <h2>Download my resume to learn more about my education, skills, projects and activities.</h2>
            </div>
            <div className="resume-actions">
              <a className="button button-primary" href={profile.resumePath} target="_blank" rel="noreferrer">Download Resume</a>
              <a className="button button-secondary" href={profile.resumePath} target="_blank" rel="noreferrer">View Resume</a>
            </div>
          </div>
        </section>

        <section className="section-shell section-block" id="contact">
          <div className="contact-layout">
            <div className="contact-copy">
              <p className="eyebrow">Contact</p>
              <h2>Let&apos;s Connect</h2>
              <p>
                I am always interested in learning, building projects, collaborating and connecting with other students and developers.
              </p>
              <div className="mini-links">
                {socialLinks.map((link) => {
                  const props = getLinkProps(link.url)
                  if (props.disabled) {
                    return (
                      <span key={link.label} className="mini-link disabled">
                        {link.label}
                      </span>
                    )
                  }

                  return (
                    <a key={link.label} className="mini-link" href={link.url} target="_blank" rel="noreferrer">
                      {link.label}
                    </a>
                  )
                })}
              </div>
            </div>

            <form className="contact-form" onSubmit={(event) => event.preventDefault()}>
              <label>
                <span>Name</span>
                <input type="text" name="name" placeholder="Your name" aria-label="Name" />
              </label>
              <label>
                <span>Email</span>
                <input type="email" name="email" placeholder={profile.email} aria-label="Email" />
              </label>
              <label>
                <span>Message</span>
                <textarea name="message" rows="5" placeholder="Write your message here..." aria-label="Message" />
              </label>
              <button type="submit" className="button button-primary">Send Message</button>
            </form>
          </div>
        </section>
      </main>

      <footer className="site-footer">
        <div className="section-shell footer-layout">
          <div>
            <h3>{profile.name}</h3>
            <p>2nd Year BTech Computer Science & Engineering Student</p>
            <p>{profile.college}</p>
          </div>

          <div className="footer-links" aria-label="Footer social links">
            {socialLinks.map((link) => (
              <a key={link.label} href={link.url || '#'} target={link.url ? '_blank' : undefined} rel={link.url ? 'noreferrer' : undefined} onClick={link.url ? undefined : (event) => event.preventDefault()}>
                {link.label}
              </a>
            ))}
          </div>
        </div>

        <div className="footer-bottom section-shell">
          <p>© 2026 {profile.name}. All rights reserved.</p>
          <p>Built with curiosity, code and continuous learning.</p>
        </div>
      </footer>
    </>
  )
}

createRoot(document.getElementById('root')).render(<App />)
"""

styles_css = """@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

:root {
  --bg: #0a1020;
  --bg-2: #111c2d;
  --surface: rgba(15, 23, 42, 0.8);
  --surface-strong: rgba(10, 16, 32, 0.96);
  --surface-soft: rgba(17, 28, 45, 0.8);
  --border: rgba(148, 163, 184, 0.2);
  --text: #eef4ff;
  --muted: #a9b7c8;
  --accent: #7dd3fc;
  --accent-strong: #67d6c7;
  --shadow: rgba(15, 23, 42, 0.35);
}

* { box-sizing: border-box; }

html { scroll-behavior: smooth; }

body {
  margin: 0;
  min-height: 100vh;
  background:
    radial-gradient(circle at top left, rgba(125, 211, 252, 0.12), transparent 22%),
    radial-gradient(circle at bottom right, rgba(103, 214, 199, 0.15), transparent 18%),
    linear-gradient(135deg, var(--bg) 0%, var(--bg-2) 100%);
  color: var(--text);
  font-family: 'Inter', sans-serif;
}

a { color: inherit; text-decoration: none; }

button, input, textarea { font: inherit; }

img { max-width: 100%; display: block; }

p, h1, h2, h3 { margin-top: 0; }

.section-shell { width: min(1180px, calc(100% - 2rem)); margin: 0 auto; }

.site-header {
  position: sticky;
  top: 0;
  z-index: 50;
  backdrop-filter: blur(18px);
  background: rgba(10, 16, 32, 0.72);
  border-bottom: 1px solid var(--border);
}

.site-header { display: flex; align-items: center; justify-content: space-between; width: 100%; padding: 1rem 0; }

.brand { display: inline-flex; align-items: center; gap: 0.75rem; font-weight: 700; letter-spacing: -0.03em; }

.brand span {
  width: 2.3rem; height: 2.3rem; display: grid; place-items: center; border-radius: 50%;
  background: linear-gradient(135deg, var(--accent), var(--accent-strong));
  color: #08111d; font-size: 0.7rem; font-weight: 800;
}

.site-nav {
  display: flex; align-items: center; gap: 1.1rem; color: var(--muted); font-size: 0.78rem; letter-spacing: 0.02em;
}

.site-nav a { position: relative; padding: 0.45rem 0.15rem; transition: color 0.2s ease; }
.site-nav a.active, .site-nav a:hover { color: var(--text); }

.nav-button, .button {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; border-radius: 999px;
  border: 1px solid var(--border); padding: 0.8rem 1.2rem; min-height: 2.8rem; font-weight: 600;
  transition: transform 0.2s ease, border-color 0.2s ease, background 0.2s ease;
}

.nav-button, .button-primary {
  background: linear-gradient(135deg, var(--accent), var(--accent-strong));
  border-color: transparent; color: #07111c;
}

.button-secondary { background: transparent; color: var(--text); }

.button:hover, .nav-button:hover { transform: translateY(-1px); }

.menu-toggle { display: none; background: transparent; border: 1px solid var(--border); color: var(--text); width: 2.6rem; height: 2.6rem; border-radius: 50%; align-items: center; justify-content: center; }

.hero {
  display: grid; grid-template-columns: 1.08fr 0.92fr; align-items: center; min-height: calc(100vh - 5rem); gap: 2.5rem; padding: 3.5rem 0 4rem;
}

.eyebrow {
  display: inline-flex; align-items: center; gap: 0.5rem; margin-bottom: 1.2rem; font-size: 0.7rem; letter-spacing: 0.12em; text-transform: uppercase; color: var(--muted);
}

.status-dot { width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--accent-strong); box-shadow: 0 0 0 0.3rem rgba(103, 214, 199, 0.18); }

h1 { font-size: clamp(2.8rem, 5vw, 5.3rem); line-height: 0.97; letter-spacing: -0.06em; margin-bottom: 1rem; max-width: 760px; }

h1 .accent-line { display: block; margin-top: 0.8rem; color: var(--accent); text-shadow: 0 0 18px rgba(125, 211, 252, 0.25); }

.hero-role { margin-bottom: 1rem; font-size: 1.2rem; color: var(--text); font-weight: 600; }
.hero-description { max-width: 53rem; color: var(--muted); line-height: 1.75; font-size: 1.02rem; }

.hero-actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 2rem; }

.social-row { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 2rem; }

.social-pill {
  display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.55rem 0.8rem; border: 1px solid var(--border); background: rgba(15, 23, 42, 0.5); border-radius: 999px; color: var(--text); font-size: 0.75rem; font-weight: 600;
}

.social-pill span {
  width: 1.6rem; height: 1.6rem; display: inline-grid; place-items: center; border-radius: 50%; background: rgba(125, 211, 252, 0.12); color: var(--accent); font-size: 0.62rem;
}

.social-pill.is-disabled { opacity: 0.6; pointer-events: none; }

.hero-art { position: relative; min-height: 30rem; display: grid; place-items: center; }

.orbit { position: absolute; border: 1px solid rgba(125, 211, 252, 0.35); border-radius: 50%; }
.orbit-one { width: 75%; height: 70%; transform: rotate(18deg); }
.orbit-two { width: 85%; height: 85%; border-color: rgba(103, 214, 199, 0.5); transform: rotate(-16deg); }
.orbit-three { width: 52%; height: 52%; border-color: rgba(255, 255, 255, 0.18); }

.art-window {
  position: relative; width: min(27rem, 82%); min-height: 19rem; border: 1px solid rgba(148, 163, 184, 0.24); background: linear-gradient(180deg, rgba(10, 16, 32, 0.8), rgba(17, 28, 45, 0.92)); border-radius: 1.4rem; box-shadow: 0 20px 60px rgba(2, 6, 23, 0.65); overflow: hidden;
}

.window-header { display: flex; gap: 0.6rem; align-items: center; padding: 0.9rem 1rem; border-bottom: 1px solid var(--border); background: rgba(15, 23, 42, 0.8); }
.dot { width: 0.72rem; height: 0.72rem; border-radius: 50%; display: inline-block; }
.dot.red { background: #fb7185; } .dot.yellow { background: #fbbf24; } .dot.green { background: #34d399; }

.window-body { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 1rem; padding: 2rem 1.5rem; color: var(--accent); }
.code-lines { display: flex; flex-direction: column; gap: 0.5rem; align-items: center; color: var(--text); font-weight: 600; font-size: 0.8rem; letter-spacing: 0.08em; text-transform: uppercase; }

.floating-tag { position: absolute; background: rgba(125, 211, 252, 0.12); border: 1px solid rgba(125, 211, 252, 0.24); color: var(--text); border-radius: 999px; padding: 0.45rem 0.8rem; font-size: 0.68rem; letter-spacing: 0.08em; text-transform: uppercase; box-shadow: 0 10px 25px rgba(2, 6, 23, 0.35); }
.tag-one { top: 10%; left: 8%; } .tag-two { bottom: 18%; right: 7%; } .tag-three { bottom: 10%; left: 17%; }

.section-block { padding: 2.5rem 0 1.5rem; }
.section-intro { margin-bottom: 2rem; }
.section-intro h2, .section-heading h2, .contact-copy h2, .resume-card h2 { font-size: clamp(2rem, 3vw, 3rem); letter-spacing: -0.055em; line-height: 1.1; margin-bottom: 0; }

.about-band { background: rgba(14, 22, 34, 0.76); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); }
.about-grid { display: grid; grid-template-columns: 0.9fr 1.1fr; gap: 2rem; padding: 3rem 0; }
.about-text { color: var(--muted); line-height: 1.8; font-size: 1.02rem; }
.about-links, .resume-actions, .footer-links { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.5rem; }
.about-links a, .text-link, .mini-link { display: inline-flex; align-items: center; gap: 0.45rem; color: var(--text); border: 1px solid var(--border); border-radius: 999px; padding: 0.7rem 0.9rem; }

.quick-grid { display: grid; grid-template-columns: repeat(7, minmax(120px, 1fr)); gap: 1rem; }
.info-card { background: rgba(15, 23, 42, 0.72); border: 1px solid var(--border); border-radius: 1rem; padding: 1.1rem 1rem; box-shadow: 0 16px 35px rgba(15, 23, 42, 0.2); }
.info-card span { display: block; color: var(--muted); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.6rem; }
.info-card strong { font-size: 0.95rem; line-height: 1.5; }

.skills-grid { display: grid; grid-template-columns: repeat(2, minmax(260px, 1fr)); gap: 1.25rem; }
.skill-card { background: rgba(15, 23, 42, 0.72); border: 1px solid var(--border); border-radius: 1.2rem; padding: 1.2rem; box-shadow: 0 18px 40px rgba(15, 23, 42, 0.2); }
.skill-card-head { display: flex; align-items: baseline; justify-content: space-between; gap: 1rem; margin-bottom: 1rem; }
.skill-card-head h3 { margin: 0; font-size: 1.15rem; }
.skill-card-head span { color: var(--accent); font-weight: 600; font-size: 0.75rem; letter-spacing: 0.08em; text-transform: uppercase; }
.skill-list { display: flex; flex-wrap: wrap; gap: 0.55rem; }
.skill-list span, .tech-list span, .certificate-tags span, .architecture-flow span { display: inline-flex; align-items: center; justify-content: center; border-radius: 999px; padding: 0.45rem 0.8rem; background: rgba(125, 211, 252, 0.08); border: 1px solid rgba(125, 211, 252, 0.18); color: var(--text); font-size: 0.7rem; font-weight: 600; }

.projects-wrap { padding: 2.8rem 0 1.2rem; background: rgba(8, 13, 24, 0.7); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); }
.project-grid { display: grid; grid-template-columns: repeat(3, minmax(260px, 1fr)); gap: 1.25rem; }
.project-card { display: flex; flex-direction: column; background: rgba(15, 23, 42, 0.75); border: 1px solid var(--border); border-radius: 1.3rem; overflow: hidden; box-shadow: 0 20px 50px rgba(15, 23, 42, 0.2); }
.project-header { display: flex; align-items: center; justify-content: space-between; gap: 0.75rem; padding: 1.1rem 1.1rem 0.8rem; }
.project-number { font-size: 0.7rem; letter-spacing: 0.12em; text-transform: uppercase; color: var(--muted); }
.project-type { color: var(--accent); font-size: 0.7rem; letter-spacing: 0.04em; text-transform: uppercase; margin-left: auto; }
.muted-link { opacity: 0.5; }
.project-body { padding: 0 1.1rem 1rem; }
.project-body h3 { margin-bottom: 0.8rem; font-size: 1.3rem; line-height: 1.35; }
.project-body p { color: var(--muted); line-height: 1.72; }
.architecture-block { margin-top: 1rem; }
.detail-label { display: inline-block; margin-bottom: 0.6rem; color: var(--accent); font-size: 0.68rem; letter-spacing: 0.08em; text-transform: uppercase; }
.architecture-flow { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.feature-list { display: grid; gap: 0.65rem; margin-top: 1rem; }
.feature-item { display: flex; align-items: flex-start; gap: 0.55rem; color: var(--text); line-height: 1.6; }
.feature-item svg { color: var(--accent-strong); margin-top: 0.18rem; flex-shrink: 0; }
.meta-grid { display: grid; gap: 0.75rem; margin-top: 1rem; }
.mini-field { display: grid; gap: 0.2rem; padding: 0.7rem 0.8rem; border: 1px solid var(--border); border-radius: 0.8rem; background: rgba(9, 14, 24, 0.45); }
.mini-field span { color: var(--muted); font-size: 0.68rem; letter-spacing: 0.05em; text-transform: uppercase; }
.mini-field strong { font-size: 0.9rem; }
.project-footer { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 0.8rem; padding: 1rem 1.1rem 1.2rem; border-top: 1px solid var(--border); margin-top: auto; }
.text-link { background: rgba(125, 211, 252, 0.06); }

.activity-panel { background: linear-gradient(135deg, rgba(15, 23, 42, 0.9), rgba(17, 28, 45, 0.7)); border: 1px solid var(--border); border-radius: 1.5rem; padding: 1.4rem; }
.panel-heading { display: flex; flex-wrap: wrap; align-items: center; gap: 0.8rem; margin-bottom: 1.4rem; }
.panel-label { color: var(--muted); font-size: 0.7rem; letter-spacing: 0.08em; text-transform: uppercase; }
.panel-heading strong { font-size: 1.1rem; }
.activity-list { display: grid; grid-template-columns: repeat(2, minmax(220px, 1fr)); gap: 0.8rem 1rem; }
.activity-item { display: flex; gap: 0.8rem; align-items: flex-start; padding: 0.9rem 1rem; background: rgba(8, 13, 24, 0.5); border: 1px solid var(--border); border-radius: 0.9rem; }
.activity-item span { display: inline-flex; width: 2.1rem; height: 2.1rem; border-radius: 50%; color: var(--accent); background: rgba(125, 211, 252, 0.08); align-items: center; justify-content: center; font-size: 0.7rem; font-weight: 700; }
.activity-item p { margin: 0; color: var(--text); line-height: 1.5; }

.profiles-grid { display: grid; grid-template-columns: repeat(3, minmax(220px, 1fr)); gap: 1rem; }
.profile-card { display: flex; flex-direction: column; gap: 1rem; background: rgba(15, 23, 42, 0.72); border: 1px solid var(--border); border-radius: 1.2rem; padding: 1.2rem; }
.profile-icon { width: 3rem; height: 3rem; border-radius: 0.9rem; display: grid; place-items: center; background: rgba(125, 211, 252, 0.08); color: var(--accent); border: 1px solid rgba(125, 211, 252, 0.18); font-weight: 800; }
.profile-name { margin-bottom: 0.35rem; color: var(--muted); letter-spacing: 0.08em; text-transform: uppercase; font-size: 0.68rem; }
.profile-card h3 { margin: 0; font-size: 1.15rem; }

.education-card { background: rgba(15, 23, 42, 0.72); border: 1px solid var(--border); border-radius: 1.3rem; padding: 1.4rem; }
.education-header { display: flex; align-items: center; justify-content: space-between; gap: 1rem; margin-bottom: 0.9rem; }
.education-badge { display: inline-flex; align-items: center; padding: 0.5rem 0.7rem; border-radius: 999px; background: rgba(103, 214, 199, 0.1); border: 1px solid rgba(103, 214, 199, 0.2); color: var(--accent-strong); font-size: 0.7rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; }
.education-header p { margin: 0; color: var(--muted); }
.education-card h3 { margin-bottom: 1.1rem; font-size: clamp(1.5rem, 2vw, 2.2rem); }
.education-meta { display: flex; flex-wrap: wrap; gap: 0.7rem; margin-bottom: 0.8rem; }
.education-meta span { display: inline-flex; padding: 0.45rem 0.7rem; border-radius: 999px; background: rgba(125, 211, 252, 0.08); border: 1px solid rgba(125, 211, 252, 0.18); color: var(--text); font-size: 0.72rem; font-weight: 600; }
.education-note { color: var(--muted); line-height: 1.7; }

.certificate-box, .resume-card, .contact-form { background: rgba(15, 23, 42, 0.72); border: 1px solid var(--border); border-radius: 1.2rem; padding: 1.4rem; }
.certificate-box p { color: var(--muted); line-height: 1.7; margin-bottom: 1rem; }
.certificate-tags { display: flex; flex-wrap: wrap; gap: 0.6rem; margin-bottom: 1rem; }
.resume-card { display: flex; align-items: center; justify-content: space-between; gap: 1.5rem; }
.resume-card h2 { max-width: 640px; margin-bottom: 0; }

.contact-layout { display: grid; grid-template-columns: 0.92fr 1.08fr; gap: 1.5rem; align-items: start; }
.contact-copy p { color: var(--muted); line-height: 1.8; }
.mini-links { display: flex; flex-wrap: wrap; gap: 0.7rem; margin-top: 1.3rem; }
.mini-link.disabled { opacity: 0.65; pointer-events: none; }
.contact-form { display: grid; gap: 1rem; }
.contact-form label { display: grid; gap: 0.45rem; color: var(--text); font-weight: 600; }
.contact-form input, .contact-form textarea { width: 100%; background: rgba(9, 14, 24, 0.6); border: 1px solid var(--border); border-radius: 0.9rem; padding: 0.9rem 1rem; color: var(--text); }
.contact-form input::placeholder, .contact-form textarea::placeholder { color: rgba(169, 183, 200, 0.8); }
.contact-form textarea { resize: vertical; min-height: 140px; }

.site-footer { margin-top: 2.5rem; background: rgba(10, 16, 32, 0.9); border-top: 1px solid var(--border); }
.footer-layout { display: flex; justify-content: space-between; gap: 1rem; padding: 2rem 0 1rem; }
.footer-layout h3 { margin-bottom: 0.5rem; font-size: 1.1rem; }
.footer-layout p { margin: 0; color: var(--muted); line-height: 1.7; }
.footer-links { align-items: center; margin-top: 0; }
.footer-links a { color: var(--text); border: 1px solid var(--border); border-radius: 999px; padding: 0.5rem 0.8rem; }
.footer-bottom { display: flex; justify-content: space-between; gap: 1rem; padding: 0 0 1.4rem; color: var(--muted); font-size: 0.85rem; }

@media (max-width: 1024px) {
  .hero, .about-grid, .contact-layout, .resume-card { grid-template-columns: 1fr; }
  .resume-card { display: grid; }
  .quick-grid { grid-template-columns: repeat(3, minmax(120px, 1fr)); }
  .project-grid { grid-template-columns: repeat(2, minmax(260px, 1fr)); }
}

@media (max-width: 760px) {
  .site-nav { position: absolute; top: 100%; right: 0; width: min(100%, 18rem); display: none; flex-direction: column; align-items: flex-start; background: rgba(10, 16, 32, 0.95); border: 1px solid var(--border); border-radius: 1rem; padding: 1rem; box-shadow: 0 25px 60px rgba(2, 6, 23, 0.5); }
  .site-nav.open { display: flex; }
  .menu-toggle { display: inline-flex; }
  .nav-button { width: 100%; }
  .hero { padding-top: 2.3rem; min-height: auto; }
  .hero-actions, .resume-actions, .about-links, .footer-layout, .footer-bottom { flex-direction: column; align-items: flex-start; }
  .skills-grid, .project-grid, .profiles-grid, .activity-list, .quick-grid { grid-template-columns: 1fr; }
  .contact-layout, .about-grid { display: grid; grid-template-columns: 1fr; }
}

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after { animation: none !important; transition: none !important; }
}
"""

index_html = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="theme-color" content="#0a1020" />
    <meta name="description" content="Portfolio of P Yashwanth, a 2nd year BTech Computer Science and Engineering student at REVA University interested in Python, Artificial Intelligence, Machine Learning, software development and problem solving." />
    <meta property="og:title" content="P Yashwanth | BTech CSE Student | AI & Machine Learning" />
    <meta property="og:description" content="Portfolio of P Yashwanth, a 2nd year BTech Computer Science and Engineering student at REVA University interested in Python, Artificial Intelligence, Machine Learning, software development and problem solving." />
    <meta property="og:type" content="website" />
    <meta property="og:image" content="/favicon.svg" />
    <title>P Yashwanth | BTech CSE Student | AI & Machine Learning</title>
    <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
"""

favicon_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="P Yashwanth favicon">
  <defs>
    <linearGradient id="bg" x1="0%" x2="100%" y1="0%" y2="100%">
      <stop offset="0%" stop-color="#7dd3fc" />
      <stop offset="100%" stop-color="#67d6c7" />
    </linearGradient>
  </defs>
  <rect width="64" height="64" rx="18" fill="#0a1020" />
  <rect x="8" y="8" width="48" height="48" rx="14" fill="url(#bg)" opacity="0.15"/>
  <text x="32" y="39" text-anchor="middle" font-size="28" font-weight="800" font-family="Arial, sans-serif" fill="#eaf6ff">PY</text>
</svg>
"""

resume_pdf = b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>\nendobj\n4 0 obj\n<< /Length 116 >>\nstream\nBT\n/F1 18 Tf\n72 720 Td\n(P Yashwanth Resume Placeholder) Tj\n0 -30 Td\n/F1 12 Tf\n(Pending update with final resume details.) Tj\nET\nendstream\nendobj\n5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\nxref\n0 6\n0000000000 65535 f \n0000000010 00000 n \n0000000062 00000 n \n0000000123 00000 n \n0000000247 00000 n \n0000000119 00000 n \ntrailer\n<< /Root 1 0 R /Size 6 >>\nstartxref\n?\n%%EOF\n"

(root / 'src' / 'data' / 'portfolio.js').write_text(portfolio_js, encoding='utf-8')
(root / 'src' / 'main.jsx').write_text(main_js, encoding='utf-8')
(root / 'src' / 'styles.css').write_text(styles_css, encoding='utf-8')
(root / 'index.html').write_text(index_html, encoding='utf-8')
(root / 'public' / 'favicon.svg').write_text(favicon_svg, encoding='utf-8')
(root / 'public' / 'resume' / 'P_Yashwanth_Resume.pdf').write_bytes(resume_pdf)

print('Portfolio generated successfully.')
