#lang racket
(define (sum-pos . nums)
  (define (sum-pos-helper nums acc)
    (cond
      [(empty? nums) acc]
      [(positive? (first nums)) (sum-pos-helper (rest nums) (+ (first nums) acc))]
      [else (sum-pos-helper (rest nums) acc)]))
  (sum-pos-helper nums 0))

(define (binmap fn l1 l2)
  (define (binmap-helper fn l1 l2 acc)
    (cond
      [(not (or (empty? l1) (empty? l2)))
           (binmap-helper fn (rest l1) (rest l2) (append acc (list (fn (first l1) (first l2)))))]
      [else acc]))
  (binmap-helper fn l1 l2 '()))


(module+ test
  (require rackunit)
  (check-equal? (sum-pos) 0)
  (check-equal? (sum-pos 1) 1)
  (check-equal? (sum-pos 1 0 -1) 1)
  (check-equal? (apply sum-pos (range -9 10)) 45)
  (check-equal? (binmap + '(1 2 3) '(4 5 6)) '(5 7 9))
  (check-equal? (binmap * '(1 2 3) '(4 5 6)) '(4 10 18))

  (check-equal? (binmap string-append '("hello" "world ")
                                      '(" mom" "travel"))
        '("hello mom" "world travel"))

  (check-equal? (binmap + '(1 2 3) '(4 5 6 7)) '(5 7 9))
  (check-equal? (binmap + '(1 2 3 4) '(4 5 6)) '(5 7 9)))