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