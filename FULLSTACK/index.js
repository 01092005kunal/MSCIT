// const obj = {
//     name: "John Doe",
//     age: 30,
// }

// console.log(obj)
// const objTemp = obj


// obj.name = "Jane Doe"
// obj.age = 25
// delete obj.name 


// console.log(obj)
// console.log(obj == objTemp )
// console.log(objTemp)


// console.log(0.1 + 0.2 === 0.3)
// console.log(0.1 + 0.2)

// console.log(0.3)

const address= {
        street: "123 Main St",
        city: "Anytown",
        country: "USA"
    }

const person1 = { 
    name: "John Doe",
    age: 30,
    address
}

const person2 = { 
    name: "alex Doe",
    age: 31,
    
}


const {age, name, address: {...addressRest}} = person1
const {age: age2, name: name2} = person2



console.log(person1)
console.log(name2 , age2,)
