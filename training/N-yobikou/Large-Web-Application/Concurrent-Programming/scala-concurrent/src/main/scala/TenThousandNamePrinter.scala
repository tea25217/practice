import java.util.concurrent.{Callable, Executors}

object TenThousandNamePrinter extends App {
  val es = Executors.newFixedThreadPool(10)

  for (i <- 1 to 10000) {
    es.submit(new Runnable {
      override def run() = {
        Thread.sleep(1000)
        println(Thread.currentThread().getName)
      }})
  }

}