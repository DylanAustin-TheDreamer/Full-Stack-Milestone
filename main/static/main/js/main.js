const navbar = document.getElementById('navbar');
const dropdown = document.getElementById('dropdown');
const mobileCarousel = document.getElementById('mobileCarousel');
const carouselSection = document.getElementById('carouselSection');
// Toggle navbar visibility on dropdown click
dropdown.addEventListener('click', () => {
    navbar.style.display = navbar.style.display === 'block' ? 'none' : 'block';
});
// Hide navbar when clicking outside
document.addEventListener('click', (event) => {
    if (!dropdown.contains(event.target) && !navbar.contains(event.target)) {
        navbar.style.display = 'none';
    }
});


