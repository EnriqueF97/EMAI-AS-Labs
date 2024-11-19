(define (problem maze-F)
  (:domain maze)

  (:objects x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15 x16 x17 x18 x19 x20 y1 y2 y3 y4 y5 y6 y7 y8 y9 y10 y11 y12 y13 y14 y15 y16 y17 y18 y19 y20 - coordinate ag - agent)

  (:init
    ; Adjacency definition
    (inc x1 x2) (inc x2 x3) (inc x3 x4) (inc x4 x5) (inc x5 x6) (inc x6 x7) (inc x7 x8) (inc x8 x9) (inc x9 x10) (inc x10 x11) (inc x11 x12) (inc x12 x13) (inc x13 x14) (inc x14 x15) (inc x15 x16) (inc x16 x17) (inc x17 x18) (inc x18 x19) (inc x19 x20)
    (inc y1 y2) (inc y2 y3) (inc y3 y4) (inc y4 y5) (inc y5 y6) (inc y6 y7) (inc y7 y8) (inc y8 y9) (inc y9 y10) (inc y10 y11) (inc y11 y12) (inc y12 y13) (inc y13 y14) (inc y14 y15) (inc y15 y16) (inc y16 y17) (inc y17 y18) (inc y18 y19) (inc y19 y20)
    (dec x2 x1) (dec x3 x2) (dec x4 x3) (dec x5 x4) (dec x6 x5) (dec x7 x6) (dec x8 x7) (dec x9 x8) (dec x10 x9) (dec x11 x10) (dec x12 x11) (dec x13 x12) (dec x14 x13) (dec x15 x14) (dec x16 x15) (dec x17 x16) (dec x18 x17) (dec x19 x18) (dec x20 x19)
    (dec y2 y1) (dec y3 y2) (dec y4 y3) (dec y5 y4) (dec y6 y5) (dec y7 y6) (dec y8 y7) (dec y9 y8) (dec y10 y9) (dec y11 y10) (dec y12 y11) (dec y13 y12) (dec y14 y13) (dec y15 y14) (dec y16 y15) (dec y17 y16) (dec y18 y17) (dec y19 y18) (dec y20 y19)

    ; Obstacles
    (obstacle x6 y1) (obstacle x11 y1) (obstacle x16 y1) (obstacle x1 y2) (obstacle x2 y2) (obstacle x3 y2) (obstacle x4 y2) (obstacle x6 y2) (obstacle x7 y2) (obstacle x8 y2) (obstacle x9 y2) (obstacle x11 y2) (obstacle x13 y2) (obstacle x14 y2) (obstacle x15 y2)
    (obstacle x16 y2) (obstacle x17 y2) (obstacle x18 y2) (obstacle x19 y2) (obstacle x6 y3) (obstacle x11 y3) (obstacle x17 y3) (obstacle x19 y3) (obstacle x2 y4) (obstacle x3 y4) (obstacle x4 y4) (obstacle x5 y4) (obstacle x6 y4) (obstacle x8 y4) (obstacle x9 y4) 
    (obstacle x10 y4) (obstacle x11 y4) (obstacle x12 y4) (obstacle x13 y4) (obstacle x15 y4) (obstacle x17 y4) (obstacle x19 y4) (obstacle x2 y5) (obstacle x8 y5) (obstacle x15 y5) (obstacle x17 y5) (obstacle x19 y5) (obstacle x4 y6) (obstacle x5 y6) (obstacle x6 y6) 
    (obstacle x8 y6) (obstacle x10 y6) (obstacle x11 y6) (obstacle x12 y6) (obstacle x13 y6) (obstacle x14 y6) (obstacle x15 y6) (obstacle x17 y6) (obstacle x1 y7) (obstacle x2 y7) (obstacle x3 y7) (obstacle x4 y7) (obstacle x8 y7) (obstacle x10 y7) (obstacle x17 y7) 
    (obstacle x19 y7) (obstacle x20 y7) (obstacle x6 y8) (obstacle x8 y8) (obstacle x10 y8) (obstacle x12 y8) (obstacle x13 y8) (obstacle x14 y8) (obstacle x15 y8) (obstacle x16 y8) (obstacle x17 y8) (obstacle x2 y9) (obstacle x3 y9) (obstacle x4 y9) (obstacle x5 y9) 
    (obstacle x6 y9) (obstacle x8 y9) (obstacle x10 y9) (obstacle x17 y9) (obstacle x18 y9) (obstacle x19 y9) (obstacle x2 y10) (obstacle x8 y10) (obstacle x10 y10) (obstacle x11 y10) (obstacle x12 y10) (obstacle x13 y10) (obstacle x14 y10) (obstacle x15 y10) 
    (obstacle x17 y10) (obstacle x2 y11) (obstacle x3 y11) (obstacle x4 y11) (obstacle x5 y11) (obstacle x6 y11) (obstacle x7 y11) (obstacle x8 y11) (obstacle x10 y11) (obstacle x13 y11) (obstacle x17 y11) (obstacle x19 y11) (obstacle x10 y12) (obstacle x12 y12) 
    (obstacle x13 y12) (obstacle x15 y12) (obstacle x16 y12) (obstacle x17 y12) (obstacle x19 y12) (obstacle x1 y13) (obstacle x2 y13) (obstacle x3 y13) (obstacle x4 y13) (obstacle x5 y13) (obstacle x6 y13) (obstacle x7 y13) (obstacle x8 y13) (obstacle x9 y13) 
    (obstacle x10 y13) (obstacle x15 y13) (obstacle x19 y13) (obstacle x10 y14) (obstacle x12 y14) (obstacle x13 y14) (obstacle x14 y14) (obstacle x15 y14) (obstacle x17 y14) (obstacle x18 y14) (obstacle x19 y14) (obstacle x2 y15) (obstacle x3 y15) (obstacle x4 y15) 
    (obstacle x5 y15) (obstacle x6 y15) (obstacle x7 y15) (obstacle x8 y15) (obstacle x9 y15) (obstacle x10 y15) (obstacle x12 y15) (obstacle x15 y15) (obstacle x19 y15) (obstacle x12 y16) (obstacle x14 y16) (obstacle x15 y16) (obstacle x16 y16) (obstacle x17 y16) 
    (obstacle x19 y16) (obstacle x20 y16) (obstacle x2 y17) (obstacle x3 y17) (obstacle x4 y17) (obstacle x5 y17) (obstacle x7 y17) (obstacle x8 y17) (obstacle x9 y17) (obstacle x10 y17) (obstacle x11 y17) (obstacle x12 y17) (obstacle x14 y17) (obstacle x5 y18) 
    (obstacle x14 y18) (obstacle x16 y18) (obstacle x17 y18) (obstacle x18 y18) (obstacle x19 y18) (obstacle x1 y19) (obstacle x2 y19) (obstacle x3 y19) (obstacle x5 y19) (obstacle x6 y19) (obstacle x7 y19) (obstacle x8 y19) (obstacle x9 y19) (obstacle x10 y19) 
    (obstacle x11 y19) (obstacle x12 y19) (obstacle x13 y19) (obstacle x14 y19) (obstacle x19 y19) (obstacle x16 y20) (obstacle x17 y20) (obstacle x19 y20)

    ; Initial position
    (at ag x20 y20)
  )

  (:goal
    ; Goal position
    (at ag x1 y1)
  )
)