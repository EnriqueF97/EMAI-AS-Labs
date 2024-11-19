(define (domain maze)
  (:requirements :strips)
  (:types agent coordinate)
  
  (:predicates 
    (inc ?a ?b - coordinate)        ; Increment relationship between coordinates
    (dec ?a ?b - coordinate)        ; Decrement relationship between coordinates
    (at ?a - agent ?x ?y - coordinate) ; Agent is at coordinate (x, y)
    (obstacle ?x ?y)              ; obstacle(x, y)
  )

  (:action move-up
    :parameters (?a - agent ?x ?y ?yn - coordinate)
    :precondition (and
      (at ?a ?x ?y)          ; Agent is at (x, y)
      (dec ?y ?yn)           ; yn is one step up from y
      (not (obstacle ?x ?yn))    ; No obstacle at (x, yn)
    )
    :effect (and
      (not (at ?a ?x ?y))    ; Remove the agent from the current coordinate
      (at ?a ?x ?yn)         ; Place the agent at the new coordinate
    )
  )

  (:action move-down
    :parameters (?a - agent ?x ?y ?yn - coordinate)
    :precondition (and
      (at ?a ?x ?y)          ; Agent is at (x, y)
      (inc ?y ?yn)           ; yn is one step down from y
      (not (obstacle ?x ?yn))    ; No obstacle at (x, yn)
    )
    :effect (and
      (not (at ?a ?x ?y))    ; Remove the agent from the current coordinate
      (at ?a ?x ?yn)         ; Place the agent at the new coordinate
    )
  )

  (:action move-right
    :parameters (?a - agent ?x ?y ?xn - coordinate)
    :precondition (and
      (at ?a ?x ?y)          ; Agent is at (x, y)
      (inc ?x ?xn)           ; xn is one step right from x
      (not (obstacle ?xn ?y))    ; No obstacle at (xn, y)
    )
    :effect (and
      (not (at ?a ?x ?y))    ; Remove the agent from the current coordinate
      (at ?a ?xn ?y)         ; Place the agent at the new coordinate
    )
  )

  (:action move-left
    :parameters (?a - agent ?x ?y ?xn - coordinate)
    :precondition (and
      (at ?a ?x ?y)          ; Agent is at (x, y)
      (dec ?x ?xn)           ; xn is one step left from x
      (not (obstacle ?xn ?y))    ; No obstacle at (xn, y)
    )
    :effect (and
      (not (at ?a ?x ?y))    ; Remove the agent from the current coordinate
      (at ?a ?xn ?y)         ; Place the agent at the new coordinate
    )
  )
)
