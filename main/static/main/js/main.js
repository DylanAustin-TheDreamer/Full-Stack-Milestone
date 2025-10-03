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

// Modal Message Functions
function closeMessageModal() {
    const modal = document.getElementById('messageModal');
    if (modal) {
        modal.style.animation = 'fadeOut 0.3s ease-out';
        setTimeout(() => {
            modal.remove();
        }, 300);
    }
}

// Auto-close modal after 5 seconds (optional)
document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('messageModal');
    if (modal) {
        // Auto-close after 5 seconds
        setTimeout(() => {
            closeMessageModal();
        }, 5000);
        
        // Close on outside click
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                closeMessageModal();
            }
        });
        
        // Close on Escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                closeMessageModal();
            }
        });
    }
});

// Add fadeOut animation to CSS if not already present
if (!document.styleSheets[0].cssRules.toString().includes('fadeOut')) {
    const style = document.createElement('style');
    style.textContent = `
        @keyframes fadeOut {
            from { opacity: 1; }
            to { opacity: 0; }
        }
    `;
    document.head.appendChild(style);
}


