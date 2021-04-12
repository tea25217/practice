object CheckThenAct extends App {
  for (i <- 1 to 100) {
    new Thread(() => println(SingletonProvider.get)).start()
  }
}

object SingletonProvider {
  lazy val get: BigObject = new BigObject()
}

class BigObject() {
  Thread.sleep(1000)
}