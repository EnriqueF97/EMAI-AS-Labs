(define (domain maze)
  (:requirements :strips)
  (:types agent coordinate)
  
  (:predicates 
    (inc ?a ?b - coordinate)  ; Increment relationship between coordinates
    (dec ?a ?b - coordinate)  ; Decrement relationship between coordinates
    (at ?x ?y - coordinate) ; Agent is at coordinate (x, y)
    (wall ?x ?y)            ; There is a wall at coordinate (x, y)
  )

  (:action move-up
    :parameters (?x ?y ?yn - coordinate)
    :precondition (and
      (at ?x ?y)          ; Agent is at (x, y)
      (dec ?y ?yn)           ; yn is one step up from y
      (not (wall ?x ?yn))    ; No wall at (x, yn)
    )
    :effect (and
      (not (at ?x ?y))    ; Remove the agent from the current coordinate
      (at ?x ?yn)         ; Place the agent at the new coordinate
    )
  )

  (:action move-down
    :parameters (?x ?y ?yn - coordinate)
    :precondition (and
      (at ?x ?y)          ; Agent is at (x, y)
      (inc ?y ?yn)           ; yn is one step down from y
      (not (wall ?x ?yn))    ; No wall at (x, yn)
    )
    :effect (and
      (not (at ?x ?y))    ; Remove the agent from the current coordinate
      (at ?x ?yn)         ; Place the agent at the new coordinate
    )
  )

  (:action move-right
    :parameters (?x ?y ?xn - coordinate)
    :precondition (and
      (at ?x ?y)          ; Agent is at (x, y)
      (inc ?x ?xn)           ; xn is one step right from x
      (not (wall ?xn ?y))    ; No wall at (xn, y)
    )
    :effect (and
      (not (at ?x ?y))    ; Remove the agent from the current coordinate
      (at ?xn ?y)         ; Place the agent at the new coordinate
    )
  )

  (:action move-left
    :parameters (?x ?y ?xn - coordinate)
    :precondition (and
      (at ?x ?y)          ; Agent is at (x, y)
      (dec ?x ?xn)           ; xn is one step left from x
      (not (wall ?xn ?y))    ; No wall at (xn, y)
    )
    :effect (and
      (not (at ?x ?y))    ; Remove the agent from the current coordinate
      (at ?xn ?y)         ; Place the agent at the new coordinate
    )
  )
)
