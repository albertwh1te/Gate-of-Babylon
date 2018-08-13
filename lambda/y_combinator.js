const Y = f => (x => x(x))(x => f(y => x(x)(y)))
const fib_gen = f => n => n < 2 ? 1 : f(n - 1) + f(n - 2)
const power_gen = f => (n => n * n)
console.log(Y(power_gen)(10))
for (let index = 0; index < 10; index++) {
    console.log(Y(fib_gen)(index))
}
