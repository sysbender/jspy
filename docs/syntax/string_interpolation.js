var assert = require('assert');

const name = 'John'
const age = 40
expected = 'John is 40'
result = `${name} is ${age}`
console.log(result)
console.log(expected)

assert.equal( expected ,  result);