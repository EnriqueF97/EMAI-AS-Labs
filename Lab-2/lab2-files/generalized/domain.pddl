(define (domain gripper-strips)
   (:requirements :typing :strips)
   (:types room gripper ball - object)
   (:constants left right - gripper rooma roomb - room)
   
   ; ToDo: 
   ; - create the predicates (hint: look at the instances files first!)
   ; - fill the preconditions and effects in every action schema
   ; - you are not allowed to use quantifiers or conditional effects!
   
   (:predicates )

   (:action move
       :parameters (?from - room ?to - room)
       :precondition (and  )
       :effect (and  )
   )

   (:action pick
       :parameters (?b - ball ?r - room ?g - gripper)
       :precondition (and  )
       :effect (and  )
   )

   (:action drop
       :parameters (?b - ball ?r - room ?g - gripper)
       :precondition (and  )
       :effect (and  )
   )
)
