(define (domain maze)
  (:requirements :strips)
  (:types agent coordinate key door)
  
  (:predicates 
    (inc ?a ?b - coordinate)        ; Increment relationship between coordinates
    (dec ?a ?b - coordinate)        ; Decrement relationship between coordinates
    (at ?a - agent ?x ?y - coordinate) ; Agent is at coordinate (x, y)
    (obstacle ?x ?y)                    ; Obstacle at coordinate (x, y)
    (door-at ?d - door ?x ?y - coordinate) ; Door at coordinate
    (key-at ?k - key ?x ?y - coordinate)   ; Key at coordinate
    (have-key ?k - key)             ; Agent has the key
    (has-key)                             ; Agent has a key
    (door-unlocked ?d - door)       ; Door is unlocked
    (key-unlocks ?k - key ?d - door) ; Key unlocks door
  )

  (:action pickup-key
    :parameters (?a - agent ?k - key ?x ?y - coordinate)
    :precondition (and 
      (at ?a ?x ?y)
      (key-at ?k ?x ?y)
      (not (has-key))
    )
    :effect (and 
      (have-key ?k)
      (has-key)
      (not (key-at ?k ?x ?y)) ; Remove the key from its position
    )
  )

  (:action unlock-door-up-down
    :parameters (?a - agent ?k - key ?d - door ?x ?y ?xd ?yd - coordinate)
    :precondition (and 
      (at ?a ?x ?y)           ; Agent is at the door’s position
      (door-at ?d ?x ?yd)      ; There is a door at the position x of agent
      (have-key ?k)           ; The agent has the key
      (has-key)
      (key-unlocks ?k ?d)     ; The key unlocks the door
      (or (dec ?y ?yd) (inc ?y ?yd))            ; The door's y is inc or dec from agent
    )
    :effect (and 
      (door-unlocked ?d)      ; Unlock the door
      (not (has-key))
    )
  )

  (:action unlock-door-left-right
    :parameters (?a - agent ?k - key ?d - door ?x ?y ?xd ?yd - coordinate)
    :precondition (and 
      (at ?a ?x ?y)           ; Agent is at the door’s position
      (door-at ?d ?xd ?y)      ; There is a door at the position y of agent
      (have-key ?k)           ; The agent has the key
      (key-unlocks ?k ?d)     ; The key unlocks the door
      (or (dec ?x ?xd) (inc ?x ?xd))            ; The door's y is inc or dec from agent
    )
    :effect (and 
      (door-unlocked ?d)      ; Unlock the door
      (not (has-key))
    )
  )

  (:action move-up
    :parameters (?a - agent ?x ?y ?yn - coordinate ?d - door)
    :precondition (and
      (at ?a ?x ?y)
      (dec ?y ?yn)
      (not (obstacle ?x ?yn))
      (or
        (not (door-at ?d ?x ?yn))      ; No door at target position
        (door-unlocked ?d)             ; Door is unlocked
      )
    )
    :effect (and
      (not (at ?a ?x ?y))
      (at ?a ?x ?yn)
    )
  )

  (:action move-down
    :parameters (?a - agent ?x ?y ?yn - coordinate ?d - door)
    :precondition (and
      (at ?a ?x ?y)
      (inc ?y ?yn)
      (not (obstacle ?x ?yn))
      (or
        (not (door-at ?d ?x ?yn))
        (door-unlocked ?d)
      )
    )
    :effect (and
      (not (at ?a ?x ?y))
      (at ?a ?x ?yn)
    )
  )

  (:action move-right
    :parameters (?a - agent ?x ?y ?xn - coordinate ?d - door)
    :precondition (and
      (at ?a ?x ?y)
      (inc ?x ?xn)
      (not (obstacle ?xn ?y))
      (or
        (not (door-at ?d ?xn ?y))
        (door-unlocked ?d)
      )
    )
    :effect (and
      (not (at ?a ?x ?y))
      (at ?a ?xn ?y)
    )
  )

  (:action move-left
    :parameters (?a - agent ?x ?y ?xn - coordinate ?d - door)
    :precondition (and
      (at ?a ?x ?y)
      (dec ?x ?xn)
      (not (obstacle ?xn ?y))
      (or
        (not (door-at ?d ?xn ?y))
        (door-unlocked ?d)
      )
    )
    :effect (and
      (not (at ?a ?x ?y))
      (at ?a ?xn ?y)
    )
  )
)
