let x=[200,200]
let apple
function setup() {
  createCanvas(400, 400);
  apple=new items([10,10],[200,200],3,'banan',25)
}

function draw() {
  background(220);
  apple.move()
  apple.ormen()
  print(apple.x[0])
}
class items{
  constructor(vel,x,dmg,type,size){
    this.vel=vel
    this.x=x
    this.dmg=dmg
    this.type=type
    this.size=size
  }
  move(){
    this.x[0]+=this.vel[0]/60
    this.x[1]+=this.vel[1]/60
    this.size*=1.001
  }
  ormen(){
    circle(this.x[0],this.x[1],this.size)
  }
}