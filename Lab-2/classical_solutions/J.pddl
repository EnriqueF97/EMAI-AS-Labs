(define (problem maze-J)
  (:domain maze)

  (:objects x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 y1 y2 y3 y4 y5 y6 y7 y8 y9 y10 - coordinate ag - agent kw kr kv ku kp ko kq ks kt ki kj kl kk kf kn kc ke kd km kg ka kb kh - key dw du dv do dp dq dr ds dt di dj dk dl dm dn dc dd de df dg dh da db - door)

  (:init
    ; Adjacency definition
    (inc x1 x2) (inc x2 x3) (inc x3 x4) (inc x4 x5) (inc x5 x6) (inc x6 x7) (inc x7 x8) (inc x8 x9) (inc x9 x10)
    (inc y1 y2) (inc y2 y3) (inc y3 y4) (inc y4 y5) (inc y5 y6) (inc y6 y7) (inc y7 y8) (inc y8 y9) (inc y9 y10)
    (dec x2 x1) (dec x3 x2) (dec x4 x3) (dec x5 x4) (dec x6 x5) (dec x7 x6) (dec x8 x7) (dec x9 x8) (dec x10 x9)
    (dec y2 y1) (dec y3 y2) (dec y4 y3) (dec y5 y4) (dec y6 y5) (dec y7 y6) (dec y8 y7) (dec y9 y8) (dec y10 y9)

    ; Walls
    (obstacle x7 y1) (obstacle x9 y1) (obstacle x1 y2) (obstacle x2 y2) (obstacle x3 y2) (obstacle x4 y2) (obstacle x7 y2) (obstacle x9 y2) (obstacle x2 y3) (obstacle x4 y3) (obstacle x7 y3) (obstacle x9 y3) (obstacle x2 y4) (obstacle x4 y4) (obstacle x7 y4) (obstacle x9 y4) (obstacle x2 y5) (obstacle x4 y5) (obstacle x7 y5) (obstacle x9 y5) (obstacle x2 y6) (obstacle x4 y6) (obstacle x7 y6) (obstacle x9 y6) (obstacle x2 y7) (obstacle x4 y7) (obstacle x7 y7) (obstacle x9 y7) (obstacle x2 y8) (obstacle x4 y8) (obstacle x7 y8) (obstacle x9 y8) (obstacle x2 y9) (obstacle x4 y9) (obstacle x7 y9) (obstacle x9 y9)

    ; Keys
    (key-at kw x8 y1) (key-at kr x10 y1) (key-at kv x1 y3) (key-at ku x3 y3) (key-at kp x6 y3) (key-at ko x8 y4) (key-at kq x10 y4) (key-at ks x1 y6) (key-at kt x3 y6) (key-at ki x5 y6) (key-at kj x6 y6) (key-at kl x8 y6) (key-at kk x10 y6) (key-at kf x1 y8) (key-at kn x3 y8) (key-at kc x5 y8) (key-at ke x8 y8) (key-at kd x10 y8) (key-at km x1 y10) (key-at kg x3 y10) (key-at ka x7 y10) (key-at kb x8 y10) (key-at kh x9 y10)

    ; Doors
    (door-at dw x4 y1) (door-at du x8 y3) (door-at dv x10 y3) (door-at do x1 y5) (door-at dp x3 y5) (door-at dq x5 y5) (door-at dr x6 y5) (door-at ds x8 y5) (door-at dt x10 y5) (door-at di x1 y7) (door-at dj x3 y7) (door-at dk x5 y7) (door-at dl x6 y7) (door-at dm x8 y7) (door-at dn x10 y7) (door-at dc x1 y9) (door-at dd x3 y9) (door-at de x5 y9) (door-at df x6 y9) (door-at dg x8 y9) (door-at dh x10 y9) (door-at da x2 y10) (door-at db x4 y10)

    ; Key-Door Relationships
    (key-unlocks kw dw) (key-unlocks ku du) (key-unlocks kv dv) (key-unlocks ko do) (key-unlocks kp dp) (key-unlocks kq dq) (key-unlocks kr dr) (key-unlocks ks ds) (key-unlocks kt dt) (key-unlocks ki di) (key-unlocks kj dj) (key-unlocks kk dk) (key-unlocks kl dl) (key-unlocks km dm) (key-unlocks kn dn) (key-unlocks kc dc) (key-unlocks kd dd) (key-unlocks ke de) (key-unlocks kf df) (key-unlocks kg dg) (key-unlocks kh dh) (key-unlocks ka da) (key-unlocks kb db)

    ; Initial position
    (at ag x10 y10)
  )

  (:goal
    ; Goal position
    (at ag x1 y1)
  )
)