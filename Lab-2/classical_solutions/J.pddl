(define (problem maze-J)
  (:domain maze-key)

  (:objects
    x1 x2 x3 x4 x5 x6 x7 x8 x9 x10
    y1 y2 y3 y4 y5 y6 y7 y8 y9 y10 - coordinate
    ag - agent
    kw kr kv ku kp ko kq ks kt ki kj kl kk kf kn kc ke kd km kg ka kb kh - key
  )

  (:init
    ; Adjacency definition
    (inc x1 x2) (inc x2 x3) (inc x3 x4) (inc x4 x5) (inc x5 x6) (inc x6 x7) (inc x7 x8) (inc x8 x9) (inc x9 x10)
    (inc y1 y2) (inc y2 y3) (inc y3 y4) (inc y4 y5) (inc y5 y6) (inc y6 y7) (inc y7 y8) (inc y8 y9) (inc y9 y10)
    (dec x2 x1) (dec x3 x2) (dec x4 x3) (dec x5 x4) (dec x6 x5) (dec x7 x6) (dec x8 x7) (dec x9 x8) (dec x10 x9)
    (dec y2 y1) (dec y3 y2) (dec y4 y3) (dec y5 y4) (dec y6 y5) (dec y7 y6) (dec y8 y7) (dec y9 y8) (dec y10 y9)

    ; Obstacles
    (obstacle x7 y1) (obstacle x9 y1)
    (obstacle x1 y2) (obstacle x2 y2) (obstacle x3 y2) (obstacle x4 y2) (obstacle x7 y2) (obstacle x9 y2)
    (obstacle x2 y3) (obstacle x4 y3) (obstacle x7 y3) (obstacle x9 y3)
    (obstacle x2 y4) (obstacle x4 y4) (obstacle x7 y4) (obstacle x9 y4)
    (obstacle x2 y5) (obstacle x4 y5) (obstacle x7 y5) (obstacle x9 y5)
    (obstacle x2 y6) (obstacle x4 y6) (obstacle x7 y6) (obstacle x9 y6)
    (obstacle x2 y7) (obstacle x4 y7) (obstacle x7 y7) (obstacle x9 y7)
    (obstacle x2 y8) (obstacle x4 y8) (obstacle x7 y8) (obstacle x9 y8)
    (obstacle x2 y9) (obstacle x4 y9) (obstacle x7 y9) (obstacle x9 y9)

    ; Keys
    (key-at kw x8 y1) (key-at kr x10 y1) (key-at kv x1 y3) (key-at ku x3 y3)
    (key-at kp x6 y3) (key-at ko x8 y4) (key-at kq x10 y4)
    (key-at ks x1 y6) (key-at kt x3 y6) (key-at ki x5 y6)
    (key-at kj x6 y6) (key-at kl x8 y6) (key-at kk x10 y6)
    (key-at kf x1 y8) (key-at kn x3 y8) (key-at kc x5 y8)
    (key-at ke x8 y8) (key-at kd x10 y8)
    (key-at km x1 y10) (key-at kg x3 y10) (key-at ka x7 y10)
    (key-at kb x8 y10) (key-at kh x9 y10)

    ; ; Doors (represented by their coordinates)
    ; (door-at x4 y1) (door-locked x4 y1)    ; dw
    ; (door-at x8 y3) (door-locked x8 y3)    ; du
    ; (door-at x10 y3) (door-locked x10 y3)  ; dv
    ; (door-at x1 y5) (door-locked x1 y5)    ; do
    ; (door-at x3 y5) (door-locked x3 y5)    ; dp
    ; (door-at x5 y5) (door-locked x5 y5)    ; dq
    ; (door-at x6 y5) (door-locked x6 y5)    ; dr
    ; (door-at x8 y5) (door-locked x8 y5)    ; ds
    ; (door-at x10 y5) (door-locked x10 y5)  ; dt
    ; (door-at x1 y7) (door-locked x1 y7)    ; di
    ; (door-at x3 y7) (door-locked x3 y7)    ; dj
    ; (door-at x5 y7) (door-locked x5 y7)    ; dk
    ; (door-at x6 y7) (door-locked x6 y7)    ; dl
    ; (door-at x8 y7) (door-locked x8 y7)    ; dm
    ; (door-at x10 y7) (door-locked x10 y7)  ; dn
    ; (door-at x1 y9) (door-locked x1 y9)    ; dc
    ; (door-at x3 y9) (door-locked x3 y9)    ; dd
    ; (door-at x5 y9) (door-locked x5 y9)    ; de
    ; (door-at x6 y9) (door-locked x6 y9)    ; df
    ; (door-at x8 y9) (door-locked x8 y9)    ; dg
    ; (door-at x10 y9) (door-locked x10 y9)  ; dh
    ; (door-at x2 y10) (door-locked x2 y10)  ; da
    ; (door-at x4 y10) (door-locked x4 y10)  ; db

    ; Key-Door Relationships
    (key-unlocks kw x4 y1)     ; kw unlocks door at (x4, y1)
    (key-unlocks ku x8 y3)     ; ku unlocks door at (x8, y3)
    (key-unlocks kv x10 y3)    ; kv unlocks door at (x10, y3)
    (key-unlocks ko x1 y5)     ; ko unlocks door at (x1, y5)
    (key-unlocks kp x3 y5)     ; kp unlocks door at (x3, y5)
    (key-unlocks kq x5 y5)     ; kq unlocks door at (x5, y5)
    (key-unlocks kr x6 y5)     ; kr unlocks door at (x6, y5)
    (key-unlocks ks x8 y5)     ; ks unlocks door at (x8, y5)
    (key-unlocks kt x10 y5)    ; kt unlocks door at (x10, y5)
    (key-unlocks ki x1 y7)     ; ki unlocks door at (x1, y7)
    (key-unlocks kj x3 y7)     ; kj unlocks door at (x3, y7)
    (key-unlocks kk x5 y7)     ; kk unlocks door at (x5, y7)
    (key-unlocks kl x6 y7)     ; kl unlocks door at (x6, y7)
    (key-unlocks km x8 y7)     ; km unlocks door at (x8, y7)
    (key-unlocks kn x10 y7)    ; kn unlocks door at (x10, y7)
    (key-unlocks kc x1 y9)     ; kc unlocks door at (x1, y9)
    (key-unlocks kd x3 y9)     ; kd unlocks door at (x3, y9)
    (key-unlocks ke x5 y9)     ; ke unlocks door at (x5, y9)
    (key-unlocks kf x6 y9)     ; kf unlocks door at (x6, y9)
    (key-unlocks kg x8 y9)     ; kg unlocks door at (x8, y9)
    (key-unlocks kh x10 y9)    ; kh unlocks door at (x10, y9)
    (key-unlocks ka x2 y10)    ; ka unlocks door at (x2, y10)
    (key-unlocks kb x4 y10)    ; kb unlocks door at (x4, y10)

    ; Initial position
    (at ag x10 y10)
  )

  (:goal
    ; Goal position
    (at ag x1 y1)
  )
)
