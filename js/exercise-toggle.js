// Simple script for exercise location toggle
document.addEventListener('DOMContentLoaded', function() {
    const locationToggle = document.getElementById('location-toggle');
    const homeWorkouts = document.querySelectorAll('.home-workout');
    const gymWorkouts = document.querySelectorAll('.gym-workout');
    
    // Load saved preference
    const savedLocation = localStorage.getItem('exerciseLocation') || 'home';
    locationToggle.value = savedLocation;
    
    // Show appropriate workouts based on saved preference
    if (savedLocation === 'home') {
        homeWorkouts.forEach(workout => workout.style.display = 'block');
        gymWorkouts.forEach(workout => workout.style.display = 'none');
    } else {
        homeWorkouts.forEach(workout => workout.style.display = 'none');
        gymWorkouts.forEach(workout => workout.style.display = 'block');
    }
    
    // Toggle between home and gym workouts
    locationToggle.addEventListener('change', function() {
        const location = this.value;
        localStorage.setItem('exerciseLocation', location);
        
        if (location === 'home') {
            homeWorkouts.forEach(workout => workout.style.display = 'block');
            gymWorkouts.forEach(workout => workout.style.display = 'none');
        } else {
            homeWorkouts.forEach(workout => workout.style.display = 'none');
            gymWorkouts.forEach(workout => workout.style.display = 'block');
        }
    });
});
