function directFollows(str, a){
    let length = str.length;
    for (let i = 0; i + 1 < length; i += 1) {
        // foreach caractere and its sucessor, add a tuple to the array
        a.push([str[i], str[i+1]]);
    }
}

function iterateTraces(L) {
    // start the return with an empty array
    let a = [];
    
    for (let l in L) {
        //iterate the trace to get the DF
        directFollows(L[l], a);
    }
    // only unique tuples
    return [... new Set(a)]; 
}

function join(df) {
    let map = {};
    for (let t in df) {
        let tuple = df[t];
        let input = tuple[0];
        let output = tuple[1];
            
        if (!Object.keys(map).includes(input)) {
            map[input] = [output];
        } else if (!map[input].includes(output)) {
            map[input].push(output);
        }
    }
    return map;
}

let L = [
    'abcde',
    'acde',
    'acbde'
];

let DF = iterateTraces(L);
let selected = join(DF);

console.log(selected);

/**
a: ['b', 'c']
b: ['c', 'd']
c: ['d', 'b']
d: ['e']
*/