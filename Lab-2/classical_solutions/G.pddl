(define (problem maze-G)
  (:domain maze)

  (:objects x1 x2 x3 x4 y1 y2 y3 y4 - coordinate ag - agent ka - key da - door)

  (:init
    ; Adjacency definition
    (inc x1 x2) (inc x2 x3) (inc x3 x4)
    (inc y1 y2) (inc y2 y3) (inc y3 y4)
    (dec x2 x1) (dec x3 x2) (dec x4 x3)
    (dec y2 y1) (dec y3 y2) (dec y4 y3)

    ; obstacles
    (obstacle x3 y1) (obstacle x3 y2) (obstacle x2 y3) (obstacle x3 y3)

    ; Keys
    (key-at ka x4 y1)

    ; Doors
    (door-at da x1 y3)

    ; Key-Door Relationships
    (key-unlocks ka da)

    ; Initial position
    (at ag x4 y4)
  )

  (:goal
    ; Goal position
    (at ag x1 y1)
  )
)