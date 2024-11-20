(define (domain gripper-strips)
   (:requirements :typing :strips)
   (:types room gripper ball - object)
   (:constants left right - gripper rooma roomb - room)
   
   ; ToDo: 
   ; - create the predicates (hint: look at the instances files first!)
   ; - fill the preconditions and effects in every action schema
   ; - you are not allowed to use quantifiers or conditional effects!
   
   (:predicates 
        (at-robot ?r - room)
        (at ?b - ball ?r - room)
        (free ?g - gripper)
        (holding ?g - gripper ?b - ball)
    )

   (:action move
   :parameters (?from - room ?to - room)
   :precondition (at-robot ?from)
   :effect (and 
            (not (at-robot ?from))
            (at-robot ?to)
        )
    )


   (:action pick
   :parameters (?b - ball ?r - room ?g - gripper)
   :precondition (and
            (at-robot ?r)
            (at ?b ?r)
            (free ?g)
        )
    :effect (and
            (not (at ?b ?r))
            (not (free ?g))
            (holding ?g ?b)
        )
    )

   (:action drop
   :parameters (?b - ball ?r - room ?g - gripper)
   :precondition (and
            (at-robot ?r)
            (holding ?g ?b)
        )
   :effect (and
            (at ?b ?r)
            (free ?g)
            (not (holding ?g ?b))
        )
    )

)
