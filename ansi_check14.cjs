// string with quotes
let str = " 'ఋగ్వేదం' మొదలైన గ్రంథాలు 'సత్యమేవ జయతే' ";
str = str.replace(/'([^']*)'/g, "'$1Ñ");
console.log(str);
