document.addEventListener('DOMContentLoaded', async () => {
    try {
        // 1. PERF: Fetch local JSON to avoid network latency (0ms RTT)
        const response = await fetch('assets/quotes.json');
        const quotes = await response.json();

        // 2. Select pseudo-random quote
        const randomIndex = Math.floor(Math.random() * quotes.length);
        const selectedQuote = quotes[randomIndex];

        // 3. Update the DOM aka DOM Injection
        const quoteEl = document.getElementById('quote');
        const authorEl = document.getElementById('author');

        quoteEl.textContent = `"${selectedQuote.text}"`;
        authorEl.textContent = `— ${selectedQuote.author}`;

        // 4. UX: Use rAF to ensure fade-in occurs in the next paint frame
        requestAnimationFrame(() => {
            quoteEl.classList.add('visible');
            authorEl.classList.add('visible');
        });

    } catch (error) {
      // Fallback for filesystem errors
        console.error('Failed to load wisdom:', error);
        document.getElementById('quote').textContent = "Focus on the present.";
    }
}); 