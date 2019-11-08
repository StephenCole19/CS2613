#lang racket

(define (tree-map fn x)
  (map (lambda (i) (fn i))x)
)
