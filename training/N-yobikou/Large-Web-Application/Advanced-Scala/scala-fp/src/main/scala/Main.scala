import scala.annotation.tailrec

object Main {

  @tailrec
  def series(n: Int, acc: Int): Int = {
    if (n == 0) {
      acc
    } else {
      series(n - 1, acc + n)
    }
  }

  @tailrec
  def fact(n: Int, acc: Int = 1): Int = if (n <= 1) acc else fact(n - 1, n * acc)

  case class Switch(isOn: Boolean)

  def toggle(switch: Switch): Switch = Switch(!switch.isOn)

  def twice(f: Int => Int): Int => Int = x => f(f(x))

}