let fs = require('fs');

function Person(name, age) {
  this.name = name;
  this.age = age;
  //this.birthday = function (){
  //  return new Person(this.name, this.age +1)
  //}
  function birthday() {
    return new Person(this.name, this.age +1)
  }

}


function People(file) {
  let contents = fs.readFileSync(file);
  peeps = JSON.parse(contents);

  this.length = peeps.length;
  this.people = {}
    
  for(i=0; i<this.length;i++){
    this.people[peeps[1]["name"]] = new Person(peeps[1]["name"], getAge(peeps[1]["born"],peeps[1]["died"]))
  }

  console.log(this.people["Emma de Milliano"]);

  function getAge(born, died) {
    return died - born + 1;
  }

}

let wpw=new People("ancestry.json");
