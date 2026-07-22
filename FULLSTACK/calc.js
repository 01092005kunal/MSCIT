
function calculatePrice(n, taxiprices) {
  if (n < 0) {
    throw new Error("Trip distance cannot be negative.");
  } 
//   n = tripDistance


  const sortedprices = [...taxiprices].sort((a, b) => a.lower - b.lower);

  let totalPrice = 0;
  let remaining = n;

  for (const { lower, upper, pricePerKm } of sortedprices) {
    if (remaining <= 0) break;

    let slabSpanAvailable;
    if (upper === null) {
      slabSpanAvailable = remaining;
    } else {
      slabSpanAvailable = Math.min(upper - lower, remaining);
    }

    if (slabSpanAvailable <= 0) continue;

    totalPrice += slabSpanAvailable * pricePerKm;
    remaining -= slabSpanAvailable;
  }

  if (remaining > 0) {
    throw new Error(
      `Taxi prices do not cover the full trip distance (missing coverage for the last ${remaining} km).`
    );
  }

  return totalPrice;
}


const tripDistance = 7;

const taxiprices = [
  { lower: 0, upper: 5, pricePerKm: 10 },    
  { lower: 5, upper: 10, pricePerKm: 6 },    
  { lower: 10, upper: null, pricePerKm: 4 }, 
];


const price = calculatePrice(tripDistance, taxiprices);
console.log("Taxi prices:", taxiprices);
console.log(`Trip distance: ${tripDistance} km`);
console.log(`Total price: ₹${price}`);

