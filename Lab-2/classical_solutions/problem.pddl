
(define (problem p1)
  (:domain maze)

  (:objects x1 x2 x3 x4 x5 x6 y1 y2 y3 y4 y5 y6 - coordinate ag - agent)

  (:init
    (inc x1 x2) (inc x2 x3) (inc x3 x4) (inc x4 x5) (inc x5 x6)
    (inc y1 y2) (inc y2 y3) (inc y3 y4) (inc y4 y5) (inc y5 y6)
    (dec x6 x5) (dec x5 x4) (dec x4 x3) (dec x3 x2) (dec x2 x1) 
    (dec y6 y5) (dec y5 y4) (dec y4 y3) (dec y3 y2) (dec y2 y1) 

    (obstacle x1 y3) (obstacle x2 y3) (obstacle x3 y3) (obstacle x4 y3)
    (obstacle x5 y4)
    (obstacle x2 y5) (obstacle x3 y5) (obstacle x4 y5)

    (at ag x1 y1))
  (:goal
    (at ag x3 y4))
)