Personal Portfolio Website

This is a simple and responsive portfolio site I built using HTML, CSS, and JavaScript. It's designed to showcase my projects, skills, and provide a place for people to get in touch. I wanted something lightweight, easy to customize, and professional without being overdone.

Features
Responsive layout that works across all screen sizes

Clean, modern UI with smooth transitions

Dynamically loads project data using JavaScript

Contact form with basic validation

Skills section organized by category

Minimal dependencies and SEO-friendly markup

File Overview
portfolio/
├── index.html       - Main HTML file
├── styles.css       - CSS styling
├── script.js        - JS for functionality
└── README.md        - This file

Getting Started
Clone or download this repository

Open index.html in your browser

Customize the content (see below)

Deploy using your preferred hosting (GitHub Pages, Netlify, Vercel, etc.)

Customizing the Site
Personal Info (index.html)
Update the hero section with your name and title:

<h1 class="hero-title">Hi, I'm <span class="highlight">Your Name</span></h1>
<h2 class="hero-subtitle">Web Developer</h2>

Edit the about section, email, and social links to reflect your info.

Projects (script.js)
Projects are loaded from an array in the script file:

const projects = [
  {
    title: "Project Name",
    description: "Brief project description.",
    technologies: ["JavaScript", "Node.js", "MongoDB"],
    liveUrl: "https://yourproject.com",
    githubUrl: "https://github.com/yourusername/project"
  },
  // Add more as needed
];

Skills (index.html)
Each skill uses an icon and a label. You can modify or add new ones:

<div class="skill-item">
  <i class="fab fa-react"></i>
  <span>React</span>
</div>

Styling (styles.css)
You can change the colors and other styles here. Start with the CSS variables:

:root {
  --primary-color: #2563eb;
  --secondary-color: #fbbf24;
  --text-color: #333;
  --background-color: #ffffff;
}

Sections
Hero: Intro with name, title, and buttons

About: Short bio and background

Projects: Dynamically loaded cards with tech stack and links

Skills: Icons grouped by category

Contact: Email, links, and a functional contact form

Performance Notes
CSS transitions and light animations

Lazy loading for project data

Font Awesome used instead of images

Minimal dependencies (only Font Awesome and Google Fonts)



Acknowledgments
Font Awesome for the icons

Google Fonts (Inter) for typography

