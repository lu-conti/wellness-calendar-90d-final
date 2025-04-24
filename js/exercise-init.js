// Update exercise.html to use the exercise-toggle.js script
document.addEventListener('DOMContentLoaded', function() {
    // Add script reference to exercise.html
    const script = document.createElement('script');
    script.src = 'js/exercise-toggle.js';
    document.head.appendChild(script);
});
