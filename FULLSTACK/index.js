const obj = {
    name: "John Doe",
    age: 30,
}

console.log(obj)
const objTemp = obj


obj.name = "Jane Doe"
obj.age = 25
delete obj.name 


console.log(obj)
console.log(obj == objTemp )
console.log(objTemp)


console.log(0.1 + 0.2 === 0.3)
console.log(0.1 + 0.2)

console.log(0.3)