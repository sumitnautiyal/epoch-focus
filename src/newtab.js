document.addEventListener('DOMContentLoaded', async () => {
    try {
        // 1. Fetch the local database
        const response = await fetch('assets/quotes.json');
        const quotes = await response.json();

        // 2. Pick a random quote
        const randomIndex = Math.floor(Math.random() * quotes.length);
        const selectedQuote = quotes[randomIndex];

        // 3. Update the DOM
        const quoteEl = document.getElementById('quote');
        const authorEl = document.getElementById('author');

        quoteEl.textContent = `"${selectedQuote.text}"`;
        authorEl.textContent = `— ${selectedQuote.author}`;

        // 4. Trigger the fade-in animation
        requestAnimationFrame(() => {
            quoteEl.classList.add('visible');
            authorEl.classList.add('visible');
        });

    } catch (error) {
        console.error('Failed to load wisdom:', error);
        document.getElementById('quote').textContent = "Focus on the present.";
    }
}); 