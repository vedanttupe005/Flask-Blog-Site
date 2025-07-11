# 📝 Personal Blog Website (Flask + Bootstrap + Npoint API)

This is a personal blog website built using **Flask**, **HTML**, **CSS**, and **Bootstrap**, with dynamic blog post content fetched from an external **Npoint JSON API**. The site features a home page listing blog posts, a responsive navigation bar, an about section, a sample post view, and a contact form that can send emails. The footer also contains a link to my GitHub profile.

---

## 🚀 Features

- 📰 **Dynamic blog posts** loaded from a [Npoint](https://www.npoint.io/) JSON API
- 📱 Responsive layout using Bootstrap
- 🔗 Navbar with:
  - Home
  - About
  - Sample Post
  - Contact
- 📧 Contact form using `POST` request to send emails
- 🔗 Footer with a GitHub profile link
- 💬 Clean and modern user interface

---

## 🔧 Technologies Used

- Python 3.x
- Flask
- HTML5, CSS3
- Bootstrap 4/5
- [Npoint.io](https://www.npoint.io/) (for JSON-based blog posts)
- Flask-Mail or SMTP (for sending emails)

---

## 📂 Project Structure

project/
│
├── static/
│ ├── css/
│ └── images/
│
├── templates/
│ ├── header.html # Reusable header/navigation bar
│ ├── footer.html # Reusable footer
│ ├── layout.html # Base template (optional)
│ ├── index.html # Home page with blog list
│ ├── about.html
│ ├── contact.html
│ ├── post.html # Individual blog post view
│
├── main.py
├── requirements.txt
└── README.md
