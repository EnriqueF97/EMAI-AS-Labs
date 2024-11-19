(define (problem maze-D)
  (:domain maze)

  (:objects x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 y1 y2 y3 y4 y5 y6 y7 y8 y9 y10 - coordinate ag - agent)

  (:init
    ; Adjacency definition
    (inc x1 x2) (inc x2 x3) (inc x3 x4) (inc x4 x5) (inc x5 x6) (inc x6 x7) (inc x7 x8) (inc x8 x9) (inc x9 x10)
    (inc y1 y2) (inc y2 y3) (inc y3 y4) (inc y4 y5) (inc y5 y6) (inc y6 y7) (inc y7 y8) (inc y8 y9) (inc y9 y10)
    (dec x2 x1) (dec x3 x2) (dec x4 x3) (dec x5 x4) (dec x6 x5) (dec x7 x6) (dec x8 x7) (dec x9 x8) (dec x10 x9)
    (dec y2 y1) (dec y3 y2) (dec y4 y3) (dec y5 y4) (dec y6 y5) (dec y7 y6) (dec y8 y7) (dec y9 y8) (dec y10 y9)

    ; Obstacles
    (obstacle x4 y1) (obstacle x5 y1) (obstacle x7 y1) (obstacle x9 y1) (obstacle x1 y2) (obstacle x2 y2) (obstacle x7 y2) (obstacle x9 y2) (obstacle x2 y3) (obstacle x3 y3) (obstacle x4 y3) (obstacle x5 y3) (obstacle x7 y3) (obstacle x9 y3) (obstacle x5 y4) (obstacle x9 y4) (obstacle x1 y5) (obstacle x2 y5) (obstacle x3 y5) (obstacle x5 y5) (obstacle x6 y5) (obstacle x7 y5) (obstacle x9 y5) (obstacle x9 y6) (obstacle x2 y7) (obstacle x3 y7) (obstacle x4 y7) (obstacle x5 y7) (obstacle x6 y7) (obstacle x7 y7) (obstacle x8 y7) (obstacle x9 y7) (obstacle x2 y8) (obstacle x6 y8) (obstacle x2 y9) (obstacle x4 y9) (obstacle x6 y9) (obstacle x8 y9) (obstacle x10 y9) (obstacle x4 y10) (obstacle x8 y10)

    ; Initial position
    (at ag x10 y10)
  )

  (:goal
    ; Goal position
    (at ag x1 y1)
  )
)