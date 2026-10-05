import { useEffect, useState } from 'react'
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
          <a className="nav-button" href={profile.resumePath} download="P_Yashwanth_Resume.pdf">
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
              <a className="button button-secondary" href={profile.resumePath} download="P_Yashwanth_Resume.pdf">Download Resume</a>
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
              <a className="button button-primary" href={profile.resumePath} download="P_Yashwanth_Resume.pdf">Download Resume</a>
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
