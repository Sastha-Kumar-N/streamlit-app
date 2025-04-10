// Function to scroll to the lectures section
function scrollToLectures() {
    document.getElementById('lectures').scrollIntoView({ behavior: 'smooth' });
}

// Dark Mode Toggle
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

themeToggle.addEventListener('click', () => {
    body.classList.toggle('light-mode');
    themeToggle.textContent = body.classList.contains('light-mode') ? '🌙' : '☀️';
});

// Check for user's preferred color scheme on load
if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
    body.classList.add('light-mode');
    themeToggle.textContent = '🌙';
}