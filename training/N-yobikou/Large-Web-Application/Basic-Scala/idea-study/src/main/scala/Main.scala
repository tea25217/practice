object Main extends App {
  val a = 2
  val z = 3
  printMulti
  println(s"a = ${a}")


  private def printMulti = {
    println(s"答えは${a * z}")
  }

}
