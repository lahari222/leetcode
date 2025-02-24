var TimeLimitedCache = function() {
    this.obj={}
    
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    let exists = this.obj[key] !== undefined;
    if (exists) {
        clearTimeout(this.obj[key].timeout);
    }

    this.obj[key] = {
        value: value,
        timeout: setTimeout(() => delete this.obj[key], duration)
    };

    return exists;
    
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if(this.obj[key]){
        return this.obj[key].value
    }
    else{
        return -1
    }
    
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return Object.keys(this.obj).length
    
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */