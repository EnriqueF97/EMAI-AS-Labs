(define (domain maze)
  (:requirements :strips)
  (:types agent position)
  
  (:predicates 
    (inc ?a ?b - position)  ; Increment relationship between positions
    (dec ?a ?b - position)  ; Decrement relationship between positions
    (at ?a - agent ?x ?y - position) ; Agent is at position (x, y)
    (wall ?x ?y)            ; There is a wall at position (x, y)
  )

  (:action move-up
    :parameters (?a - agent ?x ?y ?yn - position)
    :precondition (and
      (at ?a ?x ?y)          ; Agent is at (x, y)
      (dec ?y ?yn)           ; yn is one step up from y
      (not (wall ?x ?yn))    ; No wall at (x, yn)
    )
    :effect (and
      (not (at ?a ?x ?y))    ; Remove the agent from the current position
      (at ?a ?x ?yn)         ; Place the agent at the new position
    )
  )

  (:action move-down
    :parameters (?a - agent ?x ?y ?yn - position)
    :precondition (and
      (at ?a ?x ?y)          ; Agent is at (x, y)
      (inc ?y ?yn)           ; yn is one step down from y
      (not (wall ?x ?yn))    ; No wall at (x, yn)
    )
    :effect (and
      (not (at ?a ?x ?y))    ; Remove the agent from the current position
      (at ?a ?x ?yn)         ; Place the agent at the new position
    )
  )

  (:action move-right
    :parameters (?a - agent ?x ?y ?xn - position)
    :precondition (and
      (at ?a ?x ?y)          ; Agent is at (x, y)
      (inc ?x ?xn)           ; xn is one step right from x
      (not (wall ?xn ?y))    ; No wall at (xn, y)
    )
    :effect (and
      (not (at ?a ?x ?y))    ; Remove the agent from the current position
      (at ?a ?xn ?y)         ; Place the agent at the new position
    )
  )

  (:action move-left
    :parameters (?a - agent ?x ?y ?xn - position)
    :precondition (and
      (at ?a ?x ?y)          ; Agent is at (x, y)
      (dec ?x ?xn)           ; xn is one step left from x
      (not (wall ?xn ?y))    ; No wall at (xn, y)
    )
    :effect (and
      (not (at ?a ?x ?y))    ; Remove the agent from the current position
      (at ?a ?xn ?y)         ; Place the agent at the new position
    )
  )
)
