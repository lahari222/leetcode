/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const obj={}
    
    return function(...args) {
        const key=JSON.stringify(args);
        if(key in obj){
            return obj[key]
        }
        const result=fn(...args);
        obj[key]=result
        return result;
        
        
        
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */