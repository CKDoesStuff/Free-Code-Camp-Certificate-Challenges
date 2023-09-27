function convertToRoman(num) {
  const ROMAN_NUMERALS = {
    M: 1000, 
    CM: 900,
    D: 500,
    CD: 400,
    C: 100,
    XC: 90,
    L: 50,
    XL: 40,
    X: 10,
    IX: 9,
    V: 5,
    IV: 4,
    I: 1
    };
  let names = Object.keys(ROMAN_NUMERALS);
  let numeralOut = '';
  
  // Internal function to break off factors in valid intervals
  const findFactor = (_num, numeral) => {
    while (_num > 0) {
    if ( _num - ROMAN_NUMERALS[numeral] >= 0 ) { 
        numeralOut += parseFactor(ROMAN_NUMERALS[numeral]); 
        _num -= ROMAN_NUMERALS[numeral];
        num = _num;
      } else {
        _num = 0;
      }
    }
  }
  // Internal function to parse integer factors into roman numerals
  const parseFactor = (_num) => {
    let parseOut = '';
    for (let i = 0; i < names.length; i++) {
      if (_num == ROMAN_NUMERALS[names[i]]) { 
        parseOut = names[i]; 
      }
    }
    return parseOut;
  }
  
  // Iterate numerals through factorizer and parser from largest to smallest value
  for (let i = 0; i < names.length; i++) {
    findFactor(num, names[i]);
  }
  
  return numeralOut;
}

console.log(convertToRoman(2000));
