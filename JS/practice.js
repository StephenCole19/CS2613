class Expr{

    constructor(fn, x, y){
        this.fn = fn;
        this.x = x;
        this.y = y;
    }

    eval(){
        if(this.fn === "x"){
            return (this.x * this.y);
        }
        else {
            return (this.x + this.y);
        }
    }
}

let six_plus_nine = new Expr('+', 6, 9);

//console.log(six_plus_nine.eval());

function join(arr) {
    var r = "";
    if(arr.length === 1){
        r = r + arr[1];
    } else {
        for(var i=0;i < arr.length;i++){
            r += arr[i];
        }
    }
    return r;
}

console.log(join(["a","b","c"]));