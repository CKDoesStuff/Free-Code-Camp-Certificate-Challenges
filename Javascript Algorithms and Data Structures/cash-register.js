const US_CURRENCY = {
  'ONE HUNDRED': 100,
  'TWENTY': 20,
  'TEN': 10,
  'FIVE': 5,
  'ONE': 1,
  'QUARTER': 0.25,
  'DIME': 0.1,
  'NICKEL': 0.05,
  'PENNY': 0.01
};

Object.freeze(US_CURRENCY); // Do NOT touch my money values >:(

function checkCashRegister(price, cash, cid) {
  const Status_Msg = {CL: 'CLOSED', OP: 'OPEN', INSF: 'INSUFFICIENT_FUNDS'}
  const cashCache = [...cid].reverse();
  const objOut = { status: '', change: [] }
  let change = (cash - price) * 100; // Making things easier on myself by dealing with floating point errors early
  
  cashCache.forEach(item => { // Each item is a sub-array formatted ['MONEY_TYPE', numberValue]
    const moneyVal = US_CURRENCY[item[0]] * 100; // Pull base value of money type from currency object using 1st sub-array value
    item[1] = item[1] * 100; // Adjust the number value of sub-array to fix floating point
    let changeOut = 0;

    while (change - moneyVal >= 0 && item[1] - moneyVal >= 0) { // Iterate until either till runs out or subtracting 
      change = change - moneyVal;                               // value of current money type would make change val negative
      item[1] -= moneyVal;                                      // (i.e give too much change)
      changeOut += moneyVal;
    }
    objOut.change.push([item[0], changeOut / 100]) // Push final value to output object
  });

  objOut.status = cashCache.every(item => item[1] === 0) // Determine if till should be closed or not
    ? Status_Msg.CL : Status_Msg.OP; 

  objOut.change = objOut.change // Sort by highest calue if till is still open, or return original array if till is closed
    .filter(item => objOut.status == 'OPEN' ? item[1] : item) 
    .sort((a, b) => objOut.status == 'OPEN' ? (a[1] > b[1] ? -1 : 1) : -1);

  return change > 0 // If change isn't zero then we didn't have enough in our till so we return a fail state of infsufficient funds
    ? { status: Status_Msg.INSF, change: [] }
    : objOut;
}
console.log(
checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]));
