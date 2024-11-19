(define (problem maze-E)
  (:domain maze)

  (:objects x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15 y1 y2 y3 y4 y5 y6 y7 y8 y9 y10 y11 y12 y13 y14 y15 - coordinate ag - agent)

  (:init
    ; Adjacency definition
    (inc x1 x2) (inc x2 x3) (inc x3 x4) (inc x4 x5) (inc x5 x6) (inc x6 x7) (inc x7 x8) (inc x8 x9) (inc x9 x10) (inc x10 x11) (inc x11 x12) (inc x12 x13) (inc x13 x14) (inc x14 x15)
    (inc y1 y2) (inc y2 y3) (inc y3 y4) (inc y4 y5) (inc y5 y6) (inc y6 y7) (inc y7 y8) (inc y8 y9) (inc y9 y10) (inc y10 y11) (inc y11 y12) (inc y12 y13) (inc y13 y14) (inc y14 y15)
    (dec x2 x1) (dec x3 x2) (dec x4 x3) (dec x5 x4) (dec x6 x5) (dec x7 x6) (dec x8 x7) (dec x9 x8) (dec x10 x9) (dec x11 x10) (dec x12 x11) (dec x13 x12) (dec x14 x13) (dec x15 x14)
    (dec y2 y1) (dec y3 y2) (dec y4 y3) (dec y5 y4) (dec y6 y5) (dec y7 y6) (dec y8 y7) (dec y9 y8) (dec y10 y9) (dec y11 y10) (dec y12 y11) (dec y13 y12) (dec y14 y13) (dec y15 y14)

    ; Obstacles
    (obstacle x2 y1) (obstacle x6 y1) (obstacle x10 y1) (obstacle x2 y2) (obstacle x4 y2) (obstacle x8 y2) (obstacle x12 y2) (obstacle x13 y2) (obstacle x14 y2) (obstacle x4 y3) (obstacle x5 y3)
    (obstacle x6 y3) (obstacle x7 y3) (obstacle x8 y3) (obstacle x9 y3) (obstacle x10 y3) (obstacle x14 y3) (obstacle x1 y4) (obstacle x2 y4) (obstacle x3 y4) (obstacle x4 y4) (obstacle x6 y4) 
    (obstacle x10 y4) (obstacle x11 y4) (obstacle x12 y4) (obstacle x13 y4) (obstacle x14 y4) (obstacle x6 y5) (obstacle x8 y5) (obstacle x11 y5) (obstacle x2 y6) (obstacle x3 y6) (obstacle x4 y6) 
    (obstacle x5 y6) (obstacle x6 y6) (obstacle x8 y6) (obstacle x9 y6) (obstacle x11 y6) (obstacle x13 y6) (obstacle x14 y6) (obstacle x15 y6) (obstacle x9 y7) (obstacle x11 y7) (obstacle x1 y8) 
    (obstacle x2 y8) (obstacle x3 y8) (obstacle x4 y8) (obstacle x5 y8) (obstacle x6 y8) (obstacle x7 y8) (obstacle x8 y8) (obstacle x9 y8) (obstacle x11 y8) (obstacle x12 y8) (obstacle x13 y8) 
    (obstacle x14 y8) (obstacle x9 y9) (obstacle x14 y9) (obstacle x2 y10) (obstacle x3 y10) (obstacle x4 y10) (obstacle x5 y10) (obstacle x6 y10) (obstacle x7 y10) (obstacle x9 y10) (obstacle x10 y10) 
    (obstacle x11 y10) (obstacle x12 y10) (obstacle x14 y10) (obstacle x2 y11) (obstacle x5 y11) (obstacle x7 y11) (obstacle x14 y11) (obstacle x2 y12) (obstacle x4 y12) (obstacle x5 y12) (obstacle x7 y12) 
    (obstacle x8 y12) (obstacle x9 y12) (obstacle x10 y12) (obstacle x11 y12) (obstacle x12 y12) (obstacle x13 y12) (obstacle x14 y12) (obstacle x2 y13) (obstacle x7 y13) (obstacle x11 y13) (obstacle x2 y14) 
    (obstacle x3 y14) (obstacle x5 y14) (obstacle x7 y14) (obstacle x9 y14) (obstacle x11 y14) (obstacle x13 y14) (obstacle x15 y14) (obstacle x5 y15) (obstacle x9 y15) (obstacle x13 y15)

    ; Initial position
    (at ag x15 y15)
  )

  (:goal
    ; Goal position
    (at ag x1 y1)
  )
)