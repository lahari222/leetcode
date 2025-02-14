/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll =function(functions) {
    return new Promise((resolve,reject)=>{
        const result=[]
        let completed=0
        functions.forEach((fn,index)=>{
            fn().then(data=>{
                result[index]=data
                completed+=1
                if(completed===functions.length){
                    resolve(result)
                }
            }).catch(error=>{
                reject(error)
            })
        })
    })
    
    
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */