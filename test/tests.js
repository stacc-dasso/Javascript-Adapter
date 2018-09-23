function assert(value, message) { 
    if (!value) { 
		console.log("test failed")
        throw new Error('Assertion Error: ' + message);
    }
}


assert(1==1, "Failure with comparing integers")