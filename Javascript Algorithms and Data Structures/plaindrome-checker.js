function palindrome(str) {
  // Remove special chars and standardize case
  str = str.replace(/_*\s*\W*/g, '').toLowerCase();

  // Initialize check var and iterate str in reverse to set
  let chkStr = '';
  for (let i = str.length - 1; i >= 0; i--) {
    chkStr += str[i];
  }

  // Check palindrome
  return str == chkStr
  console.log(chkStr, str)
}

palindrome("eye");
