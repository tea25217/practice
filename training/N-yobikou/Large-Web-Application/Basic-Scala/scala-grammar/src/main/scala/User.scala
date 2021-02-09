class User(private val name: String, private val age: Int) {

  override def toString = s"User($name, $age)"

}

object User {

  def apply(nameAndAge: String) = new User(nameAndAge.split(',')(0), nameAndAge.split(',')(1).toInt)

  def printAge(user: User): Unit = println(user.age)

}

object Cache {

  var map: Map[Int, String] = Map(0 -> "")

  def makeErr {

    val num = 214748364

    for (i <- 0 to num * 2 ) {
      map = map + ( i + 1 -> s"${map(i) + i}")
      if (i % 10000 == 0) {
        println(i)
        println(map(i))
      }
    }
    println("failed")
  }

}
