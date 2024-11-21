(define (problem maze-I)
  (:domain maze-key)

  (:objects
    x1 x2 x3 x4 x5 x6 x7
    y1 y2 y3 y4 y5 y6 y7 - coordinate
    ag - agent
    kc kb ka - key
  )

  (:init
    ; Adjacency definition
    (inc x1 x2) (inc x2 x3) (inc x3 x4) (inc x4 x5) (inc x5 x6) (inc x6 x7)
    (inc y1 y2) (inc y2 y3) (inc y3 y4) (inc y4 y5) (inc y5 y6) (inc y6 y7)
    (dec x2 x1) (dec x3 x2) (dec x4 x3) (dec x5 x4) (dec x6 x5) (dec x7 x6)
    (dec y2 y1) (dec y3 y2) (dec y4 y3) (dec y5 y4) (dec y6 y5) (dec y7 y6)

    ; Obstacles
    (obstacle x4 y1) (obstacle x4 y2) (obstacle x4 y3)
    (obstacle x1 y4) (obstacle x3 y4) (obstacle x4 y4)
    (obstacle x5 y4) (obstacle x7 y4) (obstacle x4 y5)
    (obstacle x4 y7)

    ; Keys
    (key-at kc x7 y1)
    (key-at kb x1 y5)
    (key-at ka x5 y5)

    ; Doors (represented by their coordinates)
    (door-at x2 y4)
    (door-at x6 y4)
    (door-at x4 y6)
    ; (door-locked x2 y4)
    ; (door-locked x6 y4)
    ; (door-locked x4 y6)

    ; Key-Door Relationships
    (key-unlocks kc x2 y4)
    (key-unlocks kb x6 y4)
    (key-unlocks ka x4 y6)

    ; Initial position
    (at ag x7 y7)
  )

  (:goal
    ; Goal position
    (at ag x1 y1)
  )
)
