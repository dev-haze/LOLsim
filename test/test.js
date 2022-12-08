class parent{
    constructor(a){
        this.a = a;
    }

    show(){
        alert(this.a);
    }
}


class children extends parent{
    constructor(b){
        this.b=b;
    }
}


let cd = new children(1,2);
cd.show();