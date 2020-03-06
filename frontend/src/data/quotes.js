const quotes = [
  {
    author: 'Confucius',
    quote: 'FP Pudge — such an act gives out internal beauty and tendency to independence. Independence from public opinion, from desire to win, from stereotypes about game. FP Pudge — it is depths of personality and beauty',
  },
  {
    author: 'Confucius',
    quote: 'FP Pudge — such an act gives out internal beauty and tendency to independence. Independence from public opinion, from desire to win, from stereotypes about game. FP Pudge — it is depths of personality and beauty',
  },
];

const randQuote = () => quotes[Math.floor(Math.random() * quotes.length)];

export default randQuote;
