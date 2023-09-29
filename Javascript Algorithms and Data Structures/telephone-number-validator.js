function telephoneCheck(str) {
  // There's probably a simpler regex I could use but this is what I came up with
  return /^1?\s?(\((?=\d{3}\)))?(\d{3})((?<=\(\d{3})\))?-?\s?(\d{3})-?\s?(\d{4})$/.test(str);
}

console.log(telephoneCheck("(555)-555-5555"));
