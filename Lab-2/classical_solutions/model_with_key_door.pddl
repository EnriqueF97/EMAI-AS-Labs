(define (domain maze-key)
  (:requirements :strips :equality :typing :negative-preconditions :disjunctive-preconditions)
  (:types agent coordinate key)

  (:predicates
    (inc ?a ?b - coordinate)
    (dec ?a ?b - coordinate)
    (at ?a - agent ?x ?y - coordinate)
    (obstacle ?x ?y - coordinate)
    (door-at ?x ?y - coordinate)
    (door-locked ?x ?y - coordinate)
    (key-at ?k - key ?x ?y - coordinate)
    (have-key ?k - key)
    (has-key)                          ; Agent is holding a key
    (key-unlocks ?k - key ?x ?y - coordinate)
  )

  ; Action to pick up a key
  (:action pickup-key
    :parameters (?a - agent ?k - key ?x ?y - coordinate)
    :precondition (and
      (at ?a ?x ?y)
      (key-at ?k ?x ?y)
      (not (has-key))                  ; Agent cannot already have a key
    )
    :effect (and
      (have-key ?k)
      (has-key)                        ; Agent now has a key
      (not (key-at ?k ?x ?y))
    )
  )

  ; Action to unlock a door
  (:action unlock-door
    :parameters (?a - agent ?k - key ?x ?y ?xd ?yd - coordinate)
    :precondition (and
      (at ?a ?x ?y)
      (have-key ?k)
      (has-key)
      (key-unlocks ?k ?xd ?yd)
      (door-at ?xd ?yd)
      (door-locked ?xd ?yd)
      (or
        (and (dec ?x ?xd) (= ?y ?yd))
        (and (inc ?x ?xd) (= ?y ?yd))
        (and (dec ?y ?yd) (= ?x ?xd))
        (and (inc ?y ?yd) (= ?x ?xd))
      )
    )
    :effect (and
      (not (door-locked ?xd ?yd))
      (not (have-key ?k))
      (not (has-key))                  ; Agent no longer has a key
    )
  )

  ; Move actions without doors


  (:action up
      :parameters ()
      :precondition (and 
      )
      :effect 
            (forall (?a - agent ?x ?y ?yn - coordinate) 
              (when 
                (and  (not (obstacle ?x ?yn))
                      (not (door-at ?x ?yn))
                      (at ?a ?x ?y)
                      (dec ?y ?yn)
                )
                (and
                    (not (at ?a ?x ?y))
                    (at ?a ?x ?yn)
              ))
            )
  )
  
  ; (:action move-up
  ;   :parameters (?a - agent ?x ?y ?yn - coordinate)
  ;   :precondition (and
  ;     (at ?a ?x ?y)
  ;     (dec ?y ?yn)
  ;     (not (obstacle ?x ?yn))
  ;     (not (door-at ?x ?yn))
  ;   )
  ;   :effect (and
  ;     (not (at ?a ?x ?y))
  ;     (at ?a ?x ?yn)
  ;   )
  ; )

    (:action down
      :parameters ()
      :precondition (and 
      )
      :effect 
            (forall (?a - agent ?x ?y ?yn - coordinate) 
              (when 
                (and  (at ?a ?x ?y)
                      (inc ?y ?yn)
                      (not (obstacle ?x ?yn))
                      (not (door-at ?x ?yn))
                )
                (and
                    (not (at ?a ?x ?y))
                    (at ?a ?x ?yn)
              ))
            )
  )

  ; (:action move-down
  ;   :parameters (?a - agent ?x ?y ?yn - coordinate)
  ;   :precondition (and
  ;     (at ?a ?x ?y)
  ;     (inc ?y ?yn)
  ;     (not (obstacle ?x ?yn))
  ;     (not (door-at ?x ?yn))
  ;   )
  ;   :effect (and
  ;     (not (at ?a ?x ?y))
  ;     (at ?a ?x ?yn)
  ;   )
  ; )

    (:action left
      :parameters ()
      :precondition (and 
      )
      :effect 
            (forall (?a - agent ?x ?y ?xn - coordinate) 
              (when 
                (and  (at ?a ?x ?y)
                      (dec ?x ?xn)
                      (not (obstacle ?xn ?y))
                      (not (door-at ?xn ?y))
                )
                (and
                    (not (at ?a ?x ?y))
                    (at ?a ?xn ?y)
              ))
            )
  )
  

  ; (:action move-left
  ;   :parameters (?a - agent ?x ?y ?xn - coordinate)
  ;   :precondition (and
  ;     (at ?a ?x ?y)
  ;     (dec ?x ?xn)
  ;     (not (obstacle ?xn ?y))
  ;     (not (door-at ?xn ?y))
  ;   )
  ;   :effect (and
  ;     (not (at ?a ?x ?y))
  ;     (at ?a ?xn ?y)
  ;   )
  ; )

   (:action right
      :parameters ()
      :precondition (and 
      )
      :effect 
            (forall (?a - agent ?x ?y ?xn - coordinate) 
              (when 
                (and  (at ?a ?x ?y)
                      (inc ?x ?xn)
                      (not (obstacle ?xn ?y))
                      (not (door-at ?xn ?y))
                )
                (and
                    (not (at ?a ?x ?y))
                    (at ?a ?xn ?y)
              ))
            )
  )


  ; (:action move-right
  ;   :parameters (?a - agent ?x ?y ?xn - coordinate)
  ;   :precondition (and
  ;     (at ?a ?x ?y)
  ;     (inc ?x ?xn)
  ;     (not (obstacle ?xn ?y))
  ;     (not (door-at ?xn ?y))
  ;   )
  ;   :effect (and
  ;     (not (at ?a ?x ?y))
  ;     (at ?a ?xn ?y)
  ;   )
  ; )

  ; Move actions through unlocked doors
  (:action move-up-through-door
    :parameters (?a - agent ?x ?y ?yn - coordinate)
    :precondition (and
      (at ?a ?x ?y)
      (dec ?y ?yn)
      (door-at ?x ?yn)
      (not (door-locked ?x ?yn))
    )
    :effect (and
      (not (at ?a ?x ?y))
      (at ?a ?x ?yn)
    )
  )

  (:action move-down-through-door
    :parameters (?a - agent ?x ?y ?yn - coordinate)
    :precondition (and
      (at ?a ?x ?y)
      (inc ?y ?yn)
      (door-at ?x ?yn)
      (not (door-locked ?x ?yn))
    )
    :effect (and
      (not (at ?a ?x ?y))
      (at ?a ?x ?yn)
    )
  )

  (:action move-left-through-door
    :parameters (?a - agent ?x ?y ?xn - coordinate)
    :precondition (and
      (at ?a ?x ?y)
      (dec ?x ?xn)
      (door-at ?xn ?y)
      (not (door-locked ?xn ?y))
    )
    :effect (and
      (not (at ?a ?x ?y))
      (at ?a ?xn ?y)
    )
  )

  (:action move-right-through-door
    :parameters (?a - agent ?x ?y ?xn - coordinate)
    :precondition (and
      (at ?a ?x ?y)
      (inc ?x ?xn)
      (door-at ?xn ?y)
      (not (door-locked ?xn ?y))
    )
    :effect (and
      (not (at ?a ?x ?y))
      (at ?a ?xn ?y)
    )
  )
)
