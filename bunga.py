import turtle as tt

t = tt.Turtle()
t.speed('fastest') #mengubah kecepatan turtle menjadi maksimal
for i in range(180):
    t.pensize(3) #menambah ukuran pensil menjadi 2
    t.color('#00FFFF')
    t.circle(190 - i, 90)
    t.left(90)
    t.color("#800000")
    t.circle(190 - i, 90)
    t.left(18) 