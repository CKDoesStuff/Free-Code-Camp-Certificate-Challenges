function rot13(str) {
  // Make reusable rotator for later
  const rot = (letter) => letter.charCodeAt() - 13;

  return [...str]
    .map(letter =>
      /\W|_/.test(letter) // Ignore spaces and punctuation
        ? letter
        : rot(letter) >= 'A'.charCodeAt() // If we get below 'A' add 26
          ? String.fromCharCode(rot(letter)) // to continue circling back from 'Z'
          : String.fromCharCode(rot(letter) + 26)
    ).join('');
}

console.log(rot13("SERR PBQR PNZC"));
