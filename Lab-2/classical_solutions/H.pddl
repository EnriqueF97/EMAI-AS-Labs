(define (problem maze-H)
  (:domain maze)

  (:objects x1 x2 x3 x4 x5 y1 y2 y3 y4 y5 - coordinate ag - agent kc kb ka - key dc db da - door)

  (:init
    ; Adjacency definition
    (inc x1 x2) (inc x2 x3) (inc x3 x4) (inc x4 x5)
    (inc y1 y2) (inc y2 y3) (inc y3 y4) (inc y4 y5)
    (dec x2 x1) (dec x3 x2) (dec x4 x3) (dec x5 x4)
    (dec y2 y1) (dec y3 y2) (dec y4 y3) (dec y5 y4)

    ; Walls
    (obstacle x3 y1) (obstacle x2 y2) (obstacle x3 y2) (obstacle x3 y3) (obstacle x2 y4) (obstacle x3 y4)

    ; Keys
    ; (key-at kc x5 y1) (key-at kb x5 y2) 
    (key-at ka x5 y3)

    ; Doors
    ; (door-at dc x1 y2) (door-at db x1 y4) 
    (door-at da x3 y5)

    ; Key-Door Relationships
    ; (key-unlocks kc dc) (key-unlocks kb db) 
    (key-unlocks ka da)

    ; Initial position
    (at ag x5 y5)

    (not (door-unlocked da))
  )

  (:goal
    ; Goal position
    (at ag x1 y1)
  )
)