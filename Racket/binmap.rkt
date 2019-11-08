#lang racket
(require dyoo-while-loop)

(define (binmap fn x y) 
  (map (lambda (i) (list (fn i (first y)
         (while((not (empty? (rest y))))
               (fn i (first y))))))x))

(module+ test
  (require rackunit)

  (check-equal? (binmap + '(1 2 3) '(4 5 6)) '(5 7 9))
  (check-equal? (binmap * '(1 2 3) '(4 5 6)) '(4 10 18)))