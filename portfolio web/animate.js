document.addEventListener('DOMContentLoaded', function() {
    const reviewsWrapper = document.querySelector('.reviews-wrapper');
    
    // Clone the reviews to create an infinite scroll effect
    const reviews = reviewsWrapper.innerHTML;
    reviewsWrapper.innerHTML += reviews;
    
    // Adjust the animation duration based on the total width of the reviews
    const totalWidth = Array.from(reviewsWrapper.children).reduce((total, review) => total + review.offsetWidth, 0);
    reviewsWrapper.style.animationDuration = `${totalWidth / 100}px`; // Adjust as necessary
});
