const quotes = [
  {
    author: 'Confucius',
    quote: 'FP Pudge — such an act gives out internal beauty and tendency to independence. Independence from public opinion, from desire to win, from stereotypes about game. FP Pudge — it is depths of personality and beauty',
  },
  {
    author: 'Sun Tzu',
    quote: 'Those who play without wards always have sharp mind. They study to think as an enemy, they begin to see in the fog. 75 gold for Sentry Ward could become one branch, from this branch will grow sticks, due to the sticks at the turning point a support will alive',
  },
  {
    author: 'Laozi',
    quote: 'That one wins who is always grows. Legion, Pudge, Slark, Underlord, Silencer',
  },
  {
    author: 'Bushido',
    quote: 'Dishonor does not threaten that one, who is not visible for enemies. Shadow amulet — the cheapest source of invisibility',
  },
  {
    author: 'Machiavelli',
    quote: 'Only cunning  could get the best in some battles',
  },
  {
    author: 'The Art of War',
    quote: 'When the enemy is superior to you, mislead him. Send a message “FF we afk finish”. When enemy will relax, attack him',
  },
  {
    author: 'Buddha',
    quote: 'Get rid of addictions to your property. If a game goes not as in plan, then break your items. You will lose a battle, but not the war',
  },
  {
    author: 'Seneca the Younger',
    quote: '“?”,”ez”, “)))” are the instruments of moral pressure. Enemy without moral is a pathetic show',
  },
];

const randQuote = () => quotes[Math.floor(Math.random() * quotes.length)];

export default randQuote;
