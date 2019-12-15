function Person(name, age) {
  this.name = name;
  this.age = age;
  this.birthday = function (){
      return new Person(this.name, this.age +1)
  }

}

let bob=new Person("bob", 42);
console.log(bob.name)
let newbob = bob.birthday();
console.log(newbob.age)