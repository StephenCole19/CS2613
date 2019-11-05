function flatten(arr) {
    var value = [];

    if(Array.isArray(arr[0])){
        if(arr.length == 1){
            return flatten(arr[0]);
        }

        return flatten(arr.shift()).concat(flatten(arr));
    } else{
        if(arr.length == 1 || arr.length == 0){
            return arr;
        }
        value.push(arr.shift());
        return value.concat(flatten(arr));
    }
}

let fs = require('fs');

function read_json_file(filename) {
    let contents = fs.readFileSync(filename);

    return JSON.parse(contents);
}

//exports.read_json_file=read_json_file;


function summerize_mail(jsonFile, key1, key2){
    var jsonArr = flatten(read_json_file(jsonFile));
    var arr = [];

    if(key1 == undefined){
        return Array(jsonArr.length).fill({});
    }

    if(arguments.length == 2){
        for(var i=0; i < jsonArr.length;i++){
            var container = {Subject: ""};
            var obj = jsonArr[i]
            container[key1] = obj.headers[key1];
            arr.push(container);
        }
    
        return arr;
    } else {
        for(var i=0; i < jsonArr.length;i++){
            var container = {Subject: "", Date: ""};
            var obj = jsonArr[i]
            container[key1] = obj.headers[key1];
            container[key2] = obj.headers[key2];
            arr.push(container);
        }
    
        return arr;
    }
}

class Message {
    constructor(obj) {
        this.Subject = obj.headers.Subject;
        this.Date = obj.headers.Date;
    }

    equals(obj2){
        if(this.Subject === obj2.Subject && this.Date === obj2.Date){
            return true;
        }
        return false;
    }

}

exports.Message = Message;
exports.summerize_mail = summerize_mail;
exports.flatten = flatten;
exports.read_json_file = read_json_file;