(define (problem maze-A)
  (:domain maze)

  (:objects x1 x2 x3 x4 x5 y1 y2 y3 y4 y5 - coordinate ag - agent)

  (:init
    ; Adjacency definition
    (inc x1 x2) (inc x2 x3) (inc x3 x4) (inc x4 x5)
    (inc y1 y2) (inc y2 y3) (inc y3 y4) (inc y4 y5)
    (dec x2 x1) (dec x3 x2) (dec x4 x3) (dec x5 x4)
    (dec y2 y1) (dec y3 y2) (dec y4 y3) (dec y5 y4)

    ; Obstacles
    

    ; Initial position
    (at ag x5 y5)
  )

  (:goal
    ; Goal position
    (at ag x1 y1)
  )
)