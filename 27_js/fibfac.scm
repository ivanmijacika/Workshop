(define fib
        (lambda (n)
                (if (or (= n 0) (= n 1))
                        n
                        (+ (fib (- n 2)) (fib (- n 1)))
                )
        )
)




(define (fact n) ;it's a function called factorial (fact) that takes an argumen>
  (if (= n 0) ;if starts with the condition, and then within it you branch off w>
      1 ;don't actually have to say return, just put the thing you want returned
      (* n (fact (- n 1))) ;recursion! + prefix notation
      )
  ) ;parenthesis



