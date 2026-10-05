export const navItems = [
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
  resumePath: `${import.meta.env.BASE_URL}resume/P_Yashwanth_Resume.pdf`,
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
